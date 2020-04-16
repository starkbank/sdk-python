from ...utils import rest
from ...utils.api import from_api_json
from ...utils.checks import check_datetime, check_date
from ...utils.resource import Resource
from ..__utilitypayment import _resource as _payment_resource


class Log(Resource):
    """# utilitypayment.Log object
    Every time a UtilityPayment entity is modified, a corresponding utilitypayment.Log
    is generated for the entity. This log is never generated by the user, but it can
    be retrieved to check additional information on the UtilityPayment.
    ## Attributes:
    - id [string]: unique id returned when the log is created. ex: "5656565656565656"
    - payment [UtilityPayment]: UtilityPayment entity to which the log refers to.
    - errors [list of strings]: list of errors linked to this BoletoPayment event.
    - type [string]: type of the UtilityPayment event which triggered the log creation. ex: "registered" or "paid"
    - created [datetime.datetime]: creation datetime for the payment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, id, created, type, errors, payment):
        Resource.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.payment = from_api_json(_payment_resource, payment)


_resource = {"class": Log, "name": "UtilityPaymentLog"}


def get(id, user=None):
    """# Retrieve a specific utilitypayment.Log
    Receive a single utilitypayment.Log object previously created by the Stark Bank API by passing its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - utilitypayment.Log object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, payment_ids=None, types=None, after=None, before=None, user=None):
    """# Retrieve utilitypayment.Log's
    Receive a generator of utilitypayment.Log objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - payment_ids [list of strings, default None]: list of UtilityPayment ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - types [list of strings, default None]: filter retrieved objects by event types. ex: "paid" or "registered"
    - after [datetime.date, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date, default None] date filter for objects only before specified date. ex: datetime.date(2020, 3, 10)
    - user [Project object, default None]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of utilitypayment.Log objects with updated attributes
    """
    return rest.get_list(resource=_resource, limit=limit, user=user, types=types, payment_ids=payment_ids, after=check_date(after), before=check_date(before))
