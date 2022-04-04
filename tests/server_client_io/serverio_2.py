import flask_socketio as fs
from ..server_flask_socketio_client_2 import app

serverio2 = fs.SocketIO(app)


@serverio2.event
def connect():
    print('a user has connected')
