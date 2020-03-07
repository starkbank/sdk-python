from starkbank import request
from starkbank.utils.base import Base
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_user, check_datetime
from .boleto import BoletoMessage
from .boleto_payment import BoletoPaymentMessage
from .transfer import TransferMessage


class Event(Base):

    _known_fields = {
        "id",
        "message",
        "delivered",
        "created",
    }
    _known_camel_fields = {snake_to_camel(field) for field in _known_fields}

    def __init__(self, message, created, delivered, id):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.delivered = check_datetime(delivered)

        if "transfer" in message:
            self.message = TransferMessage.from_json(message["transfer"])
            self.type = "transfer"
        elif "boleto" in message:
            if "issueDate" in message["boleto"]:  # TODO: remove
                message["boleto"]["created"] = message["boleto"].pop("issueDate")
            self.message = BoletoMessage.from_json(message["boleto"])
            self.type = "boleto"
        elif "boletoPayment" in message:
            self.message = BoletoPaymentMessage.from_json(message["boletoPayment"])
            self.type = "boleto_payment"


def retrieve(id, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="event/{id}".format(id=id),
    )

    return Event.from_json(response["event"])


def list(limit=100, cursor=None, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="event",
        url_params={
            "limit": limit,
            "cursor": cursor,
        },
    )

    return [Event.from_json(transfer) for transfer in response["events"]], response["cursor"]
