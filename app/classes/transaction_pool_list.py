import requests

from . import Block, Blockchain, log
from .. import clientios, GLOBALS
# from ..routes import consensus_routine
import requests as r
from random import randint
import random
from time import sleep
from threading import Thread
import sys


class TransactionPoolList(list):
    def __init__(self, pool=None):
        super().__init__()
        if pool is None:
            pool = []
        super().extend(pool)
        self.consensus_thread = Thread(target=self.__wait_consensus_thread)

    def append(self, t):
        super().append(t)
        self.__appendCallback()

    def __appendCallback(self):

        if len(self) >= Blockchain.BLOCK_SIZE() and not self.consensus_thread.is_alive():  # When the number of pending transaction is grater than the block transaction length
            try:
                self.consensus_thread.join()
            except RuntimeError:  # cannot join thread before it is started
                pass
            self.consensus_thread = Thread(target=self.__wait_consensus_thread)  # Thread must be recreated
            self.consensus_thread.start()

    def __wait_consensus_thread(self):
        DELAY_MILLISECONDS: float = random.randint(0, 3000) / 1000.0  # 0 to 3000 ms
        newBlock_transactions = []
        for i in range(Blockchain.BLOCK_SIZE()):
            newBlock_transactions.append(self[i])  # takes two transaction to insert in the block

        ocl = GLOBALS.b.__len__()  # old chain length, used as block index

        newBlock = Block(ocl, GLOBALS.b.last_block().hash_, newBlock_transactions)

        sleep(DELAY_MILLISECONDS)  # FIXME: check if there is a better way to sleep

        if len(GLOBALS.b) == newBlock.index:
            for t in newBlock.transactions:  # remove transactions from pool
                try:
                    self.remove(t)
                except ValueError:
                    pass

            clientios.emit("new_block", newBlock.to_dict())  # broadcast newBlockToOthers
            GLOBALS.b.chain.append(newBlock)  # append the new block

            consensus_routine()

        sys.exit()


def consensus_routine():
    # call is valid
    if not GLOBALS.b.is_valid():

        try:
            new_blockchain_dict = r.get(GLOBALS.NETWORK_NODES[randint(0,len(GLOBALS.NETWORK_NODES) -1)])

            GLOBALS.b.copy(Blockchain.from_dict(new_blockchain_dict))

        except Exception as e:
            log(str(e))

    else:
        greater = {"address": "","length": -1}
        for n in GLOBALS.NETWORK_NODES:
            try:
                length = r.get(n+'/blockchain_length')
                if int(length.text) > greater['length']:
                    greater = {"address": n,"length": int(length.text)}
            except Exception as e:
                log(str(e))

        if len(GLOBALS.b) < greater["length"]:
            try:
                new_blockchain_dict = r.get(GLOBALS.NETWORK_NODES[randint(0, len(GLOBALS.NETWORK_NODES) - 1)])
                GLOBALS.b.copy(Blockchain.from_dict(new_blockchain_dict.json()))
            except Exception as e:
                log(str(e))

    t_pool_dict = []
    for t in GLOBALS.pool_pending_transactions:
        t_pool_dict.append(t.to_dict())

    clientios.emit("transaction_pool",t_pool_dict)
