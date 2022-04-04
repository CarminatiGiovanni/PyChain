from flask import Flask
from server_client_io import serverio1, clientio1

app = Flask(__name__)


@app.route('/')
def main():
    return "Hello world", 200


@app.route('/connect')
def connect_client():
    try:
        clientio1.connect('http://localhost:5000/')
        print('client connected')
        return "Client connected",200
    except Exception as e:
        return f"Client not connected: {str(e)}", 500


if __name__ == '__main__':
    serverio1.run(app, port=4000, debug=True)
    