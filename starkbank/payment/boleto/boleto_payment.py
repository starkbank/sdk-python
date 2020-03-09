from starkbank.utils.base import Base, Post, GetId, Get, GetPdf, Delete
from starkbank.utils.checks import check_datetime


class BoletoPayment(Post, Get, GetId, GetPdf, Delete):

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

    @classmethod
    def _query(cls, limit=100, status=None, tags=None):
        return super(BoletoPayment, cls)._query(
            limit=limit,
            status=status,
            tags=tags,
        )


BoletoPayment._define_known_fields()


create = BoletoPayment._post
query = BoletoPayment._query
get = BoletoPayment._get_id
get_pdf = BoletoPayment._get_pdf
delete = BoletoPayment._delete
