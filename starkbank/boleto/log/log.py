from starkbank import request
from starkbank.utils.base import Base, Get, GetId
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_user, check_datetime
from starkbank.boleto.boleto import Boleto


class BoletoLog(Get, GetId):
    _known_fields = {
        "id",
        "errors",
        "created",
        "event",
        "boleto",
    }
    _known_camel_fields = {snake_to_camel(field) for field in _known_fields}

    def __init__(self, id, created, event, errors, boleto):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.event = event
        self.errors = errors
        self.boleto = Boleto.from_json(boleto)

    @classmethod
    def endpoint(cls):
        return "boleto/log"


list = BoletoLog._list
get = BoletoLog._get
