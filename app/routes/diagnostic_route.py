from flask import request, jsonify
from . import diagnostic
from ..globals import b, NETWORK_NODES, pool_pending_transactions
from .. import clientios
from ..classes.common import list_to_dict


@diagnostic.route('/blockchain', methods=['GET', 'POST'])
def blockchain():
    """ main form """
    try:
        print(b.to_dict())
        return b.to_dict(), 200
    except Exception as e:
        print(str(e))
        return str(e), 200


@diagnostic.route('/socket_connection', methods=['GET', 'POST'])
def socket_connection():
    return clientios.to_dict(), 200


@diagnostic.route('/transaction_pool', methods=['GET', 'POST'])
def transaction_pool():
    return {'transaction\'s pool': list_to_dict(pool_pending_transactions)}, 200


@diagnostic.route('/network_nodes')
def network_nodes():
    return {'NETWORK_NODES': NETWORK_NODES}, 200
    