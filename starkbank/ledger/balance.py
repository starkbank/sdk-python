from starkbank.utils import rest
from starkbank.utils.base import Base
from starkbank.utils.checks import check_datetime


class Balance(Base):

    def __init__(self, amount, currency, updated, id):
        Base.__init__(self, id=id)

        self.amount = amount
        self.currency = currency
        self.updated = check_datetime(updated)


def get(user=None):
    balances, cursor = rest.get(resource=Balance, user=user)
    return balances[0]
