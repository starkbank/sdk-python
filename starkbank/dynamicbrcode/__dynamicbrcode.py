# coding: utf-8
from starkcore.utils.resource import Resource
from starkcore.utils.api import from_api_json
from starkcore.utils.checks import check_datetime, check_date, check_timedelta
from ..utils import rest
from .rule.__rule import _sub_resource as _rule_resource, Rule


class DynamicBrcode(Resource):
    """# DynamicBrcode object
    Check out our API Documentation at https://starkbank.com/docs/api#dynamic-brcode
    """

    def __init__(self, amount, expiration=None, tags=None, display_description=None, rules=None, id=None, uuid=None,
                 picture_url=None, updated=None, created=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.expiration = check_timedelta(expiration)
        self.display_description = display_description
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
