from . import Block, Blockchain, Transaction
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
        self.__appendCallback()

    def __appendCallback(self):

        # TODO: check the length of the pool pending transaction,\
        # if grater than BLock.transaction.__len__() build the block and broadcast it
        # with the PoET

        if len(self) >= Blockchain.BLOCK_SIZE():
            DELAY_MILLISECONDS: float = random.randint(0, 3000) / 1000.0  # 0 to 3000 ms
            newBlock_transactions = []
            for i in range(Blockchain.BLOCK_SIZE()):
                # takes two transaction to insert in the block
                newBlock_transactions.append(self[i])

            ocl = GLOBALS.b.__len__()  # old chain length

            newBlock = Block(ocl, GLOBALS.b.chain[ocl - 1].hash_, newBlock_transactions)

            sleep(DELAY_MILLISECONDS)  # FIXME: check if there is a better way to sleep

            if len(GLOBALS.b.chain) == newBlock.index:
                for t in newBlock.transactions:  # remove transactions from pool
                    try:
                        self.remove(t)
                        print(f"transaction: {t.title} has been removed from transactions pool")
                    except ValueError:
                        pass

                GLOBALS.b.chain.append(newBlock)  # append the new block

                clientios.emit("new_block", newBlock.to_dict())  # broadcast newBlockToOthers
            else:
                # TODO: implement when another block has already been added
                # when another block hash been already added
                # bring the transaction back to the pool
                pass
