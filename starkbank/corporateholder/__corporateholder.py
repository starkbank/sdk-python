from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date
from ..utils import rest
from ..corporaterule import parse_rules
from .__permission import parse_permissions


class CorporateHolder(Resource):
    """# CorporateHolder object
    The CorporateHolder describes a card holder that may group several cards.
    When you initialize a CorporateHolder, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the created object.
    ## Parameters (required):
    - name [string]: cardholder name. ex: "Tony Stark"
    ## Parameters (optional):
    - center_id [string, default None]: target cost center ID. ex: "5656565656565656"
    - permissions [list of Permission object, default None]: list of Permission object representing access granted to an user for a particular cardholder.
    - rules [list of CorporateRule, default []]: [EXPANDABLE] list of holder spending rules
    - tags [list of strings, default []]: list of strings for tagging. ex: ["travel", "food"]
    ## Attributes (return-only):
    - id [string]: unique id returned when CorporateHolder is created. ex: "5656565656565656"
    - status [string]: current CorporateHolder status. ex: "active", "blocked", "canceled"
    - updated [datetime.datetime]: latest update datetime for the CorporateHolder. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime]: creation datetime for the CorporateHolder. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, name, center_id=None, permissions=None, rules=None, tags=None, id=None, status=None, updated=None, created=None):
        Resource.__init__(self, id=id)

        self.name = name
        self.center_id = center_id
        self.permissions = parse_permissions(permissions)
        self.rules = parse_rules(rules)
        self.tags = tags
        self.status = status
        self.updated = check_datetime(updated)
        self.created = check_datetime(created)


_resource = {"class": CorporateHolder, "name": "CorporateHolder"}


def create(holders, expand=None, user=None):
    """# Create CorporateHolders
    Send a list of CorporateHolder objects for creation at the Stark Bank API
    ## Parameters (required):
    - holders [list of CorporateHolder objects]: list of CorporateHolder objects to be created in the API
    ## Parameters (optional):
    - expand [list of strings, default None]: fields to expand information. Options: ["rules"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of CorporateHolder objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=holders, expand=expand, user=user)


def get(id, expand=None, user=None):
    """# Retrieve a specific CorporateHolder
    Receive a single CorporateHolder object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - expand [list of strings, default None]: fields to expand information. Options: ["rules"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - CorporateHolder object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, expand=expand, user=user)


def query(limit=None, after=None, before=None, ids=None, status=None, tags=None, expand=None, user=None):
    """# Retrieve CorporateHolders
    Receive a generator of CorporateHolder objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["active", "blocked", "canceled"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - expand [string, default None]: fields to expand information. Options: ["rules"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of CorporateHolder objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        ids=ids,
        status=status,
        tags=tags,
        expand=expand,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, ids=None, status=None, tags=None, expand=None, user=None):
    """# Retrieve CorporateHolders
    Receive a list of up to 100 CorporateHolder objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. Max = 100. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["active", "blocked", "canceled"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - expand [string, default None]: fields to expand information. Options: ["rules"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of CorporateHolder objects with updated attributes
    - cursor to retrieve the next page of CorporateHolder objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        ids=ids,
        status=status,
        tags=tags,
        expand=expand,
        user=user,
    )


def update(id, center_id=None, permissions=None, status=None, name=None, rules=None, tags=None, user=None):
    """# Update CorporateHolder entity
    Update a CorporateHolder by passing its id.
    ## Parameters (required):
    - id [string]: CorporateHolder id. ex: '5656565656565656'
    ## Parameters (optional):
    - center_id [string, default None]: target cost center ID. ex: "5656565656565656"
    - permissions [list of Permission object, default None]: list of Permission object representing access granted to an user for a particular cardholder.
    - status [string, default None]: You may block the CorporateHolder by passing 'blocked' in the status
    - name [string, default None]: card holder name.
    - tags [list of strings, default None]: list of strings for tagging
    - rules [list of dictionaries, default None]: list of dictionaries with "amount": int, "currencyCode": string, "id": string, "interval": string, "name": string pairs
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - target CorporateHolder with updated attributes
    """
    payload = {
        "centerId": center_id,
        "permissions": permissions,
        "status": status,
        "name": name,
        "rules": rules,
        "tags": tags,
    }
    return rest.patch_id(resource=_resource, id=id, user=user, payload=payload)


def cancel(id, user=None):
    """# Cancel a CorporateHolder entity
    Cancel a CorporateHolder entity previously created in the Stark Bank API
    ## Parameters (required):
    - id [string]: CorporateHolder unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - canceled CorporateHolder object
    """
    return rest.delete_id(resource=_resource, id=id, user=user)
