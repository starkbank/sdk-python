from starkbank import request
from starkbank.utils.base import Base
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_user, check_datetime


class Boleto(Base):

    _known_fields = {
        "id",
        "amount",
        "name",
        "tax_id",
        "street_line_1",
        "street_line_2",
        "district",
        "city",
        "state_code",
        "zip_code",
        "due",
        "fine",
        "interest",
        "overdue_limit",
        "tags",
        "descriptions",
        "line",
        "bar_code",
        "status",
        "created",
    }
    _known_camel_fields = {snake_to_camel(field) for field in _known_fields}

    def __init__(self, amount, name, tax_id, street_line_1, street_line_2, district, city, state_code, zip_code, due=None, fine=None, interest=None, overdue_limit=None, tags=None, descriptions=None, id=None, line=None, bar_code=None, status=None, created=None):
        Base.__init__(self, id=id)

        self.amount = amount
        self.name = name
        self.tax_id = tax_id
        self.street_line_1 = street_line_1
        self.street_line_2 = street_line_2
        self.district = district
        self.city = city
        self.state_code = state_code
        self.zip_code = zip_code
        self.due = due
        self.fine = fine
        self.interest = interest
        self.overdue_limit = overdue_limit
        self.tags = tags
        self.descriptions = descriptions
        self.line = line
        self.bar_code = bar_code
        self.status = status
        self.created = check_datetime(created)


def create(boletos, user=None):
    response = request.post(
        user=check_user(user),
        endpoint="boleto",
        body={
            "boletos": [
                {snake_to_camel(k): v for k, v in boleto.json().items() if v is not None} for boleto in boletos
            ]
        }
    )

    return [
        Boleto.from_json(boleto) for boleto in response["boletos"]
    ]


def retrieve(id, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="boleto/{id}".format(id=id),
    )

    return Boleto.from_json(response["boleto"])


def retrieve_pdf(id, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="boleto/{id}/pdf".format(id=id),
        json_response=False,
    )

    return response


def list(limit=100, cursor=None, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="boleto/",
        url_params={
            "limit": limit,
            "cursor": cursor,
        },
    )

    return [Boleto.from_json(boleto) for boleto in response["boletos"]], response["cursor"]


def delete(ids, user=None):
    if len(ids) > 100:
        raise ValueError("ids cannot have more than 100 elements")

    boletos = []
    for id in ids:
        response = request.delete(
            user=check_user(user),
            endpoint="boleto/{id}".format(id=id),
        )

        boletos.append(Boleto.from_json(response["boleto"]))

    return boletos
