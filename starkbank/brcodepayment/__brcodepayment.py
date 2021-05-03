from ..utils import rest
from ..utils.checks import check_datetime, check_date
from ..utils.resource import Resource


class BrcodePayment(Resource):

    """# BrcodePayment object
    When you initialize a BrcodePayment, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    ## Parameters (required):
    - brcode [string]: String loaded directly from the QR Code or copied from the invoice. ex: "00020126580014br.gov.bcb.pix0136a629532e-7693-4846-852d-1bbff817b5a8520400005303986540510.005802BR5908T'Challa6009Sao Paulo62090505123456304B14A"
    - tax_id [string]: receiver tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
    - description [string]: Text to be displayed in your statement (min. 10 characters). ex: "payment ABC"
    ## Parameters (conditionally required):
    - amount [int, default None]: If the BRCode does not provide an amount, this parameter is mandatory, else it is optional. ex: 23456 (= R$ 234.56)
    ## Parameters (optional):
    - scheduled [datetime.date, datetime.datetime or string, default now]: payment scheduled date or datetime. ex: datetime.datetime(2020, 3, 10, 15, 17, 3)
    - tags [list of strings, default None]: list of strings for tagging
    ## Attributes (return-only):
    - id [string, default None]: unique id returned when payment is created. ex: "5656565656565656"
    - name [string]: receiver name. ex: "Jon Snow"
    - status [string, default None]: current payment status. ex: "success" or "failed"
    - type [string, default None]: brcode type. ex: "static" or "dynamic"
    - transaction_ids [list of strings, default None]: ledger transaction ids linked to this payment. ex: ["19827356981273"]
    - fee [integer, default None]: fee charged by this brcode payment. ex: 50 (= R$ 0.50)
    - updated [datetime.datetime, default None]: latest update datetime for the payment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime, default None]: creation datetime for the payment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, brcode, tax_id, description, amount=None, scheduled=None, tags=None, id=None, name=None,
                 status=None, type=None, transaction_ids=None, fee=None, updated=None, created=None):
        Resource.__init__(self, id=id)

        self.brcode = brcode
        self.tax_id = tax_id
        self.description = description
        self.tags = tags
        self.scheduled = check_date(scheduled)
        self.name = name
        self.status = status
        self.type = type
        self.amount = amount
        self.transaction_ids = transaction_ids
        self.fee = fee
        self.updated = check_datetime(updated)
        self.created = check_datetime(created)


_resource = {"class": BrcodePayment, "name": "BrcodePayment"}


def create(payments, user=None):
    """# Create BrcodePayments
    Send a list of BrcodePayment objects for creation in the Stark Bank API
    ## Parameters (required):
    - payments [list of BrcodePayment objects]: list of BrcodePayment objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of BrcodePayment objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=payments, user=user)


def get(id, user=None):
    """# Retrieve a specific BrcodePayment
    Receive a single BrcodePayment object previously created by the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - BrcodePayment object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def pdf(id, user=None):
    """# Retrieve a specific BrcodePayment pdf file
    Receive a single BrcodePayment pdf receipt file generated in the Stark Bank API by its id.
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - BrcodePayment pdf file
    """
    return rest.get_content(resource=_resource, id=id, user=user, sub_resource_name="pdf")


def query(limit=None, after=None, before=None, tags=None, ids=None, status=None, user=None):
    """# Retrieve BrcodePayments
    Receive a generator of BrcodePayment objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - status [string, default None]: filter for status of retrieved objects. ex: "success"
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of BrcodePayment objects with updated attributes
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


def page(cursor=None, after=None, before=None, tags=None, ids=None, status=None, limit=None, user=None):
    """# Retrieve paged BrcodePayments
    Receive a list of up to 100 BrcodePayment objects previously created in the Stark Bank API and the cursor to the next page.
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
    - list of BrcodePayment objects with updated attributes
    - cursor to retrieve the next page of BrcodePayment objects
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


def update(id, status=None, user=None):
    """# Update BrcodePayment entity
    Update a BrcodePayment by passing its Id, if it hasn't been paid yet.
    ## Parameters (required):
    - id [string]: BrcodePayment id. ex: '5656565656565656'
    ## Parameters (required):
    - status [string]: You may cancel the payment by passing 'canceled' in the status
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - target BrcodePayment with updated attributes
    """
    return rest.patch_id(resource=_resource, id=id, user=user, status=status)
