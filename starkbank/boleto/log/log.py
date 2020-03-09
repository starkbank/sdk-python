from starkbank.utils.base import Base, Get, GetId
from starkbank.utils.checks import check_datetime
from starkbank.boleto.boleto import Boleto


class BoletoLog(Get, GetId):
    def __init__(self, id, created, type, errors, boleto):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.boleto = Boleto.from_json(boleto)

    @classmethod
    def _endpoint(cls):
        return "boleto/log"

    @classmethod
    def _query(cls, limit=100, boleto_ids=None, events=None):
        return super(BoletoLog, cls)._query(
            limit=limit,
            boleto_ids=boleto_ids,
            events=events,
        )


BoletoLog._define_known_fields()


query = BoletoLog._query
get = BoletoLog._get_id
