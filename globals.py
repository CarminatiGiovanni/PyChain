from classes.blockchain import Blockchain
from config import nodes

b = Blockchain([])  # instantiate the Blockchain object
NETWORK_NODES: list[str] = nodes  # where all the other chains url are stored
pool_pending_transactions: list = []