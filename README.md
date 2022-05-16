# getting started:

 1. git clone [https://github.com/HeyJOe03/PyChain.git](https://github.com/HeyJOe03/PyChain)
 2. cd PyChain (move to PyChain directory)
 3. pip install -r requirements.txt
 4. create config.ini
 5. python server.py

# edit for each server:
    - config.ini


```ini
# edit the port number
[SERVER]
PORT = 3000
HOST = 0.0.0.0

#edit nodes routes
[nodes]
rasp3 = http://192.168.1.11:3000/
rasp4 = http://192.168.1.10:3000/
```    