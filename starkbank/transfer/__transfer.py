from ..utils import rest
from ..utils.checks import check_datetime, check_date
from ..utils.resource import Resource


class Transfer(Resource):
    """# Transfer object
    When you initialize a Transfer, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    ## Parameters (required):
    - amount [integer]: amount in cents to be transferred. ex: 1234 (= R$ 12.34)
    - name [string]: receiver full name. ex: "Anthony Edward Stark"
    - tax_id [string]: receiver tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
    - bank_code [string]: receiver 1 to 3 digits of the bank institution in Brazil. ex: "200" or "341"
    - branch_code [string]: receiver bank account branch. Use '-' in case there is a verifier digit. ex: "1357-9"
    - account_number [string]: Receiver Bank Account number. Use '-' before the verifier digit. ex: "876543-2"
    ## Parameters (optional):
    - tags [list of strings]: list of strings for reference when searching for transfers. ex: ["employees", "monthly"]
    ## Attributes (return-only):
    - id [string, default None]: unique id returned when Transfer is created. ex: "5656565656565656"
    - fee [integer, default None]: fee charged when transfer is created. ex: 200 (= R$ 2.00)
    - status [string, default None]: current boleto status. ex: "registered" or "paid"
    - transaction_ids [list of strings, default None]: ledger transaction ids linked to this transfer (if there are two, second is the chargeback). ex: ["19827356981273"]
    - created [datetime.datetime, default None]: creation datetime for the transfer. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime, default None]: latest update datetime for the transfer. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, amount, name, tax_id, bank_code, branch_code, account_number, transaction_ids=None, fee=None, tags=None, status=None, id=None, created=None, updated=None):
        Resource.__init__(self, id=id)

        self.tax_id = tax_id
        self.amount = amount
        self.name = name
        self.bank_code = bank_code
        self.branch_code = branch_code
        self.account_number = account_number
        self.tags = tags
        self.fee = fee
        self.status = status
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)
        self.transaction_ids = transaction_ids


_resource = {"class": Transfer, "name": "Transfer"}


def create(transfers, user=None):
    """# Create Transfers
    Send a list of Transfer objects for creation in the Stark Bank API
    ## Parameters (required):
    - transfers [list of Transfer objects]: list of Transfer objects to be created in the API
    ## Parameters (optional):
    - user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of Transfer objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=transfers, user=user)


def get(id, user=None):
    """# Retrieve a specific Transfer
    Receive a single Transfer object previously created in the Stark Bank API by passing its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Transfer object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def pdf(id, user=None):
    """# Retrieve a specific Transfer pdf file
    Receive a single Transfer pdf receipt file generated in the Stark Bank API by passing its id.
    Only valid for transfers with "processing" and "success" status.
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Transfer pdf file
    """
    return rest.get_pdf(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, transaction_ids=None, status=None, sort=None, tags=None, user=None):
    """# Retrieve Transfers
    Receive a generator of Transfer objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created or updated only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created or updated only before specified date. ex: datetime.date(2020, 3, 10)
    - transaction_ids [list of strings, default None]: list of transaction IDs linked to the desired transfers. ex: ["5656565656565656", "4545454545454545"]
    - status [string, default None]: filter for status of retrieved objects. ex: "paid" or "registered"
    - sort [string, default "-created"]: sort order considered in response. Valid options are 'created', '-created', 'updated' or '-updated'.
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - user [Project object, default None]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of Transfer objects with updated attributes
    """
    return rest.get_list(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        transaction_ids=transaction_ids,
        status=status,
        sort=sort,
        tags=tags,
        user=user,
    )
