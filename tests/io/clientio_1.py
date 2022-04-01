import socketio as sc

clientio1 = sc.Client()

@clientio1.event
def connect():
    print("Connected to the server!!!")