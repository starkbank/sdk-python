from ..transfer import Transfer
from ...utils import rest
from ...utils.api import from_api_json
from ...utils.checks import check_datetime
from ...utils.resource import Resource


class TransferLog(Resource):
    """TransferLog object

    Every time a Transfer entity is modified, a corresponding TransferLog
    is generated for the entity. This log is never generated by the
    user.

    Attributes:
        id [string]: unique id returned when the log is created. ex: "5656565656565656"
        transfer [Transfer]: Transfer entity to which the log refers to.
        errors [list of strings]: list of errors linked to this BoletoPayment event.
        type [string]: type of the Transfer event which triggered the log creation. ex: "processing" or "success"
        created [datetime.datetime]: creation datetime for the transfer. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, id, created, type, errors, transfer):
        Resource.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.transfer = from_api_json(Transfer, transfer)


def get(id, user=None):
    """Retrieve a specific TransferLog

    Receive a single TransferLog object previously created by the Stark Bank API by passing its id

    Parameters (required):
        id [string]: object unique id. ex: "5656565656565656"
    Parameters (optional):
        user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    Return:
        TransferLog object with updated attributes
    """
    return rest.get_id(resource=TransferLog, id=id, user=user)


def query(limit=None, transfer_ids=None, types=None, user=None):
    """Retrieve TransferLogs

    Receive a generator of TransferLog objects previously created in the Stark Bank API

    Parameters (optional):
        limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
        transfer_ids [list of strings, default None]: list of Transfer ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
        types [list of strings, default None]: filter retrieved objects by types. ex: "success" or "failed"
        user [Project object, default None]: Project object. Not necessary if starkbank.user was set before function call
    Return:
        list of TransferLog objects with updated attributes
    """
    return rest.get_list(resource=TransferLog, limit=limit, user=user, types=types, transfer_ids=transfer_ids)
