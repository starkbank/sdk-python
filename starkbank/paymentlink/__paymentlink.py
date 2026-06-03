from datetime import datetime
from ..utils import rest
from starkcore.utils.api import from_api_json
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_date, check_datetime, check_timedelta
from .allowedinstallment.__allowedinstallment import AllowedInstallment
from .allowedinstallment.__allowedinstallment import _sub_resource as _allowed_installment_sub_resource
from .item.__item import Item
from .item.__item import _sub_resource as _item_sub_resource


class PaymentLink(Resource):
    """# PaymentLink object
    When you initialize a PaymentLink, the entity will not be automatically
    sent to the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    ## Parameters (required):
    - name [string]: payment link name displayed to the payer. ex: "Assinatura Premium"
    - amount [integer]: payment link total amount in cents. ex: 15000 (= R$ 150.00)
    - usage_mode [string]: defines how many times the link can be paid. ex: "single" or "multi"
    - allowed_methods [list of strings]: list of accepted payment methods. ex: ["credit", "debit"]
    ## Parameters (conditionally required):
    - allowed_installments [list of PaymentLink.AllowedInstallment objects]: list of accepted installment options. Required when allowed_methods includes "credit" or "debit". ex: [PaymentLink.AllowedInstallment(count=1, total_amount=15000)]
    ## Parameters (optional):
    - expiration [integer or datetime.timedelta, default None]: time interval in seconds between creation and expiration when sent to the API. ex: 36000 (= 10 hours). On API responses this field is returned as a datetime.datetime instead.
    - description [string, default None]: payment link description displayed to the payer. ex: "Plano trinta dias"
    - success_url [string, default None]: URL where the payer is redirected after a successful payment. ex: "https://merchant.com/obrigado"
    - tags [list of strings, default None]: list of strings for tagging. ex: ["campanha-abril", "plano-premium"]
    - timestamp [datetime.datetime or string, default None]: payment link reference timestamp. ex: datetime.datetime(2026, 4, 8, 12, 0, 0, 0)
    - items [list of PaymentLink.Item objects, default None]: list of PaymentLink.Item objects describing the purchase contents. ex: [PaymentLink.Item(code="PREM-001", description="Plano Premium Mensal", quantity=1, unit_price=15000, total_price=15000, discount=0)]
    - metadata [dictionary, default None]: dictionary object used to store additional information about the PaymentLink object. ex: {"customerId": "5678901234567890", "orderId": "ORD-2026-001"}
    ## Attributes (return-only):
    - id [string]: unique id returned when PaymentLink is created. ex: "5656565656565656"
    - status [string]: current PaymentLink status. ex: "active", "expired", "paid", "canceling" or "canceled"
    - token [string]: public token used to access the PaymentLink web page. ex: "b3c836df0d744fad9c8adcd960304930"
    - url [string]: public URL where the payer can complete the payment. ex: "https://starkv2.sandbox.starkbank.com/paymentlink/b3c836df0d744fad9c8adcd960304930"
    - created [datetime.datetime]: creation datetime for the PaymentLink. ex: datetime.datetime(2026, 4, 8, 12, 0, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the PaymentLink. ex: datetime.datetime(2026, 4, 8, 12, 0, 0, 0)
    """

    def __init__(self, name, amount, usage_mode, allowed_methods, allowed_installments=None, expiration=None,
                 description=None, success_url=None, tags=None, timestamp=None, items=None, metadata=None,
                 id=None, status=None, token=None, url=None, created=None, updated=None):
        Resource.__init__(self, id=id)

        self.name = name
        self.amount = amount
        self.usage_mode = usage_mode
        self.allowed_methods = allowed_methods
        self.allowed_installments = _parse_allowed_installments(allowed_installments)
        self.expiration = _parse_expiration(expiration)
        self.description = description
        self.success_url = success_url
        self.tags = tags
        # API returns "" (not omitted) when the link was created without a timestamp.
        self.timestamp = check_datetime(timestamp or None)
        self.items = _parse_items(items)
        self.metadata = metadata
        self.status = status
        self.token = token
        self.url = url
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": PaymentLink, "name": "PaymentLink"}


def _parse_allowed_installments(allowed_installments):
    if allowed_installments is None:
        return None
    parsed_allowed_installments = []
    for allowed_installment in allowed_installments:
        if isinstance(allowed_installment, AllowedInstallment):
            parsed_allowed_installments.append(allowed_installment)
            continue
        parsed_allowed_installments.append(from_api_json(_allowed_installment_sub_resource, allowed_installment))
    return parsed_allowed_installments


def _parse_expiration(expiration):
    # API quirk: `expiration` is sent as a seconds interval on create
    # but returned as an ISO datetime on read (routes.md:214).
    if isinstance(expiration, (str, datetime)):
        return check_datetime(expiration)
    return check_timedelta(expiration)


def _parse_items(items):
    if items is None:
        return None
    parsed_items = []
    for item in items:
        if isinstance(item, Item):
            parsed_items.append(item)
            continue
        parsed_items.append(from_api_json(_item_sub_resource, item))
    return parsed_items


def create(links, user=None):
    """# Create PaymentLinks
    Send a list of PaymentLink objects for creation in the Stark Bank API.
    Each PaymentLink with `allowed_methods` containing `"credit"` or `"debit"` must include
    `allowed_installments`. The API accepts up to 100 PaymentLinks per request.
    ## Parameters (required):
    - links [list of PaymentLink objects]: list of PaymentLink objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of PaymentLink objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=links, user=user)


def get(id, user=None):
    """# Retrieve a specific PaymentLink
    Receive a single PaymentLink object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - PaymentLink object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, status=None, tags=None, ids=None, user=None):
    """# Retrieve PaymentLinks
    Receive a generator of PaymentLink objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created or updated only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created or updated only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string or list of strings, default None]: filter for status of retrieved objects. ex: "active" or ["active", "paid"]. Accepted values: "active", "expired", "paid", "canceling", "canceled"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. Accepts up to 30 ids. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of PaymentLink objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        tags=tags,
        ids=ids,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, status=None, tags=None, ids=None, user=None):
    """# Retrieve paged PaymentLinks
    Receive a list of up to 100 PaymentLink objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None]: date filter for objects created or updated only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created or updated only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string or list of strings, default None]: filter for status of retrieved objects. ex: "active" or ["active", "paid"]. Accepted values: "active", "expired", "paid", "canceling", "canceled"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. Accepts up to 30 ids. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of PaymentLink objects with updated attributes
    - cursor to retrieve the next page of PaymentLink objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        tags=tags,
        ids=ids,
        user=user,
    )


def update(id, status=None, user=None):
    """# Update PaymentLink entity
    Update a PaymentLink by passing id. You may cancel an active PaymentLink by passing 'canceling' in the status.
    ## Parameters (required):
    - id [string]: PaymentLink id. ex: '5656565656565656'
    ## Parameters (optional):
    - status [string, default None]: You may cancel the PaymentLink by passing 'canceling' in the status. Only "canceling" is accepted by the API
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - target PaymentLink with updated attributes
    """
    payload = {
        "status": status,
    }
    return rest.patch_id(resource=_resource, id=id, user=user, payload=payload)
