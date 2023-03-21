from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date


class TaxPayment(Resource):
    """# TaxPayment object
    When you initialize a TaxPayment, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    ## Parameters (conditionally required):
    - line [string, default None]: Number sequence that describes the payment. Either 'line' or 'bar_code' parameters are required. If both are sent, they must match. ex: "85800000003 0 28960328203 1 56072020190 5 22109674804 0"
    - bar_code [string, default None]: Bar code number that describes the payment. Either 'line' or 'barCode' parameters are required. If both are sent, they must match. ex: "83660000001084301380074119002551100010601813"
    ## Parameters (required):
    - description [string]: Text to be displayed in your statement (min. 10 characters). ex: "payment ABC"
    ## Parameters (optional):
    - scheduled [datetime.date or string, default today]: payment scheduled date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings]: list of strings for tagging
    ## Attributes (return-only):
    - id [string]: unique id returned when payment is created. ex: "5656565656565656"
    - type [string]: tax type. ex: "das"
    - status [string]: current payment status. ex: "success" or "failed"
    - amount [int]: amount automatically calculated from line or bar_code. ex: 23456 (= R$ 234.56)
    - fee [integer]: fee charged when tax payment is created. ex: 200 (= R$ 2.00)
    - transaction_ids [list of strings]: ledger transaction ids linked to this TaxPayment. ex: ["19827356981273"]
    - updated [datetime.datetime]: latest update datetime for the payment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime]: creation datetime for the payment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, description, line=None, bar_code=None, tags=None, scheduled=None, id=None, type=None, amount=None,
                 fee=None, status=None, transaction_ids=None, updated=None, created=None):
        Resource.__init__(self, id=id)

        self.line = line
        self.bar_code = bar_code
        self.description = description
        self.tags = tags
        self.scheduled = check_date(scheduled)
        self.status = status
        self.amount = amount
        self.fee = fee
        self.type = type
        self.transaction_ids = transaction_ids
        self.updated = check_datetime(updated)
        self.created = check_datetime(created)


_resource = {"class": TaxPayment, "name": "TaxPayment"}


def create(payments, user=None):
    """# Create TaxPayments
    Send a list of TaxPayment objects for creation in the Stark Bank API
    ## Parameters (required):
    - payments [list of TaxPayment objects]: list of TaxPayment objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of TaxPayment objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=payments, user=user)


def get(id, user=None):
    """# Retrieve a specific TaxPayment
    Receive a single TaxPayment object previously created by the Stark Bank API by passing its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - TaxPayment object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def pdf(id, user=None):
    """# Retrieve a specific TaxPayment pdf file
    Receive a single TaxPayment pdf file generated in the Stark Bank API by passing its id.
    Only valid for tax payments with "success" status.
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - TaxPayment pdf file
    """
    return rest.get_content(resource=_resource, id=id, user=user, sub_resource_name="pdf")


def query(limit=None, after=None, before=None, tags=None, ids=None, status=None, user=None):
    """# Retrieve TaxPayments
    Receive a generator of TaxPayment objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - status [string, default None]: filter for status of retrieved objects. ex: "success"
    - user [Project object, default None]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of TaxPayment objects with updated attributes
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
    """# Retrieve paged TaxPayments
    Receive a list of up to 100 TaxPayment objects previously created in the Stark Bank API and the cursor to the next page.
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
    - list of TaxPayment objects with updated attributes
    - cursor to retrieve the next page of TaxPayment objects
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
    """# Delete a TaxPayment entity
    Delete a TaxPayment entity previously created in the Stark Bank API
    ## Parameters (required):
    - id [string]: TaxPayment unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - deleted TaxPayment object
    """
    return rest.delete_id(resource=_resource, id=id, user=user)
