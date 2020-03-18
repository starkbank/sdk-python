from ..utils import rest
from ..utils.checks import check_datetime, check_date
from ..utils.resource import Resource


class Transfer(Resource):
    """Transfer object

    When you initialize a Transfer, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.

    Parameters (required):
        amount [integer]: amount in cents to be transferred. ex: 1234 (= R$ 12.34)
        name [string]: receiver full name. ex: "Anthony Edward Stark"
        tax_id [string]: receiver tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
        bank_code [string]: receiver 1 to 3 digits of the bank institution in Brazil. ex: "200" or "341"
        branch_code [string]: receiver bank account branch. Use '-' in case there is a verifier digit. ex: "1357-9"
        account_number [string]: Receiver Bank Account number. Use '-' before the verifier digit. ex: "876543-2"
    Parameters (optional):
        tags [list of strings]: list of strings for reference when searching for transfers. ex: ["employees", "monthly"]
    Attributes (return-only):
        id [string, default None]: unique id returned when Transfer is created. ex: "5656565656565656"
        fee [integer, default None]: fee charged when transfer is created. ex: 200 (= R$ 2.00)
        status [string, default None]: current boleto status. ex: "registered" or "paid"
        created [datetime.datetime, default None]: creation datetime for the boleto. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, amount, name, tax_id, bank_code, branch_code, account_number, fee=None, tags=None, status=None, id=None, created=None):
        Resource.__init__(self, id=id)

        self.tax_id = tax_id
        self.amount = amount
        self.fee = fee
        self.name = name
        self.bank_code = bank_code
        self.branch_code = branch_code
        self.account_number = account_number
        self.tags = tags
        self.status = status
        self.created = check_datetime(created)


def create(transfers, user=None):
    """Create Transfers

    Send a list of Transfer objects for creation in the Stark Bank API

    Parameters (required):
        transfers [list of Transfer objects]: list of Transfer objects to be created in the API
    Parameters (optional):
        user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    Return:
        list of Transfer objects with updated attributes
    """
    return rest.post(resource=Transfer, entities=transfers, user=user)


def get(id, user=None):
    """Retrieve a specific Transfer

    Receive a single Transfer object previously created in the Stark Bank API by passing its id

    Parameters (required):
        id [string]: object unique id. ex: "5656565656565656"
    Parameters (optional):
        user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    Return:
        Transfer object with updated attributes
    """
    return rest.get_id(resource=Transfer, id=id, user=user)


def pdf(id, user=None):
    """Retrieve a specific Transfer pdf file

    Receive a single Transfer pdf receipt file generated in the Stark Bank API by passing its id.
    Only valid for transfers with "success" status

    Send a list of Transfer objects for creation in the Stark Bank API

    Parameters (required):
        id [string]: object unique id. ex: "5656565656565656"
    Parameters (optional):
        user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    Return:
        Transfer pdf file
    """
    return rest.get_pdf(resource=Transfer, id=id, user=user)


def query(limit=None, transaction_ids=None, tags=None, after=None, before=None, status=None, sort=None, user=None):
    """Retrieve Transfers

    Receive a generator of Transfer objects previously created in the Stark Bank API

    Parameters (optional):
        limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
        status [string, default None]: filter for status of retrieved objects. ex: "paid" or "registered"
        tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
        transaction_ids [list of strings, default None]: list of Transaction ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
        after [datetime.date, default None]: date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
        before [datetime.date, default None]: date filter for objects only before specified date. ex: datetime.date(2020, 3, 10)
        sort [string, default "-created"]: sort order considered in response. Valid options are 'created', '-created', 'updated' or '-updated'.
        user [Project object, default None]: Project object. Not necessary if starkbank.user was set before function call
    Return:
        generator of Transfer objects with updated attributes
    """
    return rest.get_list(resource=Transfer, limit=limit, user=user, status=status, tags=tags, after=check_date(after), before=check_date(before), transaction_ids=transaction_ids, sort=sort)


def delete(ids, user=None):
    """Delete list of Transfer entities

    Delete list of Transfer entities previously created in the Stark Bank API

    Parameters (required):
        ids [list of strings]: list of Transfer unique ids. ex: ["5656565656565656", "4545454545454545"]
    Parameters (optional):
        user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    Return:
        list of deleted Transfers with updated attributes
    """
    return rest.delete_list(resource=Transfer, ids=ids, user=user)
