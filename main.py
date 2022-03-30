from flask import Flask, jsonify
from config import PORT, HOST
from globals import b
from routes import *

# instantiate the app component, also set static and HTML templates folder
app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route('/',methods=['POST','GET'])
def entry_page():
    return jsonify(blockchain = b.to_dict())

if __name__ == '__main__':
    try:
        # THIS STARTS THE SERVER
        # this is a BLOCKING TASK !!!
        app.run(debug=True, host=HOST, port=PORT)
    except Exception as e:
        print(str(e))
