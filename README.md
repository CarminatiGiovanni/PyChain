# libraries to intall with pip:
    - flask
    - flask-socketio
    - eventlet
    - socketio

# edit for each server:
    - config.ini


```ini
# edit the port number
[SERVER]
PORT = 3000
HOST = localhost

#edit nodes routes
[nodes]
rasp3 = http://192.168.1.11:3000/
rasp4 = http://192.168.1.10:3000/
```    