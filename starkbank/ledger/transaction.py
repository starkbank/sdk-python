from starkbank.utils.base import Base, Post, GetId, Get
from starkbank.utils.case import snake_to_camel, camel_to_snake
from starkbank.utils.checks import check_datetime


class Transaction(Post, Get, GetId):
    _known_fields = {
        "amount",
        "description",
        "tags",
        "external_id",
        "receiver_id",
        "sender_id",
        "id",
        "fee",
        "created",
        "source",
    }
    _known_camel_fields = {snake_to_camel(field) for field in _known_fields}

    def __init__(self, amount, description, tags, external_id, receiver_id, sender_id=None, id=None, fee=None,
                 created=None, source=None):
        Base.__init__(self, id=id)

        self.amount = amount
        self.description = description
        self.tags = tags
        self.external_id = external_id
        self.receiver_id = receiver_id
        self.sender_id = sender_id
        self.fee = fee
        self.created = check_datetime(created)
        self.source = source

    @classmethod
    def from_json(cls, json):
        json.setdefault("receiverId", None)
        return cls(**{
            camel_to_snake(k): v for k, v in json.items() if k in cls._known_camel_fields
        })


create = Transaction._create
list = Transaction._list
get = Transaction._get
