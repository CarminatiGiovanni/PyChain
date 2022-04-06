from .classes.blockchain import Blockchain
from .config import nodes

test_dict = dict(blockchain=[
    {'index': 0, "prevHash": None, 'hash': "firstHash829", 'timestamp': 4.00, 'nonce': 0, 'transactions': [
        {'content_type': 'text', 'author': 'G. D\'Annunzio', 'title': 'Alcyone', 'value': 'Ludi del cielo\nDel mare\nDella terra e\nDegli eroi', "description": "Libro originale del 1942", "timestamp": 5.0},
        {'content_type': 'text', 'author': 'Dante', 'title': 'Divina Commedia', 'value': 'Nel mezzo del cammin di nostra vita\nmi ritrovai in una selva oscura\nche la diritta via era smarrita', "description": "Canto I", "timestamp": 5.1}
    ]},
    {'index': 1, "prevHash": 'firstHash829', 'hash': "oTHEhASH", 'timestamp': 5.00, 'nonce': 34, 'transactions': [
        {'content_type': 'text', 'author': 'M. L. King', 'title': 'I have a dream', 'value': 'That one day.....', "description": "Discorso vs leggi raziali", "timestamp": 5.2},
        {'content_type': 'text', 'author': 'G. Leopardi', 'title': 'L\'infinito', 'value': 'Sempre caro mi fu quest\'ermo colle,\ne questa siepe, che da tanta parte\ndell\'ultimo orizzonte il guardo esclude.', "description": "Sonetto di G. Leopardi", "timestamp": 5.3}
    ]},
])

# b = Blockchain()  # instantiate the Blockchain object
b = Blockchain.from_dict(test_dict)
NETWORK_NODES: list[str] = nodes  # where all the other chains url are stored
pool_pending_transactions: list = []
