from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date


class AcquiringPurchase(Resource):
    """# AcquiringPurchase object
    An AcquiringPurchase object represents a card purchase through the Stark Bank API.
    When you initialize an AcquiringPurchases, the entity will not be automatically sent to the Stark Bank API.
    The 'create' function sends the objects to the Stark Bank API, starts the authorization process and returns the list of created objects.
    ## Parameters (required):
    - amount [integer]: AcquiringPurchase amount in cents. Minimum = 0. ex: 1234 (= R$ 12.34)
    - currency_code [string]: AcquiringPurchase currency code. ex: "USD"
    - card_id [string]: unique id referencing an AcquiringCard. ex: "5656565656565656"
    - installments [integer]: number of installments. ex: 3
    - merchant_category_code [string]: AcquiringPurchase merchant category code. ex: "fastFoodRestaurants"
    - rules [list of dicts]: list of rules. ex: [{"key": "force_3DS", "value": True}, {"key": "auto_capture", "value": True}]
    ## Parameters (optional):
    - metadata [string, default None]: free parameter for user-defined purposes
    ## Attributes (return-only):
    - id [string]: unique id returned when an AcquiringPurchase is created. ex: "5656565656565656"
    - status [string]: current AcquiringPurchase status. Options: "pending", "approved", "denied", "canceled", "confirmed", "voided"
    - created [datetime.datetime]: creation datetime. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, amount, currency_code, card_id, installments, merchant_category_code, rules, metadata=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.currency_code = currency_code
        self.card_id = card_id
        self.installments = installments
        self.merchant_category_code = merchant_category_code  ## add merchant_category_number?
        self.rules = rules
        self.metadata = metadata


_resource = {"class": AcquiringPurchase, "name": "AcquiringPurchase"}


def create(purchases, user=None):
    """# Create AcquiringPurchases
    Send a list of AcquiringPurchase objects for creation and authorization in the Stark Bank API
    ## Parameters (required):
    - purchases [list of AcquiringPurchase objects]: list of AcquiringPurchase objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - list of AcquiringCard objects
    """
    return rest.post_multi(resource=_resource, entities=purchases, user=user)


def get(id, user=None):
    """# Retrieve a specific AcquiringPurchase object
    Receive a single AcquiringPurchase object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - AcquiringPurchase object
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(ids=None, limit=None, after=None, before=None, card_ids=None, status=None, user=None):
    """# Retrieve AcquiringPurchases
    Receive a generator of AcquiringPurchase objects previously created in the Stark Bank API
    ## Parameters (optional):
    - ids [list of strings, default [], default None]: purchase IDs
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - card_ids [list of strings, default []]: card  IDs. ex: ["5656565656565656", "4545454545454545"]
    - status [list of strings, default None]: filter for status of retrieved objects. Options: ["approved", "canceled", "denied", "confirmed", "voided"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of AcquiringPurchase objects
    """
    return rest.get_stream(
        resource=_resource,
        ids=ids,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        card_ids=card_ids,
        status=status,
        user=user,
    )


def page(card_ids=None, ids=None, status=None, after=None, before=None, user=None, limit=None, cursor=None):
    """# Retrieve paged AcquiringPurchase
    Receive a list of AcquiringPurchase objects previously created in the Stark Bank API and the cursor to the next page.
    ## Parameters (optional):
    - card_ids [list of strings, default []]: card  IDs. ex: ["5656565656565656", "4545454545454545"]
    - ids [list of strings, default [], default None]: purchase IDs
    - status [list of strings, default None]: filter for status of retrieved objects. Options: ["approved", "canceled", "denied", "confirmed", "voided"]
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. Max = 100. ex: 35
    - cursor [string, default None]: cursor returned on the previous page function call
    ## Return:
    - list of AcquiringPurchase objects
    - cursor to retrieve the next page of AcquiringPurchase objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        ids=ids,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        card_ids=card_ids,
        status=status,
        user=user,
    )


def update(id, status=None, amount=None, tags=None, user=None):
    """# Update AcquiringPurchase entity
    Update, capture or cancel an AcquiringPurchase through its id.
    ## Parameters (required):
    - id [string]: AcquiringPurchase id. ex: '5656565656565656'
    ## Parameters (optional):
    - tags [list of strings]: list of strings for tagging
    - amount [integer]: amount to capture. Maximum = AcquiringPurchase amount. ex: 1234 (= R$ 12.34)
    - status [string]: status to capture or cancel an authorized purchase. Options: ["confirmed", "canceled"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - target AcquiringPurchase with updated attributes
    """
    payload = {
        "tags": tags,
        "status": status,
        "amount": amount,
    }
    return rest.patch_id(resource=_resource, id=id, user=user, payload=payload)
