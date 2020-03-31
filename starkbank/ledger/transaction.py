from starkbank.utils import rest
from starkbank.utils.checks import check_datetime, check_date
from starkbank.utils.resource import Resource


class Transaction(Resource):
    """Transaction object

    A Transaction is a transfer of funds between workspaces inside Stark Bank.
    Transactions created by the user are only for internal transactions.
    Other operations (such as transfer or charge-payment) will automatically
    create a transaction for the user which can be retrieved for the statement.
    When you initialize a Transaction, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.

    Parameters (required):
        amount [integer]: amount in cents to be transferred. ex: 1234 (= R$ 12.34)
        description [string]: text to be displayed in the receiver and the sender statements (Min. 10 characters). ex: "funds redistribution"
        external_id [string]: unique id, generated by user, to avoid duplicated transactions. ex: "transaction ABC 2020-03-30"
        received_id [string]: unique id of the receiving workspace. ex: "5656565656565656"
    Parameters (optional):
        tags [list of strings]: list of strings for reference when searching transactions (may be empty). ex: ["abc", "test"]
    Attributes (return-only):
        source [string, default None]: unique locator of the related entity in the API reference
        id [string, default None]: unique id returned when Transaction is created. ex: "7656565656565656"
        fee [integer, default None]: fee charged when transfer is created. ex: 200 (= R$ 2.00)
        created [datetime.datetime, default None]: creation datetime for the boleto. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, amount, description, external_id, receiver_id, tags=None, id=None, fee=None, created=None, source=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.description = description
        self.tags = tags
        self.external_id = external_id
        self.receiver_id = receiver_id
        self.fee = fee
        self.created = check_datetime(created)
        self.source = source


def create(transactions, user=None):
    """Create Transactions

    Send a list of Transaction objects for creation in the Stark Bank API

    Parameters (required):
        transactions [list of Transaction objects]: list of Transaction objects to be created in the API
    Parameters (optional):
        user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    Return:
        list of Transaction objects with updated attributes
    """
    return rest.post(resource=Transaction, entities=transactions, user=user)


def get(id, user=None):
    """Retrieve a specific Transaction

    Receive a single Transaction object previously created in the Stark Bank API by passing its id

    Parameters (required):
        id [string]: object unique id. ex: "5656565656565656"
    Parameters (optional):
        user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    Return:
        Transaction object with updated attributes
    """
    return rest.get_id(resource=Transaction, id=id, user=user)


def query(limit=None, external_ids=None, after=None, before=None, user=None):
    """Retrieve Transactions

    Receive a generator of Transaction objects previously created in the Stark Bank API

    Parameters (optional):
        limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
        external_ids [list of strings, default None]: list of external ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
        after [datetime.date, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
        before [datetime.date, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
        user [Project object, default None]: Project object. Not necessary if starkbank.user was set before function call
    Return:
        generator of Transaction objects with updated attributes
    """
    return rest.get_list(resource=Transaction, limit=limit, user=user, external_ids=external_ids, after=check_date(after), before=check_date(before))
