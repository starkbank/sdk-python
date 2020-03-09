from starkbank.utils.base import Base, Get
from starkbank.utils.checks import check_datetime


class Balance(Get):

    def __init__(self, amount, currency, updated, id):
        Base.__init__(self, id=id)

        self.amount = amount
        self.currency = currency
        self.updated = check_datetime(updated)


Balance._define_known_fields()

list = Balance._get
