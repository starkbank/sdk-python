from starkbank.utils.base import Base, Post, BaseDelete, Get, GetId, GetPdf
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_datetime


class Boleto(Post, Get, GetId, GetPdf, BaseDelete):
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

    def __init__(self, amount, name, tax_id, street_line_1, street_line_2, district, city, state_code, zip_code,
                 due=None, fine=None, interest=None, overdue_limit=None, tags=None, descriptions=None, id=None,
                 line=None, bar_code=None, status=None, created=None):
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


create = Boleto._create
list = Boleto._list
get = Boleto._get
get_pdf = Boleto.get_pdf
delete = Boleto.delete
