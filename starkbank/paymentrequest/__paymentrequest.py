from ..utils import rest
from starkcore.utils.api import from_api_json
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date
from ..transfer.__transfer import Transfer
from ..transaction.__transaction import Transaction
from ..brcodepayment.__brcodepayment import BrcodePayment
from ..boletopayment.__boletopayment import BoletoPayment
from ..utilitypayment.__utilitypayment import UtilityPayment
from ..darfpayment.__darfpayment import DarfPayment
from ..taxpayment.__taxpayment import TaxPayment
from ..transfer.__transfer import _resource as _transfer_resource
from ..transaction.__transaction import _resource as _transaction_resource
from ..boletopayment.__boletopayment import _resource as _boleto_payment_resource
from ..brcodepayment.__brcodepayment import _resource as _brcode_payment_resource
from ..utilitypayment.__utilitypayment import _resource as _utility_payment_resource
from ..darfpayment.__darfpayment import _resource as _darf_payment_resource
from ..taxpayment.__taxpayment import _resource as _tax_payment_resource
class PaymentRequest(Resource):
    """# PaymentRequest object
    A PaymentRequest is an indirect request to access a specific cash-out service
    (such as Transfers, BoletoPayments, etc.) which goes through the cost center
    approval flow on our website. To emit a PaymentRequest, you must direct it to
    a specific cost center by its ID, which can be retrieved on our website at the
    cost center page.
    ## Parameters (required):
    - center_id [string]: target cost center ID. ex: "5656565656565656"
    - payment [Transfer, BoletoPayment, UtilityPayment, BrcodePayment, Transaction, DarfPayment, TaxPayment or dictionary]: payment entity that should be approved and executed.
    ## Parameters (conditionally required):
    - type [string]: payment type, inferred from the payment parameter if it is not a dictionary. ex: "transfer", "boleto-payment"
    ## Parameters (optional):
    - due [datetime.date or string, default today]: Payment target date in ISO format. ex: 2020-04-30
    - tags [list of strings]: list of strings for tagging
    ## Attributes (return-only):
    - id [string]: unique id returned when a PaymentRequest is created. ex: "5656565656565656"
    - amount [integer]: PaymentRequest amount. ex: 100000 = R$1.000,00
    - description [string]: payment request description. ex: "Tony Stark's Suit"
    - status [string]: current PaymentRequest status. ex: "pending" or "approved"
    - actions [list of dictionaries]: list of actions that are affecting this PaymentRequest. ex: [{"type": "member", "id": "56565656565656, "action": "requested"}]
    - updated [datetime.datetime]: latest update datetime for the PaymentRequest. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime]: creation datetime for the PaymentRequest. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, center_id, payment, type=None, due=None, tags=None, id=None, amount=None,
                 description=None, status=None, actions=None, updated=None, created=None):
        Resource.__init__(self, id=id)

        self.center_id = center_id
        self.due = due
        self.tags = tags
        self.amount = amount
        self.description = description
        self.status = status
        self.actions = actions
        self.updated = check_datetime(updated)
        self.created = check_datetime(created)

        self.payment, self.type = _parse_payment(payment=payment, type=type)


def _parse_payment(payment, type):
    if isinstance(payment, dict):
        try:
            return from_api_json(*({
                "transfer": _transfer_resource,
                "transaction": _transaction_resource,
                "boleto-payment": _boleto_payment_resource,
                "brcode-payment": _brcode_payment_resource,
                "utility-payment": _utility_payment_resource,
                "darf-payment": _darf_payment_resource,
                "tax-payment": _tax_payment_resource,
            }[type], payment)), type
        except KeyError:
            return payment, type

    if type:
        return payment, type

    if isinstance(payment, Transfer):
        return payment, "transfer"
    if isinstance(payment, Transaction):
        return payment, "transaction"
    if isinstance(payment, BrcodePayment):
        return payment, "brcode-payment"
    if isinstance(payment, BoletoPayment):
        return payment, "boleto-payment"
    if isinstance(payment, UtilityPayment):
        return payment, "utility-payment"
    if isinstance(payment, DarfPayment):
        return payment, "darf-payment"
    if isinstance(payment, TaxPayment):
        return payment, "tax-payment"

    raise Exception(
        "payment must be either "
        "a dictionary"
        ", a starkbank.Transfer"
        ", a starkbank.Transaction"
        ", a starkbank.BrcodePayment"
        ", a starkbank.BoletoPayment"
        ", a starkbank.UtilityPayment"
        ", a starkbank.TaxPayment"
        " or a starkbank.DarfPayment"
        ", but not a {}".format(type(payment))
    )


_resource = {"class": PaymentRequest, "name": "PaymentRequest"}


def create(requests, user=None):
    """# Create PaymentRequests
    Send a list of PaymentRequest objects for creation in the Stark Bank API
    ## Parameters (required):
    - requests [list of PaymentRequest objects]: list of PaymentRequest objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of PaymentRequest objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=requests, user=user)


def query(center_id, limit=None, after=None, before=None, sort=None, status=None, type=None, tags=None, ids=None, user=None):
    """# Retrieve PaymentRequests
    Receive a generator of PaymentRequest objects previously created by this user in the Stark Bank API
    ## Parameters (required):
    - center_id [string]: target cost center ID. ex: "5656565656565656"
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created or updated only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created or updated only before specified date. ex: datetime.date(2020, 3, 10)
    - sort [string, default "-created"]: sort order considered in response. Valid options are "-created" or "-due".
    - status [string, default None]: filter for status of retrieved objects. ex: "success" or "failed"
    - type [string, default None]: payment type, inferred from the payment parameter if it is not a dictionary. ex: "transfer", "boleto-payment"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of PaymentRequest objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        center_id=center_id,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        sort=sort,
        status=status,
        type=type,
        tags=tags,
        ids=ids,
        user=user,
    )


def page(center_id, cursor=None, limit=None, after=None, before=None, sort=None, status=None, type=None, tags=None, ids=None, user=None):
    """# Retrieve paged PaymentRequests
    Receive a list of up to 100 PaymentRequest objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (required):
    - center_id [string]: target cost center ID. ex: "5656565656565656"
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None]: date filter for objects created or updated only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created or updated only before specified date. ex: datetime.date(2020, 3, 10)
    - sort [string, default "-created"]: sort order considered in response. Valid options are "-created" or "-due".
    - status [string, default None]: filter for status of retrieved objects. ex: "success" or "failed"
    - type [string, default None]: payment type, inferred from the payment parameter if it is not a dictionary. ex: "transfer", "boleto-payment"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of PaymentRequest objects with updated attributes
    - cursor to retrieve the next page of PaymentRequest objects
    """
    return rest.get_page(
        resource=_resource,
        center_id=center_id,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        sort=sort,
        status=status,
        type=type,
        tags=tags,
        ids=ids,
        user=user,
    )
