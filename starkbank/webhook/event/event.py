from json import loads
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.signature import Signature
from ellipticcurve.publicKey import PublicKey
from ...utils import rest
from ...utils.api import from_api_json
from ...utils.resource import Resource
from ...utils.rest import get_public_key
from ...utils.checks import check_datetime, check_date
from ...boleto.log import BoletoLog
from ...transfer.log import TransferLog
from ...exception import InvalidSignatureException
from ...payment.boleto.log import BoletoPaymentLog
from ...utils import cache


class Event(Resource):
    """Description: Webhook Event object

    An Event is the notification received from the subscription
    to the Webhook. Events cannot be created, but may be retrieved
    from the Stark Bank API to list all generated updates on entities.

    Attributes:
        log [Log]: a Log object from one the subscription services (notification EventLog, TransferLog or notification EventPaymentLog)
        created [datetime.datetime, default None]: creation datetime for the notification Event. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
        delivered [datetime.datetime, default None]: delivery datetime of the notification event on user endpoint. Is None if there have been no successful attempts on delivery. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
        subscription [string]: service to which this notification event refers to. ex: "transfer" or "charge"
        id [string, default None]: unique id returned when log is created. ex: "5656565656565656"
    """

    def __init__(self, log, created, delivered, subscription, id):
        Resource.__init__(self, id=id)

        self.created = check_datetime(created)
        self.delivered = check_datetime(delivered)
        self.subscription = subscription
        self.log = from_api_json(*{
            "transfer": (TransferLog, log),
            "boleto": (BoletoLog, log),
            "boleto-payment": (BoletoPaymentLog, log),
        }[subscription])


def get(id, user=None):
    """Retrieve a single notification Event

    Receive a single notification Event object previously created in the Stark Bank API by passing its id

    Parameters (required):
        id [string]: object unique id. ex: "5656565656565656"
    Parameters (optional):
        user [Project object]: optional Project object. Not necessary if starkbank.user was set before function call
    Return
        Event object with updated return-only attributes
    """
    return rest.get_id(resource=Event, id=id, user=user)


def query(limit=None, after=None, before=None, is_delivered=None, user=None):
    """Retrieve notification Events

    Receive a generator of notification Event objects previously created in the Stark Bank API

    Parameters (optional):
        limit [integer, default None]: optional number of objects to be retrieved. Unlimited if None. ex: 35
        is_delivered [bool, default None]: optional bool to filter successfully delivered events. ex: True or False
        after [datetime.date, default None] optional date filter for objects only after specified date. ex: datetime.date(2020, 3, 10)
        before [datetime.date, default None] optional date filter for objects only before specified date. ex: datetime.date(2020, 3, 10)
        user [Project object, default None]: optional Project object. Not necessary if starkbank.user was set before function call
    Return
        generator of Event objects with updated return-only attributes
    """
    return rest.get_list(resource=Event, limit=limit, user=user, is_delivered=is_delivered, after=check_date(after), before=check_date(before))


def delete(ids, user=None):
    """Delete a single notification Event entity

    Delete a list of notification Event entities previously created in the Stark Bank API

    Parameters (required):
        ids [list of strings]: list of object unique ids. ex: ["5656565656565656", "4545454545454545"]
    Parameters (optional):
        user [Project object]: optional Project object. Not necessary if starkbank.user was set before function call
    Return
        list of deleted objects with updated return-only attributes
    """
    return rest.delete_list(resource=Event, ids=ids, user=user)


def set_delivered(ids, user=None):
    """Set notification Event entities as delivered

    Set list of notification Event entities as delivered with delivery datetime at update time by passing id

    Parameters (required):
        ids [list of strings]: list of object unique ids. ex: ["5656565656565656", "4545454545454545"]
    Parameters (optional):
        user [Project object]: optional Project object. Not necessary if starkbank.user was set before function call
    """
    return rest.patch_list(resource=Event, ids=ids, user=user)


def process(content, signature, user=None):
    """Process single notification Event

    Process a single notification Event object received from event listening at subscribed user endpoint

    Parameters (required):
        content [string]: response content from request received at user endpoint
        signature [string]: base-64 digital signature from received response header
    Parameters (optional):
        user [Project object]: optional Project object. Not necessary if starkbank.user was set before function call
    Return
        Event object with updated return-only attributes
    """
    event = from_api_json(Event, loads(content)["event"])

    if _verify_signature(content=content, signature=signature, user=user):
        return event
    if _verify_signature(content=content, signature=signature, user=user, refresh=True):
        return event

    raise InvalidSignatureException("the provided signature and message were not verified by the Stark Bank public key")


def _verify_signature(content, signature, user=None, refresh=False):
    signature = Signature.fromBase64(signature)
    public_key = cache.get("starkbank-public-key")
    if public_key is None or refresh:
        public_key = PublicKey.fromPem(get_public_key(limit=1, user=user)[0]["content"])
        cache["starkbank-public-key"] = public_key
    return Ecdsa.verify(message=content, signature=signature, publicKey=public_key)
