from starkbank.boleto_payment.boleto_payment import BoletoPayment
from starkbank.utils.base import Base, Get, GetId
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_datetime


class BoletoPaymentLog(Get, GetId):
    _known_fields = {
        "id",
        "errors",
        "created",
        "event",
        "payment",
    }
    _known_camel_fields = {snake_to_camel(field) for field in _known_fields}

    def __init__(self, id, created, event, errors, payment):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.event = event
        self.errors = errors
        self.payment = BoletoPayment.from_json(payment)

    @classmethod
    def endpoint(cls):
        return "boleto-payment/log"


list = BoletoPaymentLog._list
get = BoletoPaymentLog._get
