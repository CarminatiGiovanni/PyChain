from app import create_app, serverio
from app.config import PORT, HOST
from socketio import Client

app = create_app(debug=True, template_folder="templates", static_folder="static")

clientio = Client()


@app.before_first_request
def before_first_request():
    try:
        clientio.connect("http://localhost:4000")
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    try:
        serverio.run(app, port=PORT)
    except Exception as e:
        print(str(e))
