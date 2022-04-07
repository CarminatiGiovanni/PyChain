from flask import Blueprint

main = Blueprint('main', __name__)
diagnostic = Blueprint('diagnostic', __name__, url_prefix='/diagnostic')

from . import main_route, server_events, diagnostic_route
