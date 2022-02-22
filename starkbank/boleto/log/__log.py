from ...utils import rest
from starkcore.utils.checks import check_datetime, check_date
from starkcore.utils.api import from_api_json
from starkcore.utils.resource import Resource
from ..__boleto import _resource as _boleto_resource


class Log(Resource):
    """# boleto.Log object
    Every time a Boleto entity is updated, a corresponding boleto.Log
    is generated for the entity. This log is never generated by the
    user, but it can be retrieved to check additional information
    on the Boleto.
    ## Attributes:
    - id [string]: unique id returned when the log is created. ex: "5656565656565656"
    - boleto [Boleto]: Boleto entity to which the log refers to.
    - errors [list of strings]: list of errors linked to this Boleto event
    - type [string]: type of the Boleto event which triggered the log creation. ex: "registered" or "paid"
    - created [datetime.datetime]: creation datetime for the log. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, id, created, type, errors, boleto):
        Resource.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.boleto = from_api_json(_boleto_resource, boleto)


_resource = {"class": Log, "name": "BoletoLog"}


def get(id, user=None):
    """# Retrieve a specific boleto.Log
    Receive a single boleto.Log object previously created by the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - boleto.Log object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, types=None, boleto_ids=None, user=None):
    """# Retrieve boleto.Logs
    Receive a generator of boleto.Log objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter for log event types. ex: "paid" or "registered"
    - boleto_ids [list of strings, default None]: list of Boleto ids to filter logs. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of boleto.Log objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        boleto_ids=boleto_ids,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, types=None, boleto_ids=None, user=None):
    """# Retrieve paged boleto.Logs
    Receive a list of up to 100 boleto.Log objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter for log event types. ex: "paid" or "registered"
    - boleto_ids [list of strings, default None]: list of Boleto ids to filter logs. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of boleto.Log objects with updated attributes
    - cursor to retrieve the next page of boleto.Log objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        boleto_ids=boleto_ids,
        user=user,
    )
