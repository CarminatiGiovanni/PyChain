from .classes import Transaction, TransactionPoolList, Blockchain, Block
from .globals import NETWORK_NODES, pool_pending_transactions, b
from . import clientios
import random
from time import sleep


def poolAppendHandlerFunction(t: Transaction):
    print(NETWORK_NODES)

    # TODO: check the length of the pool pending transaction,\
    # if grater than BLock.transaction.__len__() build the block and broadcast it
    # with the PoET

    if len(pool_pending_transactions) > Blockchain.BLOCK_SIZE():
        DELAY_MILLISECONDS = random.randint(0,3000) # 0 to 3000 ms
        newBlock_transactions = []
        for i in range(Blockchain.BLOCK_SIZE()):
            # takes two transaction to insert in the block
            newBlock_transactions.append(pool_pending_transactions[random.randint(0,pool_pending_transactions.__len__()-1)])

        ocl = b.chain.__len__() # old chain length
        newBlock = Block(ocl,b.chain[ocl-1].hash,newBlock_transactions)

        sleep(DELAY_MILLISECONDS) # FIXME: check if there is a better way to sleep

        if len(b.chain) == newBlock.index:
            b.chain.append(newBlock) # append the new block

            for t in newBlock.transactions: # remove transactions from pool
                pool_pending_transactions.remove(t)

            clientios.emit("new_block", newBlock.to_dict()) # broadcast newBlockToOthers
        else:
            # when another block hash been already added
            # bring the transaction back to the pool
            pass
