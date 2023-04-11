from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date
from ..utils import rest


class CorporateWithdrawal(Resource):
    """# CorporateWithdrawal object
    The CorporateWithdrawal objects created in your Workspace return cash from your Corporate balance to your
    Banking balance.
    ## Parameters (required):
    - amount [integer]: CorporateWithdrawal value in cents. Minimum = 0 (any value will be accepted). ex: 1234 (= R$ 12.34)
    - external_id [string] CorporateWithdrawal external ID. ex: "12345"
    ## Parameters (optional):
    - tags [list of strings, default []]: list of strings for tagging. ex: ["tony", "stark"]
    ## Attributes (return-only):
    - id [string]: unique id returned when CorporateWithdrawal is created. ex: "5656565656565656"
    - transaction_id [string]: Stark Bank ledger transaction ids linked to this CorporateWithdrawal
    - corporate_transaction_id [string]: corporate ledger transaction ids linked to this CorporateWithdrawal
    - updated [datetime.datetime]: latest update datetime for the CorporateWithdrawal. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime]: creation datetime for the CorporateWithdrawal. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, amount, external_id, tags=None, id=None, transaction_id=None,
                 corporate_transaction_id=None, updated=None, created=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.external_id = external_id
        self.tags = tags
        self.transaction_id = transaction_id
        self.corporate_transaction_id = corporate_transaction_id
        self.updated = check_datetime(updated)
        self.created = check_datetime(created)


_resource = {"class": CorporateWithdrawal, "name": "CorporateWithdrawal"}


def create(withdrawal, user=None):
    """# Create a CorporateWithdrawal
    Send a single CorporateWithdrawal object for creation at the Stark Bank API
    ## Parameters (required):
    - withdrawal [CorporateWithdrawal object]: CorporateWithdrawal object to be created in the API.
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - CorporateWithdrawal object with updated attributes
    """
    return rest.post_single(resource=_resource, entity=withdrawal, user=user)


def get(id, user=None):
    """# Retrieve a specific CorporateWithdrawal
    Receive a single CorporateWithdrawal object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - CorporateWithdrawal object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(external_ids=None, after=None, before=None, limit=None, tags=None, user=None):
    """# Retrieve CorporateWithdrawals
    Receive a generator of CorporateWithdrawal objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - external_ids [list of strings, default None]: external IDs. ex: ["5656565656565656", "4545454545454545"]
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - generator of CorporateWithdrawal objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        external_ids=external_ids,
        after=check_date(after),
        before=check_date(before),
        tags=tags,
        limit=limit,
        user=user,
    )


def page(external_ids=None, after=None, before=None, limit=None, tags=None, cursor=None, user=None):
    """# Retrieve paged CorporateWithdrawals
    Receive a list of up to 100 CorporateWithdrawal objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. Max = 100. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - external_ids [list of strings, default None]: external IDs. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - list of CorporateWithdrawal objects with updated attributes
    - cursor to retrieve the next page of CorporateWithdrawal objects
    """
    return rest.get_page(
        resource=_resource,
        external_ids=external_ids,
        after=check_date(after),
        before=check_date(before),
        tags=tags,
        limit=limit,
        cursor=cursor,
        user=user,
    )
