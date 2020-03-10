from starkbank.utils import rest
from starkbank.utils.base import Base
from starkbank.utils.checks import check_datetime


class Transfer(Base):

    def __init__(self, amount, name, tax_id, bank_code, branch_code, account_number, fee=None, tags=None, status=None, id=None, created=None):
        Base.__init__(self, id=id)

        self.tax_id = tax_id
        self.amount = amount
        self.fee = fee
        self.name = name
        self.bank_code = bank_code
        self.branch_code = branch_code
        self.account_number = account_number
        self.tags = tags
        self.status = status
        self.created = check_datetime(created)


Transfer._define_known_fields()


def create(transfers, user=None):
    return rest.post(resource=Transfer, entities=transfers, user=user)


def get(id, user=None):
    return rest.get_id(resource=Transfer, id=id, user=user)


def get_pdf(id, user=None):
    return rest.get_pdf(resource=Transfer, id=id, user=user)


def query(limit=100, request_id=None, transaction_ids=None, tags=None, after=None, before=None, status=None, sort=None, user=None):
    return rest.query(resource=Transfer, limit=limit, user=user, status=status, tags=tags, after=after, before=before, request_id=request_id, transaction_ids=transaction_ids, sort=sort)


def delete(ids, user=None):
    return rest.delete(resource=Transfer, ids=ids, user=user)
