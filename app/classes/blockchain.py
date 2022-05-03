from .common import list_to_str, list_to_dict
from .block import Block


class Blockchain:

    @classmethod
    def BLOCK_SIZE(cls):
        return 2

    def __init__(self):
        self.chain = []

    def __len__(self):
        return len(self.chain)

    @classmethod
    def from_dict(cls, blockchain: list or dict):
        if type(blockchain) == list:
            chain = blockchain
        elif type(blockchain) == dict:
            try:
                chain = []
                for block in blockchain['blockchain']:
                    chain.append(Block.from_dict(block))
            except KeyError:
                return None
        else:
            return None

        b = Blockchain()
        b.chain = chain
        return b

    def __str__(self) -> str:
        return list_to_str(self.chain)

    def to_dict(self) -> dict:
        return {'blockchain': list_to_dict(self.chain)}

    def is_valid(self) -> bool:
        for i in range(1, len(self)):
            if self.chain[i-1].hash_ != self.chain[i].prevHash:
                return False
        return True
