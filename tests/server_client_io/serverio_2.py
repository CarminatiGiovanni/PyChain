import flask_socketio as fs
import tests.server_flask_socketio_client_2 as tsf

serverio2 = fs.SocketIO(tsf.app)


@serverio2.event
def connect():
    print('a user has connected')
