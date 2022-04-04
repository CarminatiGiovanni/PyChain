
import socketio as sc

clientio2 = sc.Client()

@clientio2.event
def connect():
    print("Connected to the server!!!")