from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_date, check_datetime


class Deposit(Resource):

    """# Deposit object
    Deposits represent passive cash-in received by your account from external transfers
    ## Attributes (return-only):
    - id [string]: unique id associated with a Deposit when it is created. ex: "5656565656565656"
    - name [string]: payer name. ex: "Iron Bank S.A."
    - tax_id [string]: payer tax ID (CPF or CNPJ). ex: "012.345.678-90" or "20.018.183/0001-80"
    - bank_code [string]: payer bank code in Brazil. ex: "20018183" or "341"
    - branch_code [string]: payer bank account branch. ex: "1357-9"
    - account_number [string]: payer bank account number. ex: "876543-2"
    - account_type [string]: payer bank account type. ex: "checking"
    - amount [integer]: Deposit value in cents. ex: 1234 (= R$ 12.34)
    - type [string]: Type of settlement that originated the deposit. ex: "pix" or "ted"
    - status [string]: current Deposit status. ex: "created"
    - tags [list of strings]: list of strings that are tagging the deposit. ex: ["reconciliationId", "txId"]
    - fee [integer]: fee charged by this deposit. ex: 50 (= R$ 0.50)
    - transaction_ids [list of strings]: ledger transaction ids linked to this deposit (if there are more than one, all but the first are reversals or failed reversal chargebacks). ex: ["19827356981273"]
    - created [datetime.datetime]: creation datetime for the Deposit. ex: datetime.datetime(2020, 12, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the Deposit. ex: datetime.datetime(2020, 12, 10, 10, 30, 0, 0)
    """

    def __init__(self, id, name, tax_id, bank_code, branch_code, account_number, account_type, amount, type, status,
                 tags, fee, transaction_ids, created, updated):
        Resource.__init__(self, id=id)

        self.name = name
        self.tax_id = tax_id
        self.bank_code = bank_code
        self.branch_code = branch_code
        self.account_number = account_number
        self.account_type = account_type
        self.amount = amount
        self.type = type
        self.status = status
        self.tags = tags
        self.fee = fee
        self.transaction_ids = transaction_ids
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": Deposit, "name": "Deposit"}


def get(id, user=None):
    """# Retrieve a specific Deposit
    Receive a single Deposit object from the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Deposit object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, status=None, sort=None, tags=None, ids=None, user=None):
    """# Retrieve Deposits
    Receive a generator of Deposit objects from the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "paid" or "registered"
    - sort [string, default "-created"]: sort order considered in response. Valid options are "created" or "-created".
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of Deposit objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        sort=sort,
        status=status,
        tags=tags,
        ids=ids,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, status=None, sort=None, tags=None, ids=None, user=None):
    """# Retrieve paged Deposits
    Receive a list of up to 100 Deposit objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "paid" or "registered"
    - sort [string, default "-created"]: sort order considered in response. Valid options are "created" or "-created".
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of Deposit objects with updated attributes
    - cursor to retrieve the next page of Deposit objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        sort=sort,
        status=status,
        tags=tags,
        ids=ids,
        user=user,
    )


def update(id, amount=None, user=None):
    """# Update Deposit entity
    Update the Deposit by passing its id to be partially or fully reversed.
    ## Parameters (required):
    - id [string]: Deposit id. ex: "5656565656565656"
    ## Parameters (optional):
    - amount [string, default None]: The new amount of the Deposit. If the amount = 0 the Deposit will be fully reversed
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - target Deposit with updated attributes
    """
    payload = {
        "amount": amount,
    }
    return rest.patch_id(resource=_resource, id=id, user=user, payload=payload)