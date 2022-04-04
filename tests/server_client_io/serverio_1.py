import flask_socketio as fs
import tests.server_flask_socketio_client as tsf


serverio1 = fs.SocketIO(tsf.app)


@serverio1.event
def connect():
    print('a user has connected')
