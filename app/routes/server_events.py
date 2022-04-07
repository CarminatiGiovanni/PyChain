from flask_socketio import emit, join_room, leave_room
from .. import serverio
from ..classes.transaction import Transaction
from ..globals import pool_pending_transactions
from .. import clientios


@serverio.on('message')
def message(msg):
    print(msg)


@serverio.event
def connection():
    print('A user has connected')


@serverio.on('new_transaction')
def new_transaction(transaction):
    t = Transaction.from_dict(transaction)
    if t not in pool_pending_transactions:
        pool_pending_transactions.append(t)
        clientios.emit('new_transaction',transaction)
