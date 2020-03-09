from ....utils.base import Base, Get, GetId
from ....utils.checks import check_datetime
from ..boleto_payment import BoletoPayment


class BoletoPaymentLog(Get, GetId):

    def __init__(self, id, created, event, errors, payment):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.event = event
        self.errors = errors
        self.payment = BoletoPayment.from_json(payment)

    @classmethod
    def _endpoint(cls):
        return "boleto-payment/log"


BoletoPaymentLog._define_known_fields()


query = BoletoPaymentLog._query
get = BoletoPaymentLog._get_id