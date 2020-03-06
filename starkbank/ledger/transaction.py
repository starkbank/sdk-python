from starkbank import request
from starkbank.utils.base import Base
from starkbank.utils.case import snake_to_camel, camel_to_snake
from starkbank.utils.checks import check_user, check_datetime


class Transaction(Base):

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

    def __init__(self, amount, description, tags, external_id, receiver_id, sender_id=None, id=None, fee=None, created=None, source=None):
        Base.__init__(self, id=id)

        self.amount = amount
        self.description = description
        self.tags = tags
        self.external_id = external_id
        self.receiver_id = receiver_id
        self.sender_id = sender_id
        self.fee = fee
        self.created = created
        self.source = source

    @classmethod
    def from_json(cls, json):
        json.setdefault("receiverId", None)
        return cls(**{
            camel_to_snake(k): v for k, v in json.items() if k in cls._known_camel_fields
        })


def create(transactions, user=None):
    response, errors = request.post(
        user=check_user(user),
        endpoint="transaction",
        body={
            "transactions": [
                {snake_to_camel(k): v for k, v in transaction.json().items() if v is not None} for transaction in transactions
            ]
        }
    )

    if errors:
        return None, errors

    return [
        Transaction.from_json(transaction) for transaction in response["transactions"]
    ], []


def retrieve(id, user=None):
    response, errors = request.get(
        user=check_user(user),
        endpoint="transaction/{id}".format(id=id),
    )

    if errors:
        return None, errors

    return Transaction.from_json(response["transaction"]), []


def list(limit=100, cursor=None, user=None):
    response, errors = request.get(
        user=check_user(user),
        endpoint="transaction/",
        url_params={
            "limit": limit,
            "cursor": cursor,
        },
    )

    if errors:
        return None, errors

    return [Transaction.from_json(transaction) for transaction in response["transactions"]], response["cursor"], []
