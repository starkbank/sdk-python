from json import dumps
from ..utils import rest
from ..utils.parse import parse_and_verify
from starkcore.utils.api import api_json
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date


class CorporatePurchase(Resource):
    """# CorporatePurchase object
    Displays the CorporatePurchase objects created in your Workspace.
    ## Attributes (return-only):
    - id [string]: unique id returned when CorporatePurchase is created. ex: "5656565656565656"
    - holder_id [string]: card holder unique id. ex: "5656565656565656"
    - holder_name [string]: card holder name. ex: "Tony Stark"
    - center_id [string]: target cost center ID. ex: "5656565656565656"
    - card_id [string]: unique id returned when CorporateCard is created. ex: "5656565656565656"
    - card_ending [string]: last 4 digits of the card number. ex: "1234"
    - description [string]: purchase descriptions. ex: "my_description"
    - amount [integer]: CorporatePurchase value in cents. Minimum = 0. ex: 1234 (= R$ 12.34)
    - tax [integer]: IOF amount taxed for international purchases. ex: 1234 (= R$ 12.34)
    - issuer_amount [integer]: issuer amount. ex: 1234 (= R$ 12.34)
    - issuer_currency_code [string]: issuer currency code. ex: "USD"
    - issuer_currency_symbol [string]: issuer currency symbol. ex: "$"
    - merchant_amount [integer]: merchant amount. ex: 1234 (= R$ 12.34)
    - merchant_currency_code [string]: merchant currency code. ex: "USD"
    - merchant_currency_symbol [string]: merchant currency symbol. ex: "$"
    - merchant_category_code [string]: merchant category code. ex: "fastFoodRestaurants"
    - merchant_category_type [string]: merchant category type. ex: "health"
    - merchant_country_code [string]: merchant country code. ex: "USA"
    - merchant_name [string]: merchant name. ex: "Google Cloud Platform"
    - merchant_display_name [string]: merchant name. ex: "Google Cloud Platform"
    - merchant_display_url [string]: public merchant icon (png image). ex: "https://sandbox.api.starkbank.com/v2/corporate-icon/merchant/ifood.png"
    - merchant_fee [integer]: fee charged by the merchant to cover specific costs, such as ATM withdrawal logistics, etc. ex: 200 (= R$ 2.00)
    - method_code [string]: method code. Options: "chip", "token", "server", "manual", "magstripe" or "contactless"
    - tags [list of strings]: list of strings for tagging returned by the sub-issuer during the authorization. ex: ["travel", "food"]
    - corporate_transaction_ids [list of strings]: ledger transaction ids linked to this Purchase
    - status [string]: current CorporateCard status. Options: "approved", "canceled", "denied", "confirmed", "voided"
    - updated [datetime.datetime]: latest update datetime for the CorporatePurchase. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime]: creation datetime for the CorporatePurchase. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, id=None, holder_id=None, holder_name=None, center_id=None, card_id=None, card_ending=None, 
                 description=None, amount=None, tax=None, issuer_amount=None, issuer_currency_code=None, issuer_currency_symbol=None, 
                 merchant_amount=None, merchant_currency_code=None, merchant_currency_symbol=None, merchant_category_code=None, 
                 merchant_category_type=None, merchant_country_code=None, merchant_name=None, merchant_display_name=None, 
                 merchant_display_url=None, merchant_fee=None, method_code=None, tags=None, corporate_transaction_ids=None, 
                 status=None, updated=None, created=None):
        Resource.__init__(self, id=id)

        self.id = id
        self.holder_id = holder_id
        self.holder_name = holder_name
        self.center_id = center_id
        self.card_id = card_id
        self.card_ending = card_ending
        self.description = description
        self.amount = amount
        self.tax = tax
        self.issuer_amount = issuer_amount
        self.issuer_currency_code = issuer_currency_code
        self.issuer_currency_symbol = issuer_currency_symbol
        self.merchant_amount = merchant_amount
        self.merchant_currency_code = merchant_currency_code
        self.merchant_currency_symbol = merchant_currency_symbol
        self.merchant_category_code = merchant_category_code
        self.merchant_category_type = merchant_category_type
        self.merchant_country_code = merchant_country_code
        self.merchant_name = merchant_name
        self.merchant_display_name = merchant_display_name
        self.merchant_display_url = merchant_display_url
        self.merchant_fee = merchant_fee
        self.method_code = method_code
        self.tags = tags
        self.corporate_transaction_ids = corporate_transaction_ids
        self.status = status
        self.updated = check_datetime(updated)
        self.created = check_datetime(created)


_resource = {"class": CorporatePurchase, "name": "CorporatePurchase"}


def get(id, user=None):
    """# Retrieve a specific CorporatePurchase
    Receive a single CorporatePurchase object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - CorporatePurchase object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(ids=None, limit=None, after=None, before=None, merchant_category_types=None, holder_ids=None, card_ids=None,
          status=None, user=None):
    """# Retrieve CorporatePurchases
    Receive a generator of CorporatePurchase objects previously created in the Stark Bank API
    ## Parameters (optional):
    - ids [list of strings, default None]: purchase IDs
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - merchant_category_types [list of strings, default None]: merchant category type. ex: "health"
    - holder_ids [list of strings, default None]: card holder IDs. ex: ["5656565656565656", "4545454545454545"]
    - card_ids [list of strings, default None]: card  IDs. ex: ["5656565656565656", "4545454545454545"]
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["approved", "canceled", "denied", "confirmed", "voided"],
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of CorporatePurchase objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        ids=ids,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        merchant_category_types=merchant_category_types,
        holder_ids=holder_ids,
        card_ids=card_ids,
        status=status,
        user=user,
    )


def page(merchant_category_types=None, holder_ids=None, card_ids=None, status=None, after=None, before=None, ids=None,
        cursor=None, limit=None, user=None):
    """# Retrieve paged CorporatePurchase
    Receive a list of up to 100 CorporatePurchase objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. Max = 100. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - merchant_category_types [list of strings, default None]: merchant category type. ex: "health"
    - holder_ids [list of strings, default None]: card holder IDs. ex: ["5656565656565656", "4545454545454545"]
    - card_ids [list of strings, default None]: card  IDs. ex: ["5656565656565656", "4545454545454545"]
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["approved", "canceled", "denied", "confirmed", "voided"]
    - ids [list of strings, default None]: purchase IDs
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of CorporatePurchase objects with updated attributes
    - cursor to retrieve the next page of CorporatePurchase objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        ids=ids,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        merchant_category_types=merchant_category_types,
        holder_ids=holder_ids,
        card_ids=card_ids,
        status=status,
        user=user,
    )


def parse(content, signature, user=None):
    """# Create a single verified CorporatePurchase authorization request from a content string
    Use this method to parse and verify the authenticity of the authorization request received at the informed endpoint.
    Authorization requests are posted to your registered endpoint whenever CorporatePurchases are received.
    They present CorporatePurchase data that must be analyzed and answered with approval or declination.
    If the provided digital signature does not check out with the starkbank public key, a stark.exception.InvalidSignatureException will be raised.
    If the authorization request is not answered within 2 seconds or is not answered with an HTTP status code 200 the CorporatePurchase will go through the pre-configured stand-in validation.
    ## Parameters (required):
    - content [string]: response content from request received at user endpoint (not parsed)
    - signature [string]: base-64 digital signature received at response header "Digital-Signature"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Parsed CorporatePurchase object
    """
    return parse_and_verify(
        content=content,
        signature=signature,
        user=user,
        resource=_resource,
        key="",
    )


def response(status, amount=None, reason=None, tags=None):
    """# Helps you respond CorporatePurchase requests
    ## Parameters (required):
    - status [string]: sub-issuer response to the authorization. ex: "approved" or "denied"
    ## Parameters (conditionally required):
    - reason [string]: denial reason. Options: "other", "blocked", "lostCard", "stolenCard", "invalidPin", "invalidCard", "cardExpired", "issuerError", "concurrency", "standInDenial", "subIssuerError", "invalidPurpose", "invalidZipCode", "invalidWalletId", "inconsistentCard", "settlementFailed", "cardRuleMismatch", "invalidExpiration", "prepaidInstallment", "holderRuleMismatch", "insufficientBalance", "tooManyTransactions", "invalidSecurityCode", "invalidPaymentMethod", "confirmationDeadline", "withdrawalAmountLimit", "insufficientCardLimit", "insufficientHolderLimit"
    ## Parameters (optional):
    - amount [integer, default None]: amount in cents that was authorized. ex: 1234 (= R$ 12.34)
    - tags [list of strings, default None]: tags to filter retrieved object. ex: ["tony", "stark"]
    ## Return:
    - Dumped JSON string that must be returned to us on the CorporatePurchase request
    """
    params = {"authorization": {
        "status": status,
        "amount": amount,
        "reason": reason,
        "tags": tags,
    }}
    return dumps(api_json(params))
