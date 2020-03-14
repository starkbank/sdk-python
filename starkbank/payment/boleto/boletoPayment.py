from ...utils import rest
from ...utils.checks import check_datetime
from ...utils.resource import Resource


class BoletoPayment(Resource):
    """Description: BoletoPayment object

    When you initialize a BoletoPayment, the entity will not necessarily be
    created in the Stark Bank API. The create function sends the object
    to the Stark Bank API and returns the list of validated and created
    objects.

    Parameters (conditionally required):
        line [string, default None]: Number sequence that describes the payment. Either 'line' or 'bar_code' parameters are required. If both are sent, they must match. ex: "34191.09008 63571.277308 71444.640008 5 81960000000062"
        bar_code [string, default None]: Bar code number that describes the payment. Either 'line' or 'barCode' parameters are required. If both are sent, they must match. ex: "34195819600000000621090063571277307144464000"
    Parameters (required):
        tax_id [string]: receiver tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
        description [string]: Text to be displayed in your statement (min. 10 characters). ex: "payment ABC"
        tags [list of strings]: list of strings for tagging (may be empty)
    Parameters (optional):
        scheduled [datetime.date, default today]: payment scheduled date. ex: datetime.date(2020, 3, 10)
    Attributes (return-only):
        id [string, default None]: unique id returned when payment is created. ex: "5656565656565656"
        status [string, default None]: current payment status. ex: "registered" or "paid"
        amount [int, default None]: amount automatically calculated from line or bar_code. ex: 23456 (= R$ 234.56)
        created [datetime.datetime, default None]: creation datetime for the payment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, tax_id, description, tags, line=None, bar_code=None, scheduled=None, id=None, status=None, amount=None, created=None):
        Resource.__init__(self, id=id)

        self.line = line
        self.tax_id = tax_id
        self.bar_code = bar_code
        self.description = description
        self.tags = tags
        self.scheduled = scheduled
        self.status = status
        self.amount = amount
        self.created = check_datetime(created)


def create(payments, user=None):
    return rest.post(resource=BoletoPayment, entities=payments, user=user)


def get(id, user=None):
    return rest.get_id(resource=BoletoPayment, id=id, user=user)


def pdf(id, user=None):
    return rest.get_pdf(resource=BoletoPayment, id=id, user=user)


def query(limit=None, status=None, tags=None, user=None):
    return rest.get_list(resource=BoletoPayment, limit=limit, user=user, status=status, tags=tags)


def delete(ids, user=None):
    return rest.delete_list(resource=BoletoPayment, ids=ids, user=user)
