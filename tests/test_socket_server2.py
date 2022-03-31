from flask import Flask
from flask_socketio import SocketIO, send
from socketio import Client

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketIO = SocketIO(app)

clientio = Client()


@clientio.event
def connect():
    print('socket connected to http://localhost:5000')


@clientio.event
def connect_error():
    print('connection error')

@app.route('/')
def hello():
    clientio.connect('http://localhost:5000')
    return "Hello world",200


if __name__ == '__main__':
    socketIO.run(app, port= 4000)