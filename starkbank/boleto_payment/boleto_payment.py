from starkbank import request
from starkbank.utils.base import Base
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_user, check_datetime


class BoletoPayment(Base):

    _known_fields = {
        "id",
        "line",
        "barCode",
        "taxId",
        "description",
        "tags",
        "scheduled",
        "status",
        "amount",
        "created",
    }
    _known_camel_fields = {snake_to_camel(field) for field in _known_fields}

    def __init__(self, tax_id, description, tags, line=None, bar_code=None, scheduled=None, id=None, status=None, amount=None, created=None):
        Base.__init__(self, id=id)

        self.line = line
        self.bar_code = bar_code
        self.tax_id = tax_id
        self.description = description
        self.tags = tags
        self.scheduled = scheduled
        self.status = status
        self.amount = amount
        self.created = check_datetime(created)


def create(payments, user=None):
    response = request.post(
        user=check_user(user),
        endpoint="boleto-payment",
        body={
            "payments": [
                {snake_to_camel(k): v for k, v in payment.json().items() if v is not None} for payment in payments
            ]
        }
    )

    return [
        BoletoPayment.from_json(payment) for payment in response["payments"]
    ]


def retrieve(id, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="boleto-payment/{id}".format(id=id),
    )

    return BoletoPayment.from_json(response["payment"])


def retrieve_pdf(id, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="boleto-payment/{id}/pdf".format(id=id),
        json_response=False,
    )

    return response


def list(limit=100, cursor=None, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="boleto-payment/",
        url_params={
            "limit": limit,
            "cursor": cursor,
        },
    )

    return [BoletoPayment.from_json(payment) for payment in response["payments"]], response["cursor"]


def delete(id, user=None):
    response = request.delete(
        user=check_user(user),
        endpoint="boleto-payment/{id}".format(id=id),
    )

    return BoletoPayment.from_json(response["payments"])

