from flask import request, jsonify
from . import main

@main.route('/',methods=['GET','POST'])
def index():
    """ main form """
    return jsonify(hello = 'world')