from .classes.blockchain import Blockchain
from .config import nodes

test_dict = {
    'blockchain':[
        {'index':0,"prevHash":None,'hash':"firstHash829",'timestamp':4.00,'nonce':0,'transactions':[
            {'sender':"giovanni",'receiver':'Pietro','value':100,'timestamp':2.0},
            {'sender':"Fusini",'receiver':'Fustinoni','value':10,'timestamp':2.1}
        ]},
        {'index':1, "prevHash": 'firstHash829', 'hash': "oTHEhASH", 'timestamp': 5.00, 'nonce': 34, 'transactions': [
            {'sender': "mARTA", 'receiver': 'Mamma', 'value': 163, 'timestamp': 5.1},
            {'sender': "Papa", 'receiver': 'Nonns', 'value': 410, 'timestamp': 5.5}
        ]},
    ]}

# b = Blockchain()  # instantiate the Blockchain object
b = Blockchain.from_dict(test_dict)
NETWORK_NODES: list[str] = nodes  # where all the other chains url are stored
pool_pending_transactions: list = []