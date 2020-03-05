from starkbank import request
from starkbank.utils.base import Base
from starkbank.utils.case import snake_to_camel, camel_to_snake
from starkbank.utils.checks import check_user, check_datetime
from .boleto import from_json as boleto_from_json

known_fields = {
    "id",
    "errors",
    "created",
    "event",
    "boleto",
}

known_camel_fields = {snake_to_camel(field) for field in known_fields}


class BoletoLog(Base):
    def __init__(self, id, created, event, errors, boleto):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.event = event
        self.errors = errors
        self.boleto = boleto_from_json(boleto)


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

    return [from_json(boleto) for boleto in response["logs"]], []


def retrieve(id, user=None):
    response, errors = request.get(
        user=check_user(user),
        endpoint="boleto/log/{id}".format(id=id),
    )

    if errors:
        return None, errors

    return from_json(response["log"]), []


def from_json(json):
    return BoletoLog(**{
        camel_to_snake(k): v for k, v in json.items() if k in known_camel_fields
    })
