from time import time
from hashlib import sha256
from .common import list_to_str, list_to_dict
from .transaction import Transaction

class Block:
    def __init__(self, index: int, prevHash: str, transactions: list):
        self.index = index
        self.prevHash = prevHash
        self.transactions = transactions
        self.nonce = 0
        self.hash = None
        self.timestamp = float(time())

        print("Creating new Block...")
        print(f"index:{self.index},prevHash:{self.prevHash},transactions:{len(self.transactions)},timestamp:{self.timestamp}")

        self._compute_hash()

        print("done")
        print(f"nonce:{self.nonce},hash:{self.hash}")

    def __init__(self, block: dict):
        try:
            self.index = block['index']
            self.prevHash = block['prevHash']
            self.transactions = []
            for transaction in block['transactions']:
                transaction.append(Transaction(transaction))
            self.nonce = block['nonce']
            self.hash = block['hash']
            self.timestamp = block['timestamp']
        except KeyError:
            self.__del__()

    def _compute_hash(self):
        self.hash = sha256(str(self)).hexdigest()

    def __str__(self):
        return "{" + f"index:{self.index},prevHash:{self.prevHash},transactions:{list_to_str(self.transactions)},timestamp:{self.timestamp}" + "}"

    def as_dict(self):
        return {'index': self.index, 'prevHash': self.prevHash, 'transactions': list_to_dict(self.transactions), 'timestamp': self.timestamp}

    def __del__(self):
        print('Del called')
