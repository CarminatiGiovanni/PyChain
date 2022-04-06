class Transaction:

    def __init__(self, content_type: str, author: str, value: str, description: str, timestamp: float):
        self.content_type = content_type
        self.author = author
        self.value = value
        self.description = description
        self.timestamp = timestamp

    @classmethod
    def from_dict(cls, transaction: dict):
        content_type = transaction['content_type']
        author = transaction['author']
        value = transaction['value']
        description = transaction['description']
        timestamp = transaction['timestamp']
        return Transaction(content_type, author, value, description, timestamp)

    def __str__(self) -> str:
        return "{" + f"content_type:{self.content_type},author:{self.author},value:{self.value},description:{self.description},timestamp:{self.timestamp}" + "}"

    def to_dict(self):
        return {'content_type': self.content_type, 'author': self.author, 'value': self.value, "description": {self.description}, "timestamp": self.timestamp}
