from starkbank.utils.base import Base, Post, GetId, Get
from starkbank.utils.checks import check_datetime, check_date_string


class Transaction(Post, Get, GetId):

    _json_fill = {"receiverId": None}

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
    def _query(cls, limit=100, externalIds=None, after=None, before=None, user=None):
        return super(Transaction, cls)._query(
            limit=limit,
            externalIds=externalIds,
            after=after,
            before=before,
            user=user,
        )


Transaction._define_known_fields()


create = Transaction._post
query = Transaction._query
get = Transaction._get_id
