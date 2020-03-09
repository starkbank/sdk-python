from starkbank.utils.base import Base, Get, GetId
from starkbank.utils.checks import check_datetime
from .boleto import BoletoMessage
from .boleto_payment import BoletoPaymentMessage
from .transfer import TransferMessage


class Event(Get, GetId):

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


Event._define_known_fields()

get = Event._get_id
query = Event._query
