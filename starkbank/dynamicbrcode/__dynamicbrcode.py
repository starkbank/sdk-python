# coding: utf-8
from starkcore.utils.resource import Resource
from starkcore.utils.api import from_api_json
from starkcore.utils.checks import check_datetime, check_date, check_timedelta
from ..utils import rest
from .rule.__rule import _sub_resource as _rule_resource, Rule


class DynamicBrcode(Resource):
    """# DynamicBrcode object
    When you initialize a DynamicBrcode, the entity will not be automatically
    sent to the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    DynamicBrcodes are conciliated BR Codes that can be used to receive Pix transactions in a convenient way.
    When a DynamicBrcode is paid, a Deposit is created with the tags parameter containing the character “dynamic-brcode/” followed by the DynamicBrcode’s uuid "dynamic-brcode/{uuid}" for conciliation.
    Additionally, all tags passed on the DynamicBrcode will be transferred to the respective Deposit resource.
    ## Parameters (required):
    - amount [integer]: DynamicBrcode value in cents. Minimum = 0 (any value will be accepted). ex: 1234 (= R$ 12.34)
    ## Parameters (optional):
    - expiration [integer or datetime.timedelta, default 3600 (1 hour)]: time interval in seconds between due date and expiration date. ex 123456789
    - tags [list of strings, default []]: list of strings for tagging, these will be passed to the respective Deposit resource when paid
    - rules [list of DynamicBrcode.Rules, default []]: list of DynamicBrcode.Rule objects for modifying invoice behavior. ex: [DynamicBrcode.Rule(key="allowedTaxIds", value=[ "012.345.678-90", "45.059.493/0001-73" ])]
    ## Attributes (return-only):
    - id [string]: id returned on creation, this is the BR code. ex: "00020126360014br.gov.bcb.pix0114+552840092118152040000530398654040.095802BR5915Jamie Lannister6009Sao Paulo620705038566304FC6C"
    - uuid [string]: unique uuid returned when the DynamicBrcode is created. ex: "4e2eab725ddd495f9c98ffd97440702d"
    - picture_url [string]: public QR Code (png image) URL. ex: "https://sandbox.api.starkbank.com/v2/dynamic-brcode/d3ebb1bd92024df1ab6e5a353ee799a4.png"
    - updated [datetime.datetime]: latest update datetime for the DynamicBrcode. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime]: creation datetime for the DynamicBrcode. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, amount, expiration=None, tags=None, rules=None, id=None, uuid=None, picture_url=None,
                 updated=None, created=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.expiration = check_timedelta(expiration)
        self.rules = _parse_rules(rules)
        self.tags = tags
        self.uuid = uuid
        self.picture_url = picture_url
        self.updated = check_datetime(updated)
        self.created = check_datetime(created)

_resource = {"class": DynamicBrcode, "name": "DynamicBrcode"}


def _parse_rules(rules):
    if rules is None:
        return None
    parsed_rules = []
    for rule in rules:
        if isinstance(rule, Rule):
            parsed_rules.append(rule)
            continue
        parsed_rules.append(from_api_json(_rule_resource, rule))
    return parsed_rules


def create(brcodes, user=None):
    """# Create DynamicBrcodes
    Send a list of DynamicBrcode objects for creation in the Stark Bank API
    ## Parameters (required):
    - brcodes [list of DynamicBrcode objects]: list of DynamicBrcode objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of DynamicBrcode objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=brcodes, user=user)


def get(uuid, user=None):
    """# Retrieve a specific DynamicBrcode
    Receive a single DynamicBrcode object previously created in the Stark Bank API by its uuid
    ## Parameters (required):
    - uuid [string]: object's unique uuid. ex: "901e71f2447c43c886f58366a5432c4b"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - DynamicBrcode object with updated attributes
    """
    return rest.get_id(resource=_resource, id=uuid, user=user)


def query(limit=None, after=None, before=None, tags=None, uuids=None, user=None):
    """# Retrieve DynamicBrcodes
    Receive a generator of DynamicBrcode objects previously created by this user in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created or updated only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created or updated only before specified date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - uuids [list of strings, default None]: list of uuids to filter retrieved objects. ex: ["901e71f2447c43c886f58366a5432c4b", "4e2eab725ddd495f9c98ffd97440702d"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of DynamicBrcode objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        tags=tags,
        uuids=uuids,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, tags=None, uuids=None, user=None):
    """# Retrieve paged DynamicBrcodes
    Receive a list of up to 100 DynamicBrcode objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your brcodes.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None]: date filter for objects created or updated only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created or updated only before specified date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - uuids [list of strings, default None]: list of uuids to filter retrieved objects. ex: ["901e71f2447c43c886f58366a5432c4b", "4e2eab725ddd495f9c98ffd97440702d"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of DynamicBrcode objects with updated attributes
    - cursor to retrieve the next page of DynamicBrcode objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        tags=tags,
        uuids=uuids,
        user=user,
    )
