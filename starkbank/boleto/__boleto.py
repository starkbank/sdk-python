from ..utils import rest
from ..utils.checks import check_date, check_datetime
from ..utils.resource import Resource


class Boleto(Resource):
    """# Boleto object
    When you initialize a Boleto, the entity will not be automatically
    sent to the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    ## Parameters (required):
    - amount [integer]: Boleto value in cents. Minimum = 200 (R$2,00). ex: 1234 (= R$ 12.34)
    - name [string]: payer full name. ex: "Anthony Edward Stark"
    - tax_id [string]: payer tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
    - street_line_1 [string]: payer main address. ex: Av. Paulista, 200
    - street_line_2 [string]: payer address complement. ex: Apto. 123
    - district [string]: payer address district / neighbourhood. ex: Bela Vista
    - city [string]: payer address city. ex: Rio de Janeiro
    - state_code [string]: payer address state. ex: GO
    - zip_code [string]: payer address zip code. ex: 01311-200
    ## Parameters (optional):
    - due [datetime.date or string, default today + 2 days]: Boleto due date in ISO format. ex: 2020-04-30
    - fine [float, default 0.0]: Boleto fine for overdue payment in %. ex: 2.5
    - interest [float, default 0.0]: Boleto monthly interest for overdue payment in %. ex: 5.2
    - overdue_limit [integer, default 59]: limit in days for payment after due date. ex: 7 (max: 59)
    - descriptions [list of dictionaries, default None]: list of dictionaries with "text":string and (optional) "amount":int pairs
    - discounts [list of dictionaries, default None]: list of dictionaries with "percentage":float and "date":datetime.datetime or string pairs
    - tags [list of strings]: list of strings for tagging
    - receiver_name [string]: receiver (Sacador Avalista) full name. ex: "Anthony Edward Stark"
    - receiver_tax_id [string]: receiver (Sacador Avalista) tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
    ## Attributes (return-only):
    - id [string, default None]: unique id returned when Boleto is created. ex: "5656565656565656"
    - fee [integer, default None]: fee charged when Boleto is paid. ex: 200 (= R$ 2.00)
    - line [string, default None]: generated Boleto line for payment. ex: "34191.09008 63571.277308 71444.640008 5 81960000000062"
    - bar_code [string, default None]: generated Boleto bar-code for payment. ex: "34195819600000000621090063571277307144464000"
    - status [string, default None]: current Boleto status. ex: "registered" or "paid"
    - created [datetime.datetime, default None]: creation datetime for the Boleto. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - our_number [string, default None]: Reference number registered at the settlement bank. ex:"10131474"
    """

    def __init__(self, amount, name, tax_id, street_line_1, street_line_2, district, city, state_code, zip_code,
                 due=None, fine=None, interest=None, overdue_limit=None, tags=None, descriptions=None, discounts=None,
                 receiver_name=None, receiver_tax_id=None, id=None, fee=None, line=None, bar_code=None, status=None,
                 created=None, our_number=None):
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
        self.receiver_name = receiver_name
        self.receiver_tax_id = receiver_tax_id
        self.due = check_date(due)
        self.fine = fine
        self.interest = interest
        self.overdue_limit = overdue_limit
        self.tags = tags
        self.descriptions = descriptions
        self.discounts = discounts
        self.line = line
        self.bar_code = bar_code
        self.status = status
        self.created = check_datetime(created)
        self.our_number = our_number


_resource = {"class": Boleto, "name": "Boleto"}


def create(boletos, user=None):
    """# Create Boletos
    Send a list of Boleto objects for creation in the Stark Bank API
    ## Parameters (required):
    - boletos [list of Boleto objects]: list of Boleto objects to be created in the API
    ## Parameters (optional):
    - user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of Boleto objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=boletos, user=user)


def get(id, user=None):
    """# Retrieve a specific Boleto
    Receive a single Boleto object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Boleto object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def pdf(id, layout=None, hidden_fields=None, user=None):
    """# Retrieve a specific Boleto pdf file
    Receive a single Boleto pdf file generated in the Stark Bank API by its id.
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - layout [string]: Layout specification. Available options are "default" and "booklet"
    - hidden_fields [list of strings, default None]: List of string fields to be hidden in Boleto pdf. ex: ["customerAddress"]
    - user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Boleto pdf file
    """
    return rest.get_pdf(resource=_resource, id=id, layout=layout, hidden_fields=hidden_fields, user=user)


def query(limit=None, status=None, tags=None, ids=None, after=None, before=None, user=None):
    """# Retrieve Boletos
    Receive a generator of Boleto objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "paid" or "registered"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Project object, default None]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of Boleto objects with updated attributes
    """
    return rest.get_list(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        tags=tags,
        ids=ids,
        user=user,
    )


def delete(id, user=None):
    """# Delete a Boleto entity
    Delete a Boleto entity previously created in the Stark Bank API
    ## Parameters (required):
    - id [string]: Boleto unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - deleted Boleto object
    """
    return rest.delete_id(resource=_resource, id=id, user=user)
