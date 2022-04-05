from app import create_app,serverio
from app.config import PORT, HOST

app = create_app(debug=True, template_folder="templates", static_folder="static")

if __name__ == '__main__':
    try:
        serverio.run(app,port=PORT)
    except Exception as e:
        print(str(e))
