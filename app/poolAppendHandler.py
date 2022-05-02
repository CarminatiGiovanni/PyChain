from .classes import Transaction, TransactionPoolList, Blockchain, Block
from .globals import NETWORK_NODES, pool_pending_transactions, b
import random


def poolAppendHandlerFunction(t: Transaction):
    print(NETWORK_NODES)

    # TODO: check the length of the pool pending transaction,\
    # if grater than BLock.transaction.__len__() build the block and broadcast it
    # with the PoET

    if len(pool_pending_transactions) > Blockchain.BLOCK_SIZE():
        DELAY_MILLISECONDS = random.randint(0,3000) # 0 to 3000 ms
        newBlock_transactions = []
        for i in range(Blockchain.BLOCK_SIZE()):
            newBlock_transactions.append(pool_pending_transactions.pop(random.randint(0,pool_pending_transactions.__len__()-1)))

        ocl = b.chain.__len__() # old chain length
        newBlock = Block(ocl,b.chain[ocl-1],newBlock_transactions)

        # TODO implement delay and consensus

        # b.chain.append(newBlock)

    pass
