from .. import serverio, clientios
from ..classes import Transaction, Block
from ..GLOBALS import pool_pending_transactions, b


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
        clientios.emit('new_transaction', transaction)


@serverio.on('new_block')
def new_block_(block):
    new_block: Block = Block.from_dict(block)
    print(str(new_block))

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
                print(f"removed transaction: ")
            except ValueError:
                pass

        b.chain.append(new_block)
        clientios.emit("new_block", new_block.to_dict())


def block_check(block: Block):
    if block.transactions.__len__() != b.BLOCK_SIZE():
        return False

    for t in block.transactions:
        if t not in pool_pending_transactions:
            return False

    if b.chain[len(b.chain)-1].hash != block.prevHash:
        return False

    return True
