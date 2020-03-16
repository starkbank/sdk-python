from starkbank.utils import rest
from starkbank.utils.checks import check_datetime, check_date
from starkbank.boleto.boleto import Boleto
from starkbank.utils.api import from_api_json
from starkbank.utils.resource import Resource


class BoletoLog(Resource):
    """Description: BoletoLog object

    Every time a Boleto entity is modified, a correspondent BoletoLog
    is generated for the entity. This log is never generated by the
    user, but it can be retrieved to check additional information
    on the Boleto.

    Attributes:
        boleto [Boleto]: Boleto entity to which the log refers to.
        id [string, default None]: unique id returned when log is created. ex: "5656565656565656"
        errors [list]: list of errors in case log was generated by webhook event
        type [string, default None]: type of the Boleto event which triggered log creation. ex: "registered" or "paid"
        created [datetime.datetime, default None]: creation datetime for the boleto. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, id, created, type, errors, boleto):
        Resource.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.boleto = from_api_json(Boleto, boleto)


def get(id, user=None):
    """Retrieve a single BoletoLog

    Receive a single BoletoLog object previously created by the Stark Bank API by passing its id

    Parameters (required):
        id [string]: object unique id. ex: "5656565656565656"
    Parameters (optional):
        user [Project object]: optional Project object. Not necessary if starkbank.user was set before function call
    """
    return rest.get_id(resource=BoletoLog, id=id, user=user)


def query(limit=None, boleto_ids=None, events=None, after=None, before=None, user=None):
    """Retrieve BoletoLogs

    Receive a generator of BoletoLog objects previously created in the Stark Bank API

    Parameters (optional):
        limit [integer, default None]: optional number of objects to be retrieved. Unlimited if None. ex: 35
        boleto_ids [list of strings, default None]: optional list of ids to filter selected objects. ex: ["5656565656565656", "4545454545454545"]
        events [string, default None]: optional filter for events of objects retrieved. ex: "paid" or "registered"
        user [Project object, default None]: optional Project object. Not necessary if starkbank.user was set before function call
    """
    return rest.get_list(resource=BoletoLog, limit=limit, user=user, events=events, boleto_ids=boleto_ids, after=check_date(after), before=check_date(before))
