import os, sys

sys.path.append(os.path.dirname(__file__))

from app import create_app, serverio
from app.config import PORT, template_folder, static_folder, HOST

app = create_app(debug=True, template_folder=template_folder, static_folder=static_folder)

if __name__ == '__main__':
    try:
        serverio.run(app,host= HOST, port=PORT)
    except Exception as e:
        print(str(e))
