from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_date, check_datetime


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
    - fine [float, default 2.0]: Boleto fine for overdue payment in %. ex: 2.5
    - interest [float, default 1.0]: Boleto monthly interest for overdue payment in %. ex: 5.2
    - overdue_limit [integer, default 59]: limit in days for payment after due date. ex: 7 (max: 59)
    - descriptions [list of dictionaries, default None]: list of dictionaries with "text":string and (optional) "amount":int pairs
    - discounts [list of dictionaries, default None]: list of dictionaries with "percentage":float and "date":datetime.datetime or string pairs
    - tags [list of strings]: list of strings for tagging
    - receiver_name [string]: receiver (Sacador Avalista) full name. ex: "Anthony Edward Stark"
    - receiver_tax_id [string]: receiver (Sacador Avalista) tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
    ## Attributes (return-only):
    - id [string]: unique id returned when Boleto is created. ex: "5656565656565656"
    - fee [integer]: fee charged when Boleto is paid. ex: 200 (= R$ 2.00)
    - line [string]: generated Boleto line for payment. ex: "34191.09008 63571.277308 71444.640008 5 81960000000062"
    - bar_code [string]: generated Boleto bar-code for payment. ex: "34195819600000000621090063571277307144464000"
    - status [string]: current Boleto status. ex: "registered" or "paid"
    - transaction_ids [list of strings]: ledger transaction ids linked to this boleto. ex: ["19827356981273"]
    - workspace_id [string]: ID of the Workspace where this Boleto was generated. ex: "4545454545454545"
    - our_number [string]: Reference number registered at the settlement bank. ex:"10131474"
    - created [datetime.datetime]: creation datetime for the Boleto. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, amount, name, tax_id, street_line_1, street_line_2, district, city, state_code, zip_code,
                 due=None, fine=None, interest=None, overdue_limit=None, tags=None, descriptions=None, discounts=None,
                 receiver_name=None, receiver_tax_id=None, id=None, fee=None, line=None, bar_code=None, status=None,
                 workspace_id=None, transaction_ids=None, created=None, our_number=None):
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
        self.transaction_ids = transaction_ids
        self.workspace_id = workspace_id
        self.created = check_datetime(created)
        self.our_number = our_number


_resource = {"class": Boleto, "name": "Boleto"}


def create(boletos, user=None):
    """# Create Boletos
    Send a list of Boleto objects for creation in the Stark Bank API
    ## Parameters (required):
    - boletos [list of Boleto objects]: list of Boleto objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
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
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
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
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Boleto pdf file
    """
    return rest.get_content(resource=_resource, id=id, layout=layout, hidden_fields=hidden_fields, user=user, sub_resource_name="pdf")


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
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of Boleto objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        tags=tags,
        ids=ids,
        user=user,
    )


def page(cursor=None, limit=None, status=None, tags=None, ids=None, after=None, before=None, user=None):
    """# Retrieve paged Boletos
    Receive a list of up to 100 Boleto objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "paid" or "registered"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of Boleto objects with updated attributes
    - cursor to retrieve the next page of Boleto objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
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
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - deleted Boleto object
    """
    return rest.delete_id(resource=_resource, id=id, user=user)
