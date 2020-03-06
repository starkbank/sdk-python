from starkbank.utils.base import Base
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_datetime


class BoletoMessage(Base):

    _known_fields = {
        "status",
        "amount",
        "name",
        "tax_id",
        "street_line_1",
        "street_line_2",
        "district",
        "city",
        "state_code",
        "zip_code",
        "workspace_id",
        "created",
        "interest",
        "fine",
        "due_date",
        "overdue_limit",
        "id",
    }
    _known_camel_fields = {snake_to_camel(field) for field in _known_fields}

    def __init__(self, status, amount, name, tax_id, street_line_1, street_line_2, district, city, state_code, zip_code, workspace_id, created, interest, fine, due_date, overdue_limit, id):
        Base.__init__(self, id=id)

        self.status = status
        self.amount = amount
        self.name = name
        self.tax_id = tax_id
        self.street_line_1 = street_line_1
        self.street_line_2 = street_line_2
        self.district = district
        self.city = city
        self.state_code = state_code
        self.zip_code = zip_code
        self.workspace_id = workspace_id
        self.created = check_datetime(created)
        self.interest = interest
        self.fine = fine
        self.due_date = check_datetime(due_date)
        self.overdue_limit = overdue_limit
