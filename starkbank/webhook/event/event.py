from ...utils import rest
from ...utils.api import from_api_json
from ...utils.base import Base
from ...utils.checks import check_datetime
from ...boleto.log import BoletoLog
from ...transfer.log import TransferLog
from ...payment.boleto.log import BoletoPaymentLog


class Event(Base):

    def __init__(self, log, created, delivered, subscription, id):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.delivered = check_datetime(delivered)
        self.subscription = subscription
        self.log = _process_log(log=log, subscription=subscription)


def _process_log(log, subscription):
    return from_api_json(*{
        "transfer": (TransferLog, log),
        "boleto": (BoletoLog, log),
        "boleto-payment": (BoletoPaymentLog, log),
    }[subscription])


def get(id, user=None):
    return rest.get_id(resource=Event, id=id, user=user)


def query(limit=None, after=None, before=None, is_delivered=None, user=None):
    return rest.query(resource=Event, limit=limit, user=user, is_delivered=is_delivered, after=after, before=before)
