from .block import Block
from .common import list_to_str, list_to_dict


class Blockchain:
    def __init__(self, blockchain: list[Block] or dict ):
        if type(blockchain) == list:
            self.chain = blockchain
        elif type(blockchain) == dict:
            try:
                self.chain = []
                for block in blockchain['blockchain']:
                    self.chain.append(Block(block))
            except KeyError:
                self.__del__()
        else:
            self.__del__()

    def __str__(self) -> str:
        return list_to_str(self.chain)

    def as_dict(self) -> dict:
        return {'blockchain': list_to_dict(self.chain)}

    def __del__(self):
        print('Del called!!')
