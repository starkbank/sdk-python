from starkbank import request
from starkbank.utils.base import Base, Post, GetId, Get, GetPdf, BaseDelete
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_user, check_datetime


class BoletoPayment(Post, Get, GetId, GetPdf, BaseDelete):

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


create = BoletoPayment._create
list = BoletoPayment._list
get = BoletoPayment._get
get_pdf = BoletoPayment.get_pdf
delete = BoletoPayment.delete
