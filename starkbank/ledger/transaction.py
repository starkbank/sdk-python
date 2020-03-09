from starkbank.utils.base import Base, Post, GetId, Get
from starkbank.utils.checks import check_datetime


class Transaction(Post, Get, GetId):

    _json_fill = ["receiverId"]

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


Transaction._define_known_fields()


create = Transaction._post
query = Transaction._query
get = Transaction._get_id
