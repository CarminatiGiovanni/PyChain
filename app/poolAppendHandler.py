from .classes import Transaction, TransactionPoolList
from .globals import NETWORK_NODES


def poolAppendHandlerFunction(t: Transaction):
    print(NETWORK_NODES)

    # TODO: check the length of the pool pending transaction,\
    # if grater than BLock.transaction.__len__() build the block and broadcast it
    # with the PoET

    pass
