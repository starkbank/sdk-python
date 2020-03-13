from ....utils import rest
from ....utils.api import from_api_json
from ....utils.checks import check_datetime
from ....utils.resource import Resource
from ..boletoPayment import BoletoPayment


class BoletoPaymentLog(Resource):

    def __init__(self, id, created, type, errors, payment):
        Resource.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.payment = from_api_json(BoletoPayment, payment)


def get(id, user=None):
    return rest.get_id(resource=BoletoPaymentLog, id=id, user=user)


def query(limit=None, payment_ids=None, events=None, user=None):
    return rest.get_list(resource=BoletoPaymentLog, limit=limit, user=user, events=events, payment_ids=payment_ids)
