from json import loads
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.signature import Signature
from ellipticcurve.publicKey import PublicKey
from requests import get as get_request
from ..utils import rest
from ..utils.api import from_api_json
from ..utils.request import fetch
from ..utils.resource import Resource
from ..utils.checks import check_datetime, check_date
from ..boleto.log.__log import _resource as _boleto_log_resource
from ..invoice.log.__log import _resource as _invoice_log_resource
from ..deposit.log.__log import _resource as _deposit_log_resource
from ..transfer.log.__log import _resource as _transfer_log_resource
from ..brcodepayment.log.__log import _resource as _brcodepayment_payment_log_resource
from ..boletopayment.log.__log import _resource as _boleto_payment_log_resource
from ..utilitypayment.log.__log import _resource as _utility_payment_log_resource
from ..boletoholmes.log.__log import _resource as _boleto_holmes_log_resource
from ..error import InvalidSignatureError
from ..utils import cache


_resource_by_subscription = {
    "transfer": _transfer_log_resource,
    "invoice": _invoice_log_resource,
    "deposit": _deposit_log_resource,
    "boleto": _boleto_log_resource,
    "brcode-payment": _brcodepayment_payment_log_resource,
    "boleto-payment": _boleto_payment_log_resource,
    "utility-payment": _utility_payment_log_resource,
    "holmes": _boleto_holmes_log_resource,
}


class Event(Resource):
    """# Webhook Event object
    An Event is the notification received from the subscription to the Webhook.
    Events cannot be created, but may be retrieved from the Stark Bank API to
    list all generated updates on entities.
    ## Attributes:
    - id [string]: unique id returned when the event is created. ex: "5656565656565656"
    - log [Log]: a Log object from one the subscription services (TransferLog, InvoiceLog, DepositLog, BoletoLog, BoletoHolmesLog, BrcodePaymentLog, BoletoPaymentLog or UtilityPaymentLog)
    - created [datetime.datetime]: creation datetime for the notification event. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - is_delivered [bool]: true if the event has been successfully delivered to the user url. ex: False
    - subscription [string]: service that triggered this event. ex: "transfer", "utility-payment"
    """

    def __init__(self, log, created, is_delivered, subscription, id):
        Resource.__init__(self, id=id)

        self.created = check_datetime(created)
        self.is_delivered = is_delivered
        self.subscription = subscription
        self.log = log
        if subscription in _resource_by_subscription:
            self.log = from_api_json(resource=_resource_by_subscription[subscription], json=log)


_resource = {"class": Event, "name": "Event"}


def get(id, user=None):
    """# Retrieve a specific notification Event
    Receive a single notification Event object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Event object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, is_delivered=None, user=None):
    """# Retrieve notification Events
    Receive a generator of notification Event objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - is_delivered [bool, default None]: bool to filter successfully delivered events. ex: True or False
    - user [Project object, default None]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of Event objects with updated attributes
    """
    return rest.get_list(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        is_delivered=is_delivered,
        user=user,
    )


def delete(id, user=None):
    """# Delete a webhook Event entity
    Delete a of notification Event entity previously created in the Stark Bank API by its ID
    ## Parameters (required):
    - id [string]: Event unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - deleted Event object
    """
    return rest.delete_id(resource=_resource, id=id, user=user)


def update(id, is_delivered, user=None):
    """# Update notification Event entity
    Update notification Event by passing id.
    If is_delivered is True, the event will no longer be returned on queries with is_delivered=False.
    ## Parameters (required):
    - id [list of strings]: Event unique ids. ex: "5656565656565656"
    - is_delivered [bool]: If True and event hasn't been delivered already, event will be set as delivered. ex: True
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - target Event with updated attributes
    """
    return rest.patch_id(resource=_resource, id=id, user=user, is_delivered=is_delivered)


def parse(content, signature, user=None):
    """# Create single notification Event from a content string
    Create a single Event object received from event listening at subscribed user endpoint.
    If the provided digital signature does not check out with the StarkBank public key, a
    starkbank.exception.InvalidSignatureException will be raised.
    ## Parameters (required):
    - content [string]: response content from request received at user endpoint (not parsed)
    - signature [string]: base-64 digital signature received at response header "Digital-Signature"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Parsed Event object
    """
    event = from_api_json(_resource, loads(content)["event"])

    try:
        signature = Signature.fromBase64(signature)
    except:
        raise InvalidSignatureError("The provided signature is not valid")

    if _verify_signature(content=content, signature=signature, user=user):
        return event
    if _verify_signature(content=content, signature=signature, user=user, refresh=True):
        return event

    raise InvalidSignatureError("The provided signature and content do not match the Stark Bank public key")


def _verify_signature(content, signature, user=None, refresh=False):
    public_key = cache.get("starkbank-public-key")
    if public_key is None or refresh:
        pem = _get_public_key_pem(user)
        public_key = PublicKey.fromPem(pem)
        cache["starkbank-public-key"] = public_key
    return Ecdsa.verify(message=content, signature=signature, publicKey=public_key)


def _get_public_key_pem(user):
    return fetch(method=get_request, path="/public-key", query={"limit": 1}, user=user).json()["publicKeys"][0]["content"]
