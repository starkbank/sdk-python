from ...utils import rest
from ...utils.checks import check_datetime
from ...utils.resource import Resource


class BoletoPayment(Resource):

    def __init__(self, tax_id, description, tags, line=None, bar_code=None, scheduled=None, id=None, status=None, amount=None, created=None):
        Resource.__init__(self, id=id)

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
    return rest.post(resource=BoletoPayment, entities=payments, user=user)


def get(id, user=None):
    return rest.get_id(resource=BoletoPayment, id=id, user=user)


def pdf(id, user=None):
    return rest.get_pdf(resource=BoletoPayment, id=id, user=user)


def query(limit=None, status=None, tags=None, user=None):
    return rest.get_list(resource=BoletoPayment, limit=limit, user=user, status=status, tags=tags)


def delete(ids, user=None):
    return rest.delete_list(resource=BoletoPayment, ids=ids, user=user)
