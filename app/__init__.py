from flask import Flask
from flask_socketio import SocketIO

serverio = SocketIO()

def create_app(debug = False, template_folder="", static_folder=""):
    """Create app object"""
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    app.debug = debug
    app.config['SECRET_KEY'] = "randomsevruhdg9829"

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    serverio.init_app(app)
    return app