from ....utils import rest
from ....utils.api import define_compatibility_fields, from_api_json
from ....utils.checks import check_datetime
from ....utils.base import Base
from ..boleto_payment import BoletoPayment


class BoletoPaymentLog(Base):

    def __init__(self, id, created, type, errors, payment):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.payment = from_api_json(BoletoPayment, payment)


define_compatibility_fields(BoletoPaymentLog)


def get(id, user=None):
    return rest.get_id(resource=BoletoPaymentLog, id=id, user=user)


def query(limit=100, payment_ids=None, events=None, user=None):
    return rest.query(resource=BoletoPaymentLog, limit=limit, user=user, events=events, payment_ids=payment_ids)
