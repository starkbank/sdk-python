from starkbank.boleto_payment.boleto_payment import BoletoPayment
from starkbank.utils.base import Base, Get, GetId
from starkbank.utils.checks import check_datetime


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


list = BoletoPaymentLog._get
get = BoletoPaymentLog._get_id
