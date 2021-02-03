from ..utils import rest
from ..utils.checks import check_datetime, check_date
from ..utils.resource import Resource


class BoletoPayment(Resource):
    """# BoletoPayment object
    When you initialize a BoletoPayment, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    ## Parameters (conditionally required):
    - line [string, default None]: Number sequence that describes the payment. Either 'line' or 'bar_code' parameters are required. If both are sent, they must match. ex: "34191.09008 63571.277308 71444.640008 5 81960000000062"
    - bar_code [string, default None]: Bar code number that describes the payment. Either 'line' or 'barCode' parameters are required. If both are sent, they must match. ex: "34195819600000000621090063571277307144464000"
    ## Parameters (required):
    - tax_id [string]: receiver tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
    - description [string]: Text to be displayed in your statement (min. 10 characters). ex: "payment ABC"
    ## Parameters (optional):
    - scheduled [datetime.date or string, default today]: payment scheduled date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings]: list of strings for tagging
    ## Attributes (return-only):
    - id [string, default None]: unique id returned when payment is created. ex: "5656565656565656"
    - status [string, default None]: current payment status. ex: "success" or "failed"
    - amount [int, default None]: amount automatically calculated from line or bar_code. ex: 23456 (= R$ 234.56)
    - fee [integer, default None]: fee charged when the boleto payment is created. ex: 200 (= R$ 2.00)
    - created [datetime.datetime, default None]: creation datetime for the payment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, tax_id, description, line=None, bar_code=None, scheduled=None, tags=None, id=None, status=None, amount=None, fee=None, created=None):
        Resource.__init__(self, id=id)

        self.line = line
        self.tax_id = tax_id
        self.bar_code = bar_code
        self.description = description
        self.tags = tags
        self.scheduled = check_date(scheduled)
        self.status = status
        self.amount = amount
        self.fee = fee
        self.created = check_datetime(created)


_resource = {"class": BoletoPayment, "name": "BoletoPayment"}


def create(payments, user=None):
    """# Create BoletoPayments
    Send a list of BoletoPayment objects for creation in the Stark Bank API
    ## Parameters (required):
    - payments [list of BoletoPayment objects]: list of BoletoPayment objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of BoletoPayment objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=payments, user=user)


def get(id, user=None):
    """# Retrieve a specific BoletoPayment
    Receive a single BoletoPayment object previously created by the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - BoletoPayment object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def pdf(id, user=None):
    """# Retrieve a specific BoletoPayment pdf file
    Receive a single BoletoPayment pdf file generated in the Stark Bank API by its id.
    Only valid for boleto payments with "success" status.
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - BoletoPayment pdf file
    """
    return rest.get_content(resource=_resource, id=id, user=user, sub_resource_name="pdf")


def query(limit=None, after=None, before=None, tags=None, ids=None, status=None, user=None):
    """# Retrieve BoletoPayments
    Receive a generator of BoletoPayment objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - status [string, default None]: filter for status of retrieved objects. ex: "success"
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of BoletoPayment objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        tags=tags,
        ids=ids,
        status=status,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, tags=None, ids=None, status=None, user=None):
    """# Retrieve paged BoletoPayments
    Receive a list of up to 100 BoletoPayment objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - status [string, default None]: filter for status of retrieved objects. ex: "success"
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of BoletoPayment objects with updated attributes
    - cursor to retrieve the next page of BoletoPayment objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        tags=tags,
        ids=ids,
        status=status,
        user=user,
    )


def delete(id, user=None):
    """# Delete a BoletoPayment entity
    Delete a BoletoPayment entity previously created in the Stark Bank API
    ## Parameters (required):
    - id [string]: BoletoPayment unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - deleted BoletoPayment object
    """
    return rest.delete_id(resource=_resource, id=id, user=user)
