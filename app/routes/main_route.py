from flask import request, jsonify
from . import main
from ..globals import b, NETWORK_NODES, pool_pending_transactions
from .. import clientios
from ..classes.transaction import Transaction
from time import time


@main.route('/', methods=['GET', 'POST'])
def index():
    """ main form """
    try:
        print(b.to_dict())
        return b.to_dict(), 200
    except Exception as e:
        print(str(e))
        return str(e), 200


@main.route('/connect', methods=['GET'])
def connect_():
    clientios.register_nodes(NETWORK_NODES)
    return "OK", 200


@main.route('/add_transaction', methods=['POST'])
def add_transaction():
    r_transaction = request.get_json()
    try:
        content_type = r_transaction['content_type']
        author = r_transaction['author']
        title = r_transaction['title']
        value = r_transaction['value']
        description = r_transaction['description']

        transaction_input_check_function(content_type, author, title, value, description)

        t = Transaction(content_type, author, title, value, description, time())
        pool_pending_transactions.append(t)

        clientios.emit("new_transaction", t.to_dict())

        return "Transaction added to the pool", 200
    except Exception as e:
        print(str(e))
        return {'Error': str(e)}, 500


def transaction_input_check_function(content_type, author, title, value, description):
    # ok -> None, error -> str(error)
    # TODO: implement input checks
    if False:
        raise(Exception('Input error'))
    else:
        return

'''
@main.route('/diagnostic/socket_connection', methods=['GET', 'POST'])
def socket_connection():
    return clientios.to_dict(), 200
'''
