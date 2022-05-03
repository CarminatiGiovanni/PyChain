from . import Block, Blockchain
from .. import clientios, GLOBALS
# from ..routes import consensus_routine
import requests as r
from random import randint
import random
from time import sleep


class TransactionPoolList(list):
    def __init__(self, pool=None):
        super().__init__()
        if pool is None:
            pool = []
        super().extend(pool)

    def append(self, t):
        super().append(t)
        self.__appendCallback()

    def __appendCallback(self):

        if len(self) >= Blockchain.BLOCK_SIZE():  # When the number of pending transaction is grater than the block transaction length
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


def consensus_routine():
    # call is valid
    if not GLOBALS.b.is_valid():

        new_blockchain_dict = r.get(GLOBALS.NETWORK_NODES[randint(0,len(GLOBALS.NETWORK_NODES) -1)])

        GLOBALS.b.copy(Blockchain.from_dict(new_blockchain_dict))

    else:
        # ask for the blockchain length
        pass

    # broadcast transaction pool
    # join other nodes transaction pool

