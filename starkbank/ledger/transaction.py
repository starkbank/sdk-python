from starkbank.utils import rest
from starkbank.utils.base import Base
from starkbank.utils.checks import check_datetime


class Transaction(Base):

    _json_fill = {"receiverId": None}

    def __init__(self, amount, description, tags, external_id, receiver_id, sender_id=None, id=None, fee=None, created=None, source=None):
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


def create(transactions, user=None):
    return rest.post(resource=Transaction, entities=transactions, user=user)


def get(id, user=None):
    return rest.get_id(resource=Transaction, id=id, user=user)


def query(limit=100, external_ids=None, after=None, before=None, user=None):
    return rest.query(resource=Transaction, limit=limit, user=user, external_ids=external_ids, after=after, before=before)
