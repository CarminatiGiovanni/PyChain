from . import Blockchain, Block
from .. import clientios, GLOBALS
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
        self.__appendCallback(t)

    def __appendCallback(self, t):
        print(f"hello len: {len(self)}")

        # TODO: check the length of the pool pending transaction,\
        # if grater than BLock.transaction.__len__() build the block and broadcast it
        # with the PoET

        if len(self) >= Blockchain.BLOCK_SIZE():
            DELAY_MILLISECONDS = random.randint(0, 3000)  # 0 to 3000 ms
            newBlock_transactions = []
            for i in range(Blockchain.BLOCK_SIZE()):
                # takes two transaction to insert in the block
                newBlock_transactions.append(self[i])

            ocl = GLOBALS.b.__len__()  # old chain length
            print("error here")
            newBlock = Block(ocl, GLOBALS.b.chain[ocl - 1].hash_, newBlock_transactions)
            print("ok")
            sleep(DELAY_MILLISECONDS)  # FIXME: check if there is a better way to sleep

            if len(GLOBALS.b.chain) == newBlock.index:
                GLOBALS.b.chain.append(newBlock)  # append the new block

                for t in newBlock.transactions:  # remove transactions from pool
                    self.remove(t)

                clientios.emit("new_block", newBlock.to_dict())  # broadcast newBlockToOthers
            else:
                # TODO: implement when another block has already been added
                # when another block hash been already added
                # bring the transaction back to the pool
                pass

