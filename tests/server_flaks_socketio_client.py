from flask import Flask
import flask_socketio as fs
import socketio as sc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = fs.SocketIO(app)

clientio = sc.Client()

@clientio.event
def connect():
    print("Connected to the server!!!")

@socketio.event
def connect():
    print('a user has connected')

@app.route('/')
def main():
    return "Hello world",200

@app.route('/connect')
def connet_client():
    try:
        clientio.connect('http://localhost:5000/')
        print('client connected')
        return "Client connected",200
    except Exception as e:
        return f"Client not connected: {str(e)}", 500



if __name__ == '__main__':
    socketio.run(app, port= 4000, debug=True)

# pip install eventlet