from starkbank.utils import rest
from starkbank.utils.checks import check_datetime
from starkbank.utils.base import Base


class BoletoPayment(Base):

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


def create(boleto_payments, user=None):
    return rest.post(resource=BoletoPayment, entities=boleto_payments, user=user)


def get(id, user=None):
    return rest.get_id(resource=BoletoPayment, id=id, user=user)


def get_pdf(id, user=None):
    return rest.get_pdf(resource=BoletoPayment, id=id, user=user)


def query(limit=None, status=None, tags=None, user=None):
    return rest.query(resource=BoletoPayment, limit=limit, user=user, status=status, tags=tags)


def delete(ids, user=None):
    return rest.delete(resource=BoletoPayment, ids=ids, user=user)
