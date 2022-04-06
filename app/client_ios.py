from socketio import Client


class ClientIOS:
    def __init__(self, network_nodes=[]):
        self.ios: list[Client] = []
        for node in network_nodes:
            clientio = Client()
            try:
                clientio.connect(f"http://{node}:3000")
                self.ios.append(clientio)
            except Exception as e:
                print("impossible connect to " + node)

    def register_nodes(self, network_nodes=[]):
        self.ios: list[Client] = []
        for node in network_nodes:
            clientio = Client()
            try:
                clientio.connect(f"http://{node}:3000")
                self.ios.append(clientio)
            except Exception as e:
                print("impossible connect to " + node)

    def emit(self, call, message):
        for c in self.ios:
            c.emit(call, message)
