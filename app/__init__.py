from flask import Flask
from flask_socketio import SocketIO
from socketio import Client

clientio = Client()

serverio = SocketIO()


def before_first_request():
    try:
        # clientio.connect('http://localhost:4000')
        print('Client connected')
    except Exception as e:
        print(str(e))


def create_app(debug=False, template_folder="", static_folder=""):
    """Create app object"""
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    app.debug = debug
    app.config['SECRET_KEY'] = "6967979699829"
    app.before_first_request(before_first_request)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    serverio.init_app(app)
    return app
