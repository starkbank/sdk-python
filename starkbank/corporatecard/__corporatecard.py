from starkcore.utils.api import endpoint, last_name, from_api_json, api_json
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_date, check_datetime
from ..utils import rest
from ..corporaterule import parse_rules


class CorporateCard(Resource):
    """# CorporateCard object
    The CorporateCard object displays the information of the cards created in your Workspace.
    Sensitive information will only be returned when the "expand" parameter is used, to avoid security concerns.
    When you initialize a CorporateCard, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the created object.
    ## Parameters (required):
    - holder_id [string]: card holder unique id. ex: "5656565656565656"
    ## Attributes (return-only):
    - id [string]: unique id returned when CorporateCard is created. ex: "5656565656565656"
    - holder_name [string]: card holder name. ex: "Tony Stark"
    - display_name [string]: card displayed name. ex: "ANTHONY STARK"
    - rules [list of CorporateRule objects]: [EXPANDABLE] list of card spending rules.
    - tags [list of strings]: list of strings for tagging. ex: ["travel", "food"]
    - street_line_1 [string, default sub-issuer street line 1]: card holder main address. ex: "Av. Paulista, 200"
    - street_line_2 [string, default sub-issuer street line 2]: card holder address complement. ex: "Apto. 123"
    - district [string, default sub-issuer district]: card holder address district/neighbourhood. ex: "Bela Vista"
    - city [string, default sub-issuer city]: card holder address city. ex: "Rio de Janeiro"
    - state_code [string, default sub-issuer state code]: card holder address state. ex: "GO"
    - zip_code [string, default sub-issuer zip code]: card holder address zip code. ex: "01311-200"
    - type [string]: card type. ex: "virtual"
    - status [string]: current CorporateCard status. ex: "active", "blocked", "canceled", "expired"
    - number [string]: [EXPANDABLE] masked card number. Expand to unmask the value. ex: "123"
    - security_code [string]: [EXPANDABLE] masked card verification value (cvv). Expand to unmask the value. ex: "123"
    - expiration [datetime.datetime]: [EXPANDABLE] masked card expiration datetime. Expand to unmask the value. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the CorporateCard. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime]: creation datetime for the CorporateCard. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, holder_id, id=None, holder_name=None, display_name=None, rules=None, tags=None, street_line_1=None,
                 street_line_2=None, district=None, city=None, state_code=None, zip_code=None, type=None,
                 status=None, number=None, security_code=None, expiration=None, updated=None, created=None
        ):
        Resource.__init__(self, id=id)

        self.holder_id = holder_id
        self.holder_name = holder_name
        self.display_name = display_name
        self.rules = parse_rules(rules)
        self.tags = tags
        self.street_line_1 = street_line_1
        self.street_line_2 = street_line_2
        self.district = district
        self.city = city
        self.state_code = state_code
        self.zip_code = zip_code
        self.type = type
        self.status = status
        self.number = number
        self.security_code = security_code
        self.expiration = check_datetime(expiration)
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": CorporateCard, "name": "CorporateCard"}


def create(card, expand=None, user=None):
    """# Create CorporateCard
    Send a CorporateCard object for creation at the Stark Bank API
    If the CorporateCard was not used in the last purchase, this resource will return it.
    ## Parameters (required):
    - card [CorporateCard object]: CorporateCard object to be created in the API.
    ## Parameters (optional):
    - expand [list of strings, default None]: fields to expand information. ex: ["rules", "security_code", "number", "expiration"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - CorporateCard object with updated attributes
    """
    path = "{endpoint}/{sub_resource}".format(endpoint=endpoint(_resource), sub_resource="token")
    json = rest.post_raw(path=path, payload=api_json(card), query={"expand": expand}, user=user).json()
    return from_api_json(_resource, json[last_name(_resource)])


def query(limit=None, after=None, before=None, status=None, types=None, holder_ids=None, ids=None, tags=None,
          expand=None, user=None):
    """# Retrieve CorporateCards
    Receive a generator of CorporateCard objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["active", "blocked", "canceled", "expired"]
    - types [list of strings, default None]: card type. ex: ["virtual"]
    - holder_ids [list of strings, default None]: card holder IDs. ex: ["5656565656565656", "4545454545454545"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - expand [list of strings, default None]: fields to expand information. ex: ["rules", "security_code", "number", "expiration"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - generator of CorporateCard objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        types=types,
        holder_ids=holder_ids,
        ids=ids,
        tags=tags,
        expand=expand,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, status=None, types=None, holder_ids=None, ids=None,
         tags=None, expand=None, user=None):
    """# Retrieve paged CorporateCards
    Receive a list of up to 100 CorporateCard objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. Max = 100. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["active", "blocked", "canceled", "expired"]
    - types [list of strings, default None]: card type. ex: ["virtual"]
    - holder_ids [list of strings, default None]: card holder IDs. ex: ["5656565656565656", "4545454545454545"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - expand [list of strings, default None]: fields to expand information. ex: ["rules", "security_code", "number", "expiration"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - list of CorporateCard objects with updated attributes
    - cursor to retrieve the next page of CorporateCard objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        types=types,
        holder_ids=holder_ids,
        ids=ids,
        tags=tags,
        expand=expand,
        user=user,
    )


def get(id, expand=None, user=None):
    """# Retrieve a specific CorporateCard
    Receive a single CorporateCard object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - expand [list of strings, default None]: fields to expand information. ex: ["rules", "security_code", "number", "expiration"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - CorporateCard object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, expand=expand, user=user)


def update(id, status=None, display_name=None, rules=None, tags=None, pin=None, user=None):
    """# Update a CorporateCard entity
    Update a CorporateCard by passing id.
    ## Parameters (required):
    - id [string]: CorporateCard id. ex: '5656565656565656'
    ## Parameters (optional):
    - status [string, default None]: You may block the CorporateCard by passing 'blocked' or activate by passing 'active' in the status
    - display_name [string, default None]: card displayed name. ex: "ANTHONY EDWARD"
    - pin [string, default None]: You may unlock your physical card by passing its PIN. This is also the PIN you use to authorize a purhcase.
    - rules [list of CorporateRule objects, default None]: list of dictionaries with "amount": int, "currencyCode": string, "id": string, "interval": string, "name": string pairs.
    - tags [list of strings]: list of strings for tagging. ex: ["tony", "stark"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - target CorporateCard with updated attributes
    """
    payload = {
        "status": status,
        "display_name": display_name,
        "pin": pin,
        "rules": [api_json(rule) for rule in rules] if rules else None,
        "tags": tags,
    }
    return rest.patch_id(resource=_resource, id=id, user=user, payload=payload)


def cancel(id, user=None):
    """# Cancel a CorporateCard entity
    Cancel a CorporateCard entity previously created in the Stark Bank API
    ## Parameters (required):
    - id [string]: CorporateCard unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - canceled CorporateCard object
    """
    return rest.delete_id(resource=_resource, id=id, user=user)
