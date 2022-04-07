from app import create_app, serverio
from app.config import PORT

app = create_app(debug=True, template_folder="template", static_folder="public")

if __name__ == '__main__':
    try:
        serverio.run(app, port=PORT)
    except Exception as e:
        print(str(e))
