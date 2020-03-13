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
    return rest.get_id(resource=Event, id=id, user=user)


def query(limit=None, after=None, before=None, is_delivered=None, user=None):
    return rest.get_list(resource=Event, limit=limit, user=user, is_delivered=is_delivered, after=check_date(after), before=check_date(before))


def process(content, signature, user=None):
    event = from_api_json(Event, loads(content)["event"])

    if _verify_signature(content=content, signature=signature, user=user):
        return event
    if _verify_signature(content=content, signature=signature, user=user, refresh=True):
        return event

    raise InvalidSignatureException("the provided signature and message were not verified by the Stark Bank public key")


def _verify_signature(content, signature, user=None, refresh=False):
    signature = Signature.fromBase64(signature)
    public_key = cache.get("webhook-public-key")
    if public_key is None or refresh:
        public_key = PublicKey.fromPem(get_public_key(service_id="webhook", user=user))
        cache["webhook-public-key"] = public_key
    return Ecdsa.verify(message=content, signature=signature, publicKey=public_key)
