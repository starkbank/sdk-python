from starkbank.utils.base import Base, Get, GetId
from starkbank.utils.checks import check_datetime
from starkbank.boleto.boleto import Boleto


class BoletoLog(Get, GetId):
    def __init__(self, id, created, event, errors, boleto):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.event = event
        self.errors = errors
        self.boleto = Boleto.from_json(boleto)

    @classmethod
    def _endpoint(cls):
        return "boleto/log"


BoletoLog._define_known_fields()


query = BoletoLog._query
get = BoletoLog._get_id
