from flask import request
from . import main
from ..GLOBALS import b, NETWORK_NODES, pool_pending_transactions
from .. import clientios
from ..classes import Transaction, log
from time import time


@main.route('/', methods=['GET', 'POST'])
def index():
    """ main form """
    try:
        return b.to_dict(), 200
    except Exception as e:
        log(str(e))
        return str(e), 200


@main.route('/connect', methods=['GET'])
def connect_():
    clientios.register_nodes(NETWORK_NODES)
    return "OK", 200


@main.route('/blockchain_length', methods=['GET'])
def blockchain_length():
    return f"{len(b)}", 200


@main.route('/add_transaction', methods=['POST'])
def add_transaction():
    r_transaction = request.get_json()
    try:
        content_type = r_transaction['content_type']
        author = r_transaction['author']
        title = r_transaction['title']
        value = r_transaction['value']
        description = r_transaction['description']

        transaction_input_check_function(content_type, author, title, value, description)  # raise an error in case of wrong input

        t = Transaction(content_type, author, title, value, description, time())
        clientios.emit("new_transaction", t.to_dict())

        pool_pending_transactions.append(t)

        return {'status':"Transaction added to the pool"}, 200
    except Exception as e:
        return {'Error': str(e)}, 500


def transaction_input_check_function(content_type, author, title, value, description):
    # ok -> None, error -> str(error)
    # TODO: implement input checks
    if False:
        raise(Exception('Input error'))
    else:
        return
