from ...utils import rest
from ...utils.checks import check_datetime, check_date
from ...utils.resource import Resource


class UtilityPayment(Resource):
    """UtilityPayment object

    When you initialize a UtilityPayment, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.

    Parameters (conditionally required):
        line [string, default None]: Number sequence that describes the payment. Either 'line' or 'bar_code' parameters are required. If both are sent, they must match. ex: "34191.09008 63571.277308 71444.640008 5 81960000000062"
        bar_code [string, default None]: Bar code number that describes the payment. Either 'line' or 'barCode' parameters are required. If both are sent, they must match. ex: "34195819600000000621090063571277307144464000"
    Parameters (required):
        description [string]: Text to be displayed in your statement (min. 10 characters). ex: "payment ABC"
    Parameters (optional):
        scheduled [datetime.date, default today]: payment scheduled date. ex: datetime.date(2020, 3, 10)
        tags [list of strings]: list of strings for tagging
    Attributes (return-only):
        id [string, default None]: unique id returned when payment is created. ex: "5656565656565656"
        status [string, default None]: current payment status. ex: "registered" or "paid"
        created [datetime.datetime, default None]: creation datetime for the payment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, description, line=None, bar_code=None, tags=None, scheduled=None, id=None, amount=None, status=None, created=None):
        Resource.__init__(self, id=id)

        self.line = line
        self.bar_code = bar_code
        self.description = description
        self.tags = tags
        self.scheduled = check_datetime(scheduled)
        self.status = status
        self.amount = amount
        self.created = check_datetime(created)


def create(payments, user=None):
    """Create UtilityPayments

    Send a list of UtilityPayment objects for creation in the Stark Bank API

    Parameters (required):
        payments [list of UtilityPayment objects]: list of UtilityPayment objects to be created in the API
    Parameters (optional):
        user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    Return:
        list of UtilityPayment objects with updated attributes
    """
    return rest.post(resource=UtilityPayment, entities=payments, user=user)


def get(id, user=None):
    """Retrieve a specific UtilityPayment

    Receive a single UtilityPayment object previously created by the Stark Bank API by passing its id

    Parameters (required):
        id [string]: object unique id. ex: "5656565656565656"
    Parameters (optional):
        user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    """
    return rest.get_id(resource=UtilityPayment, id=id, user=user)


def pdf(id, user=None):
    """Retrieve a specific UtilityPayment pdf file

    Receive a single UtilityPayment pdf file generated in the Stark Bank API by passing its id

    Send a list of UtilityPayment objects for creation in the Stark Bank API

    Parameters (required):
        id [string]: object unique id. ex: "5656565656565656"
    Parameters (optional):
        user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    Return:
        UtilityPayment pdf file
    """
    return rest.get_pdf(resource=UtilityPayment, id=id, user=user)


def query(limit=None, status=None, after=None, before=None, tags=None, ids=None, user=None):
    """Retrieve UtilityPayments

    Receive a generator of UtilityPayment objects previously created in the Stark Bank API

    Parameters (optional):
        limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
        status [string, default None]: filter for status of retrieved objects. ex: "paid"
        tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
        ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
        user [Project object, default None]: Project object. Not necessary if starkbank.user was set before function call
    Return:
        generator of UtilityPayment objects with updated attributes
    """
    return rest.get_list(resource=UtilityPayment, limit=limit, user=user, status=status, tags=tags, after=check_date(after), before=check_date(before), ids=ids)


def delete(ids, user=None):
    """Delete list of UtilityPayment entities

    Delete list of UtilityPayment entities previously created in the Stark Bank API

    Parameters (required):
        ids [list of strings]: list of UtilityPayment unique ids. ex: ["5656565656565656", "4545454545454545"]
    Parameters (optional):
        user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    Return:
        list of deleted UtilityPayments with updated attributes
    """
    return rest.delete_list(resource=UtilityPayment, ids=ids, user=user)