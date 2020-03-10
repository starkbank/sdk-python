from ...utils.base import Base, Get, GetId
from ...utils.checks import check_datetime
from ...boleto.log import BoletoLog
from ...transfer.log import TransferLog
from ...payment.boleto.log import BoletoPaymentLog


class Event(Get, GetId):

    _json_fill = {"delivered": True}

    def __init__(self, log, created, delivered, subscription, id):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.delivered = check_datetime(delivered)
        self.subscription = subscription
        self.log = _process_log(log=log, subscription=subscription)

    @classmethod
    def _query(cls, limit=100, after=None, before=None, is_delivered=None, user=None):
        return super(Event, cls)._query(
            limit=limit,
            after=after,
            before=before,
            is_delivered=is_delivered,
            user=user,
        )


def _process_log(log, subscription):
    return {
        "transfer": TransferLog.from_json(log),
        "boleto": BoletoLog.from_json(log),
        "boleto-payment": BoletoPaymentLog.from_json(log),
    }[subscription]


Event._define_known_fields()

get = Event._get_id
query = Event._query
