class Transaction:

    def __init__(self, content_type: str, author: str, title: str, value: str, description: str, timestamp: float):
        self.content_type = content_type
        self.author = author
        self.value = value
        self.title = title
        self.description = description
        self.timestamp = timestamp

    @classmethod
    def from_dict(cls, transaction: dict):
        content_type = transaction['content_type']
        author = transaction['author']
        value = transaction['value']
        title = transaction['title']
        description = transaction['description']
        timestamp = transaction['timestamp']
        return Transaction(content_type, author, title, value, description, timestamp)

    def __str__(self) -> str:
        return "{" + f"content_type:{self.content_type},author:{self.author},title:{self.author},value:{self.value},description:{self.description},timestamp:{self.timestamp}" + "}"

    def to_dict(self) -> dict:
        return {'content_type': self.content_type, 'author': self.author, 'title': self.title, 'value': self.value, "description": self.description, "timestamp": self.timestamp}

    def __eq__(self, t) -> bool:
        if self.timestamp != t.timestamp \
                or self.content_type != t.content_type \
                or self.author != t.author \
                or self.title != t.title \
                or self.value != t.value \
                or self.description != t.description:
            return False
        else:
            return True
