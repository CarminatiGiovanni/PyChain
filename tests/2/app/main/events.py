from flask_socketio import emit, join_room, leave_room
from .. import serverio

@serverio.on('message')
def message(msg):
    print(msg)

@serverio.event
def connection():
    print('A user has connected')