from starkbank import request
from starkbank.utils.base import Base
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_user, check_datetime
from starkbank.boleto_payment.boleto_payment import BoletoPayment


class BoletoPaymentLog(Base):
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


def list(limit=100, cursor=None, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="boleto-payment/log/",
        url_params={
            "limit": limit,
            "cursor": cursor,
        },
    )

    return [BoletoPaymentLog.from_json(boleto) for boleto in response["logs"]], response["cursor"]


def retrieve(id, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="boleto-payment/log/{id}".format(id=id),
    )

    return BoletoPaymentLog.from_json(response["log"])
