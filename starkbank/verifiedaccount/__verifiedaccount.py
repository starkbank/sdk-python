from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date


class VerifiedAccount(Resource):
    """# VerifiedAccount object
    When you initialize a VerifiedAccount, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    ## Parameters (required):
    - tax_id [string]: receiver tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
    ## Parameters (conditionally required):
    - bank_code [string]: code of the receiver bank institution in Brazil. If an ISPB (8 digits) is informed, a Pix transfer will be created, else a TED will be issued. The bank_code parameter is required if verifying with bank details. ex: "20018183" or "341"
    - branch_code [string]: receiver bank account branch. Use '-' in case there is a verifier digit. ex: "1357-9". The branch_code parameter is required if verifying with bank details.
    - key_id [string]: pix key identifier. ex: "tony@starkbank.com", "012.345.678-90". The key_id parameter is required if verifying with Pix key.
    - name [string]: receiver full name. ex: "Anthony Edward Stark". The name parameter is required if verifying with bank details.
    - number [string]: receiver bank account number. Use '-' before the verifier digit. ex: "876543-2". The number parameter is required if verifying with bank details.
    - type [string]: verified account type. ex: "checking", "savings", "salary" or "payment". The type parameter is required if verifying with bank details.
    ## Parameters (optional):
    - tags [list of strings, default []]: list of strings for reference when searching for verified accounts. ex: ["employees", "monthly"]
    ## Attributes (return-only):
    - id [string]: unique id returned when the VerifiedAccount is created. ex: "5656565656565656"
    - bank_name [string]: bank name associated with the verified account. ex: "Stark Bank"
    - status [string]: current verified account status. ex: "creating", "created", "processing", "active", "failed" or "canceled"
    - created [datetime.datetime]: creation datetime for the verified account. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the verified account. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, tax_id, bank_code=None, branch_code=None, key_id=None, name=None,
                 number=None, type=None, tags=None, id=None, bank_name=None, status=None,
                 created=None, updated=None):
        Resource.__init__(self, id=id)

        self.tax_id = tax_id
        self.bank_code = bank_code
        self.branch_code = branch_code
        self.key_id = key_id
        self.name = name
        self.number = number
        self.type = type
        self.tags = tags
        self.bank_name = bank_name
        self.status = status
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": VerifiedAccount, "name": "VerifiedAccount"}


def create(verified_accounts, user=None):
    """# Create VerifiedAccounts
    Send a list of VerifiedAccount objects for creation in the Stark Bank API
    ## Parameters (required):
    - verified_accounts [list of VerifiedAccount objects]: list of VerifiedAccount objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of VerifiedAccount objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=verified_accounts, user=user)


def get(id, user=None):
    """# Retrieve a specific VerifiedAccount
    Receive a single VerifiedAccount object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - VerifiedAccount object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def cancel(id, user=None):
    """# Cancel a VerifiedAccount entity
    Cancel a VerifiedAccount entity previously created in the Stark Bank API
    ## Parameters (required):
    - id [string]: VerifiedAccount unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - canceled VerifiedAccount object
    """
    return rest.delete_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, status=None, ids=None, tags=None, user=None):
    """# Retrieve VerifiedAccounts
    Receive a generator of VerifiedAccount objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created or updated only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created or updated only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "creating", "created", "processing", "active", "failed" or "canceled"
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of VerifiedAccount objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        ids=ids,
        tags=tags,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, status=None, ids=None, tags=None, user=None):
    """# Retrieve paged VerifiedAccounts
    Receive a list of up to 100 VerifiedAccount objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None]: date filter for objects created or updated only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created or updated only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "creating", "created", "processing", "active", "failed" or "canceled"
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of VerifiedAccount objects with updated attributes
    - cursor to retrieve the next page of VerifiedAccount objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        ids=ids,
        tags=tags,
        user=user,
    )
