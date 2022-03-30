class Transaction:
    '''
    def __init__(self, sender: str, receiver: str, value: int, timestamp: float):
        self.sender = sender
        self.receiver = receiver
        self.value = value
        self.timestamp = timestamp
        '''

    def __init__(self, transaction: dict):
        try:
            self.sender = transaction['sender']
            self.receiver = transaction['receiver']
            self.value = transaction['value']
            self.timestamp = transaction['timestamp']
        except KeyError:
            self.__del__()

    def __str__(self) -> str:
        return "{" + f"sender:{self.sender},receiver:{self.receiver},value:{self.value},timestamp:{self.timestamp}" + "}"

    def as_dict(self):
        return {'sender': self.sender, 'receiver': self.receiver, 'value': self.value, "timestamp": self.timestamp}

    def __del__(self):
        print('Del called')
