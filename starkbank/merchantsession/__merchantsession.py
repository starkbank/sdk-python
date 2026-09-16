from starkcore.utils.resource import Resource
from ..utils import rest
from starkcore.utils.api import from_api_json
from .allowedinstallment.__allowedinstallment import AllowedInstallment
from .allowedinstallment.__allowedinstallment import _sub_resource as _allowed_installments_sub_resource
from starkcore.utils.checks import check_date, check_datetime
from .__purchase import _resource as purchase_resource


class MerchantSession(Resource):
    """# MerchantSession object
    When you initialize a MerchantSession, the entity will not be automatically
    sent to the Stark Bank API. The 'create' function sends the object
    to the Stark Bank API and returns the created object.
    ## Parameters (required):
    - allowed_funding_types [list of strings]: funding types allowed for the purchase. Options: "credit", "debit"
    - allowed_installments [list of MerchantSession.AllowedInstallment]: amount/installment-count combinations allowed for the purchase
    - expiration [integer or datetime.timedelta]: time in seconds from creation until the session expires; after expiration, no purchase can be created with it
    ## Parameters (optional):
    - allowed_ips [list of strings, default []]: IP addresses allowed to create a purchase with this session
    - challenge_mode [string, default "enabled"]: whether 3DS holder verification is used. Options: "enabled", "disabled"
    - tags [list of strings, default []]: list of strings for tagging. All tags will be converted to lowercase.
    ## Attributes (return-only):
    - id [string]: unique id returned when MerchantSession is created. ex: "5656565656565656"
    - uuid [string]: unique uuid returned when MerchantSession is created, used to create a MerchantSession Purchase. ex: "901e71f2447c43c886f58366a5432c4b"
    - holder_id [string]: unique id of the card holder associated with this session, when applicable.
    - soft_descriptor [string]: text that will be shown in the holder's bank statement, when applicable.
    - status [string]: current MerchantSession status. ex: "created", "expired"
    - created [datetime.datetime]: creation datetime for the MerchantSession. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the MerchantSession. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, allowed_funding_types, allowed_installments, expiration, id=None, allowed_ips=None,
                 challenge_mode=None, created=None, status=None, tags=None, updated=None, uuid=None, holder_id=None, soft_descriptor=None):
        Resource.__init__(self, id=id)

        self.allowed_funding_types = allowed_funding_types
        self.allowed_installments = _parse_allowed_installments(allowed_installments)
        self.allowed_ips = allowed_ips
        self.challenge_mode = challenge_mode
        self.expiration = expiration
        self.status = status
        self.tags = tags
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)
        self.uuid = uuid
        self.holder_id = holder_id
        self.soft_descriptor = soft_descriptor

_resource = {"class": MerchantSession, "name": "MerchantSession"}


def _parse_allowed_installments(allowed_installments):
    if allowed_installments is None:
        return []
    parsed_allowed_installments = []
    for allowed_installment in allowed_installments:
        if isinstance(allowed_installment, AllowedInstallment):
            parsed_allowed_installments.append(allowed_installment)
            continue
        parsed_allowed_installments.append(from_api_json(_allowed_installments_sub_resource, allowed_installment))
    return parsed_allowed_installments


def create(merchant_session, user=None):
    """# Create a MerchantSession
    Send a MerchantSession object for creation in the Stark Bank API
    ## Parameters (required):
    - merchant_session [MerchantSession object]: MerchantSession object to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - MerchantSession object with updated attributes
    """
    return rest.post_single(resource=_resource, entity=merchant_session, user=user)


def get(id, user=None):
    """# Retrieve a specific MerchantSession
    Receive a single MerchantSession object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - MerchantSession object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, status=None, tags=None, ids=None, after=None, before=None, holder_id=None, user=None):
    """# Retrieve MerchantSessions
    Receive a generator of MerchantSession objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - status [string, default None]: filter for status of retrieved objects. ex: "created"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - holder_id [string, default None]: filter for sessions belonging to a specific card holder. ex: "5656565656565656"
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of MerchantSession objects with updated attributes
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


def page(cursor=None, limit=None, status=None, tags=None, ids=None, after=None, before=None, holder_id=None, user=None):
    """# Retrieve paged MerchantSessions
    Receive a list of up to 100 MerchantSession objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - status [string, default None]: filter for status of retrieved objects. ex: "created"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - holder_id [string, default None]: filter for sessions belonging to a specific card holder. ex: "5656565656565656"
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of MerchantSession objects with updated attributes
    - cursor to retrieve the next page of MerchantSession objects
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


def purchase(uuid, purchase, user=None):
    """# Create a MerchantSession Purchase
    Send a MerchantPurchase object linked to a previously created MerchantSession, identified by its uuid, for creation in the Stark Bank API.
    Depending on the MerchantSession's allowed_funding_types and 3DS configuration, the billing and card holder fields on the MerchantPurchase
    (card_expiration, card_number, card_security_code, holder_name, holder_email, holder_phone, holder_id, billing_country_code, billing_city,
    billing_state_code, billing_street_line_1, billing_street_line_2, billing_zip_code) and the 3DS metadata may be conditionally required.
    ## Parameters (required):
    - uuid [string]: MerchantSession unique uuid returned on creation. ex: "901e71f2447c43c886f58366a5432c4b"
    - purchase [MerchantPurchase object]: MerchantPurchase object to be created against this session
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - MerchantPurchase object with updated attributes
    """
    return rest.post_sub_resource(resource=_resource, id=uuid, sub_resource=purchase_resource, entity=purchase, user=user)

