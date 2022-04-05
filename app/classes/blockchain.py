from . import list_to_str, list_to_dict, Block


class Blockchain:

    def __init__(self):
        self.chain = []

    @classmethod
    def from_dict(cls, blockchain: list[Block] or dict ):
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

    def __del__(self):
        print('Del called!!')
