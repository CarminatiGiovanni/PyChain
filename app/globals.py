from .classes.blockchain import Blockchain
from .config import nodes

b = Blockchain()  # instantiate the Blockchain object
# b = Blockchain.from_dict(test_dict)
NETWORK_NODES: list[str] = nodes  # where all the other chains url are stored
pool_pending_transactions: list = []