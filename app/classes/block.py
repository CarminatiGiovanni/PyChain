from time import time
from hashlib import sha256
from .common import list_to_str, list_to_dict
from .transaction import Transaction


class Block:
    def __init__(self, index: int, prevHash: str, transactions: list, nonce=0, hash_=None, timestamp=float(time())):
        self.index = index
        self.prevHash = prevHash
        self.transactions = transactions  # TODO: check the transaction length
        self.nonce = nonce
        self.hash_ = hash_
        self.timestamp = timestamp

        if self.hash_ is None:
            print("---------------------------------------------")
            print("Creating new Block...")
            print(f"index:{self.index},prevHash:{self.prevHash},transactions:{len(self.transactions)},timestamp:{self.timestamp}")

            self._compute_hash()

            print(f"nonce:{self.nonce},hash:{self.hash_}")
            print("---------------------------------------------")

    @classmethod
    def from_dict(cls, block: dict):
        try:
            index = block['index']
            prevHash = block['prevHash']
            transactions = []
            for transaction in block['transactions']:
                transactions.append(Transaction.from_dict(transaction))
            nonce = block['nonce']
            hash_ = block['hash']
            timestamp = block['timestamp']

            return Block(index, prevHash, transactions, nonce, hash_, timestamp)

        except KeyError:
            return None

    def _compute_hash(self):
        self.hash_ = sha256(self.__str_for_hash().encode('utf-8')).hexdigest()

    def __str__(self):
        return "{" + f"index:{self.index},prevHash:{self.prevHash},transactions:{list_to_str(self.transactions)},timestamp:{self.timestamp},hash:{self.hash_}" + "}"

    def __str_for_hash(self):
        return "{" + f"index:{self.index},prevHash:{self.prevHash},transactions:{list_to_str(self.transactions)},timestamp:{self.timestamp},nonce:{self.nonce}" + "}"

    def to_dict(self):
        return {'index': self.index, 'prevHash': self.prevHash, 'transactions': list_to_dict(self.transactions), 'timestamp': self.timestamp, "hash": self.hash_, "nonce": self.nonce}
