from ..utils import rest
from ..utils.resource import Resource
from ..utils.checks import check_datetime


class Balance(Resource):

    def __init__(self, amount, currency, updated, id):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.currency = currency
        self.updated = check_datetime(updated)


def get(user=None):
    return next(rest.get_list(resource=Balance, user=user))
