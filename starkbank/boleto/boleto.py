from starkbank.utils.checks import check_datetime
from starkbank.utils.base import Base
from starkbank.utils import rest


class Boleto(Base):

    def __init__(self, amount, name, tax_id, street_line_1, street_line_2, district, city, state_code, zip_code,
                 due=None, fine=None, interest=None, overdue_limit=None, tags=None, descriptions=None, id=None,
                 fee=None, line=None, bar_code=None, status=None, created=None):
        Base.__init__(self, id=id)

        self.amount = amount
        self.fee = fee
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


Boleto._define_known_fields()


def create(boletos, user=None):
    return rest.post(resource=Boleto, entities=boletos, user=user)


def get(id, user=None):
    return rest.get_id(resource=Boleto, id=id, user=user)


def get_pdf(id, user=None):
    return rest.get_pdf(resource=Boleto, id=id, user=user)


def query(limit=100, status=None, tags=None, ids=None, after=None, before=None, user=None):
    return rest.query(resource=Boleto, limit=limit, user=user, status=status, tags=tags, ids=ids, after=after, before=before)


def delete(ids, user=None):
    return rest.delete(resource=Boleto, ids=ids, user=user)
