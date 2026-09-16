from starkcore.utils.resource import Resource
from ..utils import rest
from starkcore.utils.checks import check_date, check_datetime


class MerchantPurchase(Resource):
    """# MerchantPurchase object
    When you initialize a MerchantPurchase, the entity will not be automatically
    sent to the Stark Bank API. The 'create' function sends the object
    to the Stark Bank API and returns the created object.
    ## Parameters (required):
    - amount [integer]: MerchantPurchase value in cents. ex: 1234 (= R$ 12.34)
    - card_id [string]: unique id of the MerchantCard or MerchantSession Purchase used. ex: "5656565656565656"
    - funding_type [string]: type of funding used. ex: "credit", "debit"
    - installment_count [integer]: number of installments the purchase is split into. ex: 1
    ## Parameters (optional):
    - card_expiration, card_number, card_security_code, holder_name, holder_email, holder_phone, holder_id [string, default None]: card and holder data, required only when not created through a MerchantSession.
    - billing_country_code, billing_city, billing_state_code, billing_street_line_1, billing_street_line_2, billing_zip_code [string, default None]: billing address data.
    - metadata [dictionary, default None]: additional 3DS metadata sent by the merchant's browser/app.
    - soft_descriptor [string, default None]: text that will be shown in the holder's bank statement. ex: "my-store"
    - tags [list of strings, default None]: list of strings for tagging
    ## Attributes (return-only):
    - id [string]: unique id returned when MerchantPurchase is created. ex: "5656565656565656"
    - card_ending [string]: last 4 digits of the card used. ex: "1234"
    - challenge_mode [string]: whether 3DS holder verification was used. ex: "enabled", "disabled"
    - challenge_url [string]: URL to the 3DS challenge, when applicable.
    - currency_code [string]: currency of the purchase. ex: "BRL"
    - end_to_end_id [string]: unique transaction id for the acquirer network.
    - fee [integer]: fee charged when the MerchantPurchase is processed. ex: 200 (= R$ 2.00)
    - network [string]: card network flag. ex: "visa", "mastercard"
    - source [string]: locator of the entity that generated the purchase. ex: "merchant-session/{sessionId}"
    - status [string]: current MerchantPurchase status. ex: "approved", "confirmed", "canceled", "voided"
    - created [datetime.datetime]: creation datetime for the MerchantPurchase. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the MerchantPurchase. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, amount, card_id, funding_type, installment_count, id=None, card_expiration=None,
                 card_number=None, card_security_code=None,holder_name=None, holder_email=None, holder_phone=None, holder_id=None,
                 billing_country_code=None, billing_city=None,billing_state_code=None, billing_street_line_1=None,
                 billing_street_line_2=None, billing_zip_code=None, metadata=None, card_ending=None, soft_descriptor=None,
                 challenge_mode=None, challenge_url=None, created=None, currency_code=None, end_to_end_id=None,
                 fee=None, network=None, source=None, status=None, tags=None, updated=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.installment_count = installment_count
        self.card_expiration = card_expiration
        self.card_number = card_number
        self.card_security_code = card_security_code
        self.holder_name = holder_name
        self.holder_email = holder_email
        self.holder_phone = holder_phone
        self.holder_id = holder_id
        self.funding_type = funding_type
        self.billing_country_code = billing_country_code
        self.billing_city = billing_city
        self.billing_state_code = billing_state_code
        self.billing_street_line_1 = billing_street_line_1
        self.billing_street_line_2 = billing_street_line_2
        self.billing_zip_code = billing_zip_code
        self.metadata = metadata
        self.card_ending = card_ending
        self.card_id = card_id
        self.soft_descriptor = soft_descriptor
        self.challenge_mode = challenge_mode
        self.challenge_url = challenge_url
        self.currency_code = currency_code
        self.end_to_end_id = end_to_end_id
        self.fee = fee
        self.network = network
        self.source = source
        self.status = status
        self.tags = tags
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": MerchantPurchase, "name": "MerchantPurchase"}


def create(merchant_purchase, user=None):
    """# Create a MerchantPurchase
    Send a MerchantPurchase object for creation in the Stark Bank API
    ## Parameters (required):
    - merchant_purchase [MerchantPurchase object]: MerchantPurchase object to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - MerchantPurchase object with updated attributes
    """
    return rest.post_single(resource=_resource, entity=merchant_purchase, user=user)


def get(id, user=None):
    """# Retrieve a specific MerchantPurchase
    Receive a single MerchantPurchase object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - MerchantPurchase object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, status=None, tags=None, ids=None, holder_id=None, user=None):
    """# Retrieve MerchantPurchases
    Receive a generator of MerchantPurchase objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "approved"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - holder_id [string, default None]: filter for purchases made with cards belonging to a specific holder. ex: "5656565656565656"
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of MerchantPurchase objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        tags=tags,
        ids=ids,
        holder_id=holder_id,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, status=None, tags=None, ids=None, holder_id=None, user=None):
    """# Retrieve paged MerchantPurchases
    Receive a list of up to 100 MerchantPurchase objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "approved"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - holder_id [string, default None]: filter for purchases made with cards belonging to a specific holder. ex: "5656565656565656"
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of MerchantPurchase objects with updated attributes
    - cursor to retrieve the next page of MerchantPurchase objects
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
        holder_id=holder_id,
        user=user,
    )


def update(id, status=None, amount=None, user=None):
    """# Update MerchantPurchase entity
    Update a MerchantPurchase by its id. If the purchase is "approved", you may only cancel it by passing status="canceled" together with amount=0. If the purchase is "confirmed", you may pass status="reversed" with a lower amount to debit and reverse the difference, partially or totally; a partial reversal keeps status "confirmed", while a full reversal moves it to "voided".
    ## Parameters (required):
    - id [string]: MerchantPurchase id.
    ## Parameters (optional):
    - status [string, default None]: "canceled" or "reversed", per the rules above.
    - amount [integer, default None]: new amount; 0 to cancel an approved purchase, or a lower value to partially/fully reverse a confirmed one.
    - user [Organization/Project object, default None].
    ## Return:
    - target MerchantPurchase with updated attributes
    """
    payload = {
        "status": status,
        "amount": amount
    }
    return rest.patch_id(resource=_resource, id=id, user=user, payload=payload)

