from starkbank import request
from starkbank.utils.base import Base, Get
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_user, check_datetime


class Balance(Get):
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


list = Balance._list
