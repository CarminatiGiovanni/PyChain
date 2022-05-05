from .. import serverio, clientios
from ..classes import Transaction, Block
from ..GLOBALS import pool_pending_transactions, b
from ..classes import consensus_routine


@serverio.on('message')
def message(msg):
    print(msg)


@serverio.event
def connection():
    print('A user has connected')


@serverio.on('new_transaction')
def new_transaction(transaction):
    t = Transaction.from_dict(transaction)
    if t not in pool_pending_transactions and t not in b.last_block().transactions:
        print('appending transaction (from socket)')
        pool_pending_transactions.append(t)
        print("transaction from socket appended")
        clientios.emit('new_transaction', transaction)


@serverio.on('transaction_pool')
def transaction_pool_update(new_pool):
    for t in new_pool:
        transaction = Transaction.from_dict(t)
        if transaction not in pool_pending_transactions:
            pool_pending_transactions.append(transaction)
            clientios.emit("new_transaction",t)


@serverio.on('new_block')
def new_block_(block):
    new_block: Block = Block.from_dict(block)

    if new_block is None:
        print('ERROR new block is None')
        return

    if new_block in b.chain:
        return

    if new_block.index < b.chain.__len__():
        return
    elif new_block.index > b.chain.__len__():
        # TODO: implement when node is not updated to the new blockchain length
        pass
    else:
        # check if transactions are in the pool + transactions length + hash
        if not block_check(new_block):
            return

        for t in new_block.transactions:
            try:
                pool_pending_transactions.remove(t)
                print(f"removed transaction: {t.title}")
                print(pool_pending_transactions.__len__())
            except ValueError:
                pass

        b.chain.append(new_block)
        clientios.emit("new_block", new_block.to_dict())

        consensus_routine()


def block_check(block: Block):
    if block.transactions.__len__() != b.BLOCK_SIZE():
        return False

    for t in block.transactions:
        if t not in pool_pending_transactions:
            return False

    if b.last_block().hash != block.prevHash:
        return False

    return True
