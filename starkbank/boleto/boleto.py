from starkbank.utils.checks import check_date, check_datetime
from starkbank.utils.base import Base
from starkbank.utils import rest


class Boleto(Base):
    """Description: Boleto object

    When you initialize a Boleto, the entity will not necessarily be
    sent to the Stark Bank API. The create function sends the object
    to the Stark Bank API and returns the list of validated and created
    objects.

    Parameters (required):
        amount [integer]: boleto value in cents. ex: 1234 (= R$ 12.34)
        name [string]: payer full name. ex: "Anthony Edward Stark"
        tax_id [string]: payer tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
        street_line_1 [string]: payer main address. ex: Av. Paulista, 200
        street_line_2 [string]: payer address complement. ex: Apto. 123
        district [string]: payer address district / neighbourhood. ex: Bela Vista
        city [string]: payer address city. ex: Rio de Janeiro
        state_code [string]: payer address state. ex: RJ
        zip_code [string]: payer address zip code. ex: 01311-200
        due [datetime.date, default today + 2 days]: boleto due date in ISO format. ex: 2020-04-30
        tags [list of strings]: list of strings for tagging (may be empty)
    Parameters (optional):
        fine [float, default 0.0]: optional, boleto fine for overdue payment in %. ex: 2.5
        interest [float, default 0.0]: optional, boleto monthly interest for overdue payment in %. ex: 5.2
        overdue_limit [integer, default 59]: optional, limit in days for automatic boleto cancel after due date. ex: 7 (max: 59)
        descriptions [list of dictionaries, default None]: optional, list of dictionary descriptions with "text":string and (optional) "amount":int pairs
    Attrtibutes (return-only):
        id [string, default None]: unique id returned when Boleto is created. ex: "5656565656565656"
        fee [integer, default None]: fee charged when boleto is paid. ex: 200 (= R$ 2.00)
        line [string, default None]: generated boleto line for payment. ex: "34191.09008 63571.277308 71444.640008 5 81960000000062"
        bar_code [string, default None]: generated boleto bar_code for payment. ex: "34195819600000000621090063571277307144464000"
        status [string, default None]: current boleto status. ex: "registered" or "paid"
        created [datetime.datetime, default None]: creation datetime for the boleto. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

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
        self.due = check_date(due)
        self.fine = fine
        self.interest = interest
        self.overdue_limit = overdue_limit
        self.tags = tags
        self.descriptions = descriptions
        self.line = line
        self.bar_code = bar_code
        self.status = status
        self.created = check_datetime(created)


def create(boletos, user=None):
    return rest.post(resource=Boleto, entities=boletos, user=user)


def get(id, user=None):
    return rest.get_id(resource=Boleto, id=id, user=user)


def get_pdf(id, user=None):
    return rest.get_pdf(resource=Boleto, id=id, user=user)


def query(limit=None, status=None, tags=None, ids=None, after=None, before=None, user=None):
    return rest.query(resource=Boleto, limit=limit, user=user, status=status, tags=tags, ids=ids, after=check_date(after), before=check_date(before))


def delete(ids, user=None):
    return rest.delete(resource=Boleto, ids=ids, user=user)
