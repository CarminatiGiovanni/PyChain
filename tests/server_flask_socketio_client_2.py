from flask import Flask
from server_client_io import clientio2, serverio2

app = Flask(__name__)


@app.route('/')
def main():
    return "Hello world", 200


@app.route('/connect')
def connect_client():
    try:
        clientio2.connect('http://localhost:4000/')
        print('client connected')
        return "Client connected", 200
    except Exception as e:
        return f"Client not connected: {str(e)}", 500


if __name__ == '__main__':
    serverio2.run(app, port=5000, debug=True)
