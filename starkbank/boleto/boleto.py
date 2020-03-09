from starkbank.utils.base import Base, Post, Delete, Get, GetId, GetPdf
from starkbank.utils.checks import check_datetime


class Boleto(Post, Get, GetId, GetPdf, Delete):

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

    @classmethod
    def _query(cls, limit=100, status=None, tags=None, ids=None, after=None, before=None, user=None):
        return super(Boleto, cls)._query(
            limit=limit,
            status=status,
            tags=tags,
            ids=ids,
            after=after,
            before=before,
            user=user,
        )


Boleto._define_known_fields()


create = Boleto._post
get = Boleto._get_id
get_pdf = Boleto._get_pdf
delete = Boleto._delete
query = Boleto._query
