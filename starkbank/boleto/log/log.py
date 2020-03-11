from starkbank.utils import rest
from starkbank.utils.api import define_compatibility_fields
from starkbank.utils.checks import check_datetime
from starkbank.boleto.boleto import Boleto
from starkbank.utils.api import from_api_json
from starkbank.utils.base import Base


class BoletoLog(Base):
    def __init__(self, id, created, type, errors, boleto):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.boleto = from_api_json(Boleto, boleto)


define_compatibility_fields(BoletoLog)


def get(id, user=None):
    return rest.get_id(resource=BoletoLog, id=id, user=user)


def query(limit=None, boleto_ids=None, events=None, user=None):
    return rest.query(resource=BoletoLog, limit=limit, user=user, events=events, boleto_ids=boleto_ids)
