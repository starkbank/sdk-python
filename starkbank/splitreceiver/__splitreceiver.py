from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date


class SplitReceiver(Resource):
    """# SplitReceiver object
    When you initialize a SplitReceiver, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    ## Parameters (required):
    - name [string]: receiver full name. ex: "Anthony Edward Stark"
    - tax_id [string]: receiver account tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
    - bank_code [string]: code of the receiver bank institution in Brazil. If an ISPB (8 digits) is informed, a PIX splitReceiver will be created, else a TED will be issued. ex: "20018183" or "341"
    - branch_code [string]: receiver bank account branch. Use '-' in case there is a verifier digit. ex: "1357-9"
    - account_number [string]: receiver bank account number. Use '-' before the verifier digit. ex: "876543-2"
    - account_type [string]: Receiver bank account type. This parameter only has effect on Pix SplitReceivers. ex: "checking", "savings", "salary" or "payment"
    ## Parameters (optional):
    - tags [list of strings, default []]: list of strings for reference when searching for receivers. ex: ["seller/123456"]
    ## Attributes (return-only):
    - id [string]: unique id returned when the splitReceiver is created. ex: "5656565656565656"
    - status [string]: current splitReceiver status. ex: "success" or "failed"
    - created [datetime.datetime]: creation datetime for the splitReceiver. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the splitReceiver. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, name, tax_id, bank_code, branch_code, account_number, account_type,
                 tags=None, id=None, status=None, created=None, updated=None):
        Resource.__init__(self, id=id)

        self.name = name
        self.tax_id = tax_id
        self.bank_code = bank_code
        self.branch_code = branch_code
        self.account_number = account_number
        self.account_type = account_type
        self.tags = tags
        self.status = status
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": SplitReceiver, "name": "SplitReceiver"}


def create(splitReceivers, user=None):
    """# Create SplitReceivers
    Send a list of SplitReceiver objects for creation in the Stark Bank API
    ## Parameters (required):
    - splitReceivers [list of SplitReceiver objects]: list of SplitReceiver objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of SplitReceiver objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=splitReceivers, user=user)


def get(id, user=None):
    """# Retrieve a specific SplitReceiver
    Receive a single SplitReceiver object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - SplitReceiver object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, transaction_ids=None, status=None, tax_id=None, sort=None, tags=None, ids=None, user=None):
    """# Retrieve SplitReceivers
    Receive a generator of SplitReceiver objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created or updated only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created or updated only before specified date. ex: datetime.date(2020, 3, 10)
    - transaction_ids [list of strings, default None]: list of transaction IDs linked to the desired splitReceivers. ex: ["5656565656565656", "4545454545454545"]
    - status [string, default None]: filter for status of retrieved objects. ex: "success" or "failed"
    - tax_id [string, default None]: filter for splitReceivers sent to the specified tax ID. ex: "012.345.678-90"
    - sort [string, default "-created"]: sort order considered in response. Valid options are "created", "-created", "updated" or "-updated".
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of SplitReceiver objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        transaction_ids=transaction_ids,
        status=status,
        tax_id=tax_id,
        sort=sort,
        tags=tags,
        ids=ids,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, status=None, sort=None, tags=None, ids=None, user=None):
    """# Retrieve paged SplitReceivers
    Receive a list of up to 100 SplitReceiver objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None]: date filter for objects created or updated only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created or updated only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "success" or "failed"
    - sort [string, default "-created"]: sort order considered in response. Valid options are "created", "-created", "updated" or "-updated".
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of SplitReceiver objects with updated attributes
    - cursor to retrieve the next page of SplitReceiver objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        sort=sort,
        tags=tags,
        ids=ids,
        user=user,
    )
