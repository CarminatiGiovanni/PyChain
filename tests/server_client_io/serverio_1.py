import flask_socketio as fs
from ..server_flask_socketio_client import app


serverio1 = fs.SocketIO(app)


@serverio1.event
def connect():
    print('a user has connected')
