from app import create_app,serverio

app = create_app(debug=True)

if __name__ == '__main__':
    serverio.run(app, port=5000)