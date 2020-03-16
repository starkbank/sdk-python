from ..utils import rest
from ..utils.checks import check_date, check_datetime
from ..utils.resource import Resource


class Boleto(Resource):
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
    Attributes (return-only):
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
        Resource.__init__(self, id=id)

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
    """Create Boletos

    Send a list of Boleto objects for creation in the Stark Bank API

    Parameters (required):
        boletos [list of Boleto objects]: list of Boleto objects to be created in the API
    Parameters (optional):
        user [Project object]: optional Project object. Not necessary if starkbank.user was set before function call
    Return
        list of Boleto objects with updated return-only attributes
    """
    return rest.post(resource=Boleto, entities=boletos, user=user)


def get(id, user=None):
    """Retrieve a single Boleto

    Receive a single Boleto object previously created in the Stark Bank API by passing its id

    Parameters (required):
        id [string]: object unique id. ex: "5656565656565656"
    Parameters (optional):
        user [Project object]: optional Project object. Not necessary if starkbank.user was set before function call
    Return
        Boleto object with updated return-only attributes
    """
    return rest.get_id(resource=Boleto, id=id, user=user)


def pdf(id, user=None):
    """Retrieve a single Boleto pdf file

    Receive a single Boleto pdf file generated in the Stark Bank API by passing its id

    Parameters (required):
        id [string]: object unique id. ex: "5656565656565656"
    Parameters (optional):
        user [Project object]: optional Project object. Not necessary if starkbank.user was set before function call
    Return
        Boleto object pdf file
    """
    return rest.get_pdf(resource=Boleto, id=id, user=user)


def query(limit=None, status=None, tags=None, ids=None, after=None, before=None, user=None):
    """Retrieve Boletos

    Receive a generator of Boleto objects previously created in the Stark Bank API

    Parameters (optional):
        limit [integer, default None]: optional number of objects to be retrieved. Unlimited if None. ex: 35
        status [string, default None]: optional filter for status of objects retrieved. ex: "paid" or "registered"
        tags [list of strings, default None]: optional tags to filter retrieved objects. ex: ["tony", "stark"]
        ids [list of strings, default None]: optional list of ids to filter selected objects. ex: ["5656565656565656", "4545454545454545"]
        after [datetime.date, default None] optional date filter for objects only after specified date. ex: datetime.date(2020, 3, 10)
        before [datetime.date, default None] optional date filter for objects only before specified date. ex: datetime.date(2020, 3, 10)
        user [Project object, default None]: optional Project object. Not necessary if starkbank.user was set before function call
    Return
        generator of Boleto objects with updated return-only attributes
    """
    return rest.get_list(resource=Boleto, limit=limit, user=user, status=status, tags=tags, ids=ids,
                         after=check_date(after), before=check_date(before))


def delete(ids, user=None):
    """Delete list of Boleto entities

    Delete list of Boleto entities previously created in the Stark Bank API

    Parameters (required):
        ids [list of strings]: list of object unique ids. ex: ["5656565656565656", "4545454545454545"]
    Parameters (optional):
        user [Project object]: optional Project object. Not necessary if starkbank.user was set before function call
    Return
        list of deleted Boleto objects with updated return-only attributes
    """
    return rest.delete_list(resource=Boleto, ids=ids, user=user)
