from flask import Flask
from flask_socketio import SocketIO
from .client_ios import ClientIOS

clientios: ClientIOS = ClientIOS()

from .GLOBALS import NETWORK_NODES

serverio: SocketIO = SocketIO()


def before_first_request():
    clientios.register_nodes(NETWORK_NODES)


def create_app(debug=False, template_folder="", static_folder=""):
    """Create app object"""
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    app.debug = debug
    app.config['SECRET_KEY'] = "6967979699829"
    app.before_first_request(before_first_request)

    from .routes import main as main_blueprint, diagnostic as diagnostic_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(diagnostic_blueprint)

    serverio.init_app(app)
    return app
