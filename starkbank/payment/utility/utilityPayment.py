from ...utils import rest
from ...utils.checks import check_datetime, check_date
from ...utils.resource import Resource


class UtilityPayment(Resource):
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
        due [datetime.date]: boleto due date in ISO format. ex: 2020-04-30
    Parameters (optional):
        scheduled [datetime.date, default today]: payment scheduled date. ex: datetime.date(2020, 3, 10)
    Attributes (return-only):
        id [string, default None]: unique id returned when payment is created. ex: "5656565656565656"
        status [string, default None]: current payment status. ex: "registered" or "paid"
        created [datetime.datetime, default None]: creation datetime for the payment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, line, bar_code, tags, description, due, scheduled, id=None, amount=None, status=None, created=None):
        Resource.__init__(self, id=id)

        self.line = line
        self.bar_code = bar_code
        self.due = check_datetime(due)
        self.description = description
        self.tags = tags
        self.scheduled = check_datetime(scheduled)
        self.status = status
        self.amount = amount
        self.created = check_datetime(created)


def create(payments, user=None):
    return rest.post(resource=UtilityPayment, entities=payments, user=user)


def get(id, user=None):
    return rest.get_id(resource=UtilityPayment, id=id, user=user)


def pdf(id, user=None):
    return rest.get_pdf(resource=UtilityPayment, id=id, user=user)


def query(limit=None, status=None, after=None, before=None, tags=None, ids=None, user=None):
    return rest.get_list(resource=UtilityPayment, limit=limit, user=user, status=status, tags=tags, after=check_date(after), before=check_date(before), ids=ids)


def delete(ids, user=None):
    return rest.delete_list(resource=UtilityPayment, ids=ids, user=user)
