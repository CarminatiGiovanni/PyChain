from .classes import Transaction
from .globals import NETWORK_NODES


def poolAppendHandler(t: Transaction):
    print(len(NETWORK_NODES))
