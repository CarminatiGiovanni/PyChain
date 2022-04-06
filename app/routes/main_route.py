from flask import request, jsonify
from . import main
from ..globals import b, NETWORK_NODES
from .. import clientios


@main.route('/', methods=['GET', 'POST'])
def index():
    """ main form """
    return b.to_dict(), 200


@main.route('/connect', methods=['GET'])
def connect_():
    clientios.register_nodes(NETWORK_NODES)
    return "OK", 200


@main.route('/diagnostic/socket_connection', methods=['GET', 'POST'])
def socket_connection():
    return clientios.to_dict(), 200
