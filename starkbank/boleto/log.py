from starkbank import request
from starkbank.utils.base import Base
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_user, check_datetime
from .boleto import Boleto


class BoletoLog(Base):
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


def list(limit=100, cursor=None, user=None):
    response, errors = request.get(
        user=check_user(user),
        endpoint="boleto/log/",
        url_params={
            "limit": limit,
            "cursor": cursor,
        },
    )

    if errors:
        return None, errors

    return [BoletoLog.from_json(boleto) for boleto in response["logs"]], response["cursor"], []


def retrieve(id, user=None):
    response, errors = request.get(
        user=check_user(user),
        endpoint="boleto/log/{id}".format(id=id),
    )

    if errors:
        return None, errors

    return BoletoLog.from_json(response["log"]), []
