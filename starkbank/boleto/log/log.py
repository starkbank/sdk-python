from starkbank.utils import rest
from starkbank.utils.base import Base
from starkbank.utils.checks import check_datetime
from starkbank.boleto.boleto import Boleto


class BoletoLog(Base):
    def __init__(self, id, created, type, errors, boleto):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.boleto = Boleto.from_json(boleto)

    @classmethod
    def _endpoint(cls):
        return "boleto/log"


BoletoLog._define_known_fields()


def get(id, user=None):
    return rest.get_id(resource=BoletoLog, id=id, user=user)


def query(limit=100, boleto_ids=None, events=None, user=None):
    return rest.query(resource=BoletoLog, limit=limit, user=user, events=events, boleto_ids=boleto_ids)
