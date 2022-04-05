class Transaction:

    def __init__(self, sender: str, receiver: str, value: int, timestamp: float):
        self.sender = sender
        self.receiver = receiver
        self.value = value
        self.timestamp = timestamp

    @classmethod
    def from_dict(cls, transaction: dict):
        sender = transaction['sender']
        receiver = transaction['receiver']
        value = transaction['value']
        timestamp = transaction['timestamp']
        return Transaction(sender,receiver,value,timestamp)

    def __str__(self) -> str:
        return "{" + f"sender:{self.sender},receiver:{self.receiver},value:{self.value},timestamp:{self.timestamp}" + "}"

    def to_dict(self):
        return {'sender': self.sender, 'receiver': self.receiver, 'value': self.value, "timestamp": self.timestamp}
