from starkbank import request
from starkbank.utils.base import Base
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_user, check_datetime


class Balance(Base):

    _known_fields = {
        "id",
        "amount",
        "currency",
        "updated",
    }
    _known_camel_fields = {snake_to_camel(field) for field in _known_fields}

    def __init__(self, amount, currency, updated, id):
        Base.__init__(self, id=id)

        self.amount = amount
        self.currency = currency
        self.updated = check_datetime(updated)


def list(limit=100, cursor=None, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="balance/",
        url_params={
            "limit": limit,
            "cursor": cursor,
        },
    )

    return [Balance.from_json(balance) for balance in response["balances"]], response["cursor"]
