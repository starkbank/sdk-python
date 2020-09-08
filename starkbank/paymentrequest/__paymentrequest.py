from ..utils import rest
from ..utils.api import from_api_json
from ..utils.resource import Resource
from ..utils.checks import check_datetime
from ..transfer.__transfer import Transfer
from ..boletopayment.__boletopayment import BoletoPayment
from ..utilitypayment.__utilitypayment import UtilityPayment
from ..transaction.__transaction import Transaction
from ..transfer.__transfer import _resource as _transfer_resource
from ..boletopayment.__boletopayment import _resource as _boleto_payment_resource
from ..utilitypayment.__utilitypayment import _resource as _utility_payment_resource
from ..transaction.__transaction import _resource as _transaction_resource


class PaymentRequest(Resource):
    """# PaymentRequest object
    A PaymentRequest is an indirect request to access a specific cash-out service
    (such as Transfers, BoletoPayments, etc.) which goes through the cost-center
    approval flow on our website. To emit a PaymentRequest, you must direct it to
    a specific cost-center by its ID, which can be retrieved on our website at the
    cost-center page.
    ## Parameters (required):
    - center_id [string]: target cost-center ID. ex: "5656565656565656"
    - payment [Transfer, BoletoPayment, UtilityPayment, Transaction or dictionary]: payment entity that should be approved and executed.
    ## Parameters (conditionally required):
    - type [string]: payment type, inferred from the payment parameter if it is not a dictionary. ex: "transfer", "boleto-payment"
    ## Parameters (optional):
    - due [datetime.date or string, default today]: Payment target date in ISO format. ex: 2020-04-30
    - tags [list of strings]: list of strings for tagging
    - attachments [list of dictionaries]: list of dictionaries containing "name" (specifies file name) and "data" (specifies file binary data encoded in base64) fields
    ## Attributes (return-only):
    - id [string, default None]: unique id returned when PaymentRequest is created. ex: "5656565656565656"
    - amount [integer, default None]: PaymentRequest amount. ex: 100000 = R$1.000,00
    - status [string, default None]: current PaymentRequest status. ex: "pending" or "approved"
    - actions [list of dictionaries, default None]: list of actions that are affecting this PaymentRequest. ex: [{"type": "member", "id": "56565656565656, "action": "requested"}]
    - updated [datetime.datetime, default None]: latest update datetime for the PaymentRequest. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime, default None]: creation datetime for the PaymentRequest. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, center_id, payment, type=None, due=None, tags=None, attachments=None, id=None, amount=None,
                 status=None, actions=None, updated=None, created=None):
        Resource.__init__(self, id=id)

        self.center_id = center_id
        self.due = due
        self.tags = tags
        self.attachments = attachments
        self.amount = amount
        self.status = status
        self.actions = actions
        self.updated = updated
        self.created = check_datetime(created)

        self.payment, self.type = _parse_payment(payment=payment, type=type)


def _parse_payment(payment, type):
    if isinstance(payment, dict):
        try:
            return from_api_json(*({
                "transfer": _transfer_resource,
                "transaction": _transaction_resource,
                "boleto-payment": _boleto_payment_resource,
                "utility-payment": _utility_payment_resource,
            }[type], payment)), type
        except KeyError:
            raise Exception(
                "if payment is a dictionary, type must be"
                " transfer"
                ", transaction"
                ", boleto-payment"
                "or utility-payment"
            )

    if type:
        return payment, type

    if isinstance(payment, Transfer):
        return payment, "transfer"
    if isinstance(payment, Transaction):
        return payment, "transaction"
    if isinstance(payment, BoletoPayment):
        return payment, "boleto-payment"
    if isinstance(payment, UtilityPayment):
        return payment, "utility-payment"

    raise Exception(
        "payment must be either "
        "a dictionary"
        ", a starkbank.Transfer"
        ", a starkbank.Transaction"
        ", a starkbank.BoletoPayment"
        " or a starkbank.UtilityPayment"
        ", but not a {}".format(type(payment))
    )


_resource = {"class": PaymentRequest, "name": "PaymentRequest"}


def create(requests, user=None):
    """# Create PaymentRequests
    Send a list of PaymentRequest objects for creation in the Stark Bank API
    ## Parameters (required):
    - requests [list of PaymentRequest objects]: list of PaymentRequest objects to be created in the API
    ## Parameters (optional):
    - user [Project object]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of PaymentRequest objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=requests, user=user)
