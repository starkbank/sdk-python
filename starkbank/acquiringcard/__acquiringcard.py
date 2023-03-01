from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_date


class AcquiringCard(Resource):
    """# AcquiringCard object
    An AcquiringCard object represents a card for acquiring payments through the Stark Bank API.
    When you initialize an AcquiringCard, the entity will not be automatically sent to the API.
    The 'create' function sends the objects to the API and returns a list of created objects.
    ## Parameters (required):
    - number [string]: AcquiringCard number. Ex: "5117 7230 3325 8118"
    - expiration [string]: AcquiringCard expiration date. Ex: "2028-02"
    - security_code [string]: AcquiringCard security code. Ex: "406"
    - zip_code [string]: AcquiringCard zip code. Ex: "57304-160"
    ## Parameters (optional):
    - tags [list of strings, default None]: list of strings for tagging. Ex: ["stark", "bank"]
    - metadata [string, default None]: free parameter for user-defined purposes
    ## Attributes (return-only):
    - id [string, default None]: unique id returned when an AcquiringCard is created. Ex: "5656565656565656"
    - created [datetime.datetime, default None]: AcquiringCard creation datetime. Ex: datetime.datetime(2023, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime, default None]: AcquiringCard's latest update. Ex: datetime.datetime(2023, 3, 10, 10, 30, 0, 0)
    - status [string, default None]: AcquiringCard status. Options: "active", "expired", "canceled", "blocked"
    - holder_type [string]: AcquiringCard holder type. Options: "business", "individual"
    - funding_type [string]: AcquiringCard funding type. Options: "credit", "debit"
    - network [string]: AcquiringCard network. Ex: "mastercard", "visa"
    - ending [string]: last 4 digits of the AcquiringCard number. Ex: "5127"
    - country_code [string]: AcquiringCard country code. Ex: "BRA"
    - product_id [string]: AcquiringCard product ID to which the card is bound. Ex: "53810200"
    - product_code [string]: AcquiringCard product code. Options: "MRW", "MCO", "MWB", "MCS"
    - product_type [string]: AcquiringCard product type. Options: "prepaid", "credit", "debit"
    """

    def __init__(self, number, expiration, security_code, zip_code, tags=None, metadata=None):
        Resource.__init__(self, id=id)

        self.number = number
        self.expiration = expiration
        self.security_code = security_code
        self.zip_code = zip_code
        self.tags = tags
        self.metadata = metadata


_resource = {"class": AcquiringCard, "name": "AcquiringCard"}


def create(cards, expand=None, user=None):
    """# Create AcquiringCards
    Send a list of AcquiringCard objects for creation in the Stark Bank API
    ## Parameters (required):
    - cards [list of AcquiringCard objects]: list of AcquiringCard objects to be created in the API
    ## Parameters (optional):
    - expand [list of strings, default []]: fields to expand information on. Options: ["security_code", "number", "expiration"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - list of AcquiringCard objects
    """
    return rest.post_multi(resource=_resource, entities=cards, expand=expand, user=user)


def query(limit=None, ids=None, after=None, before=None, status=None, holder_types=None, funding_types=None, tags=None,
          expand=None, user=None):
    """# Retrieve AcquiringCards
    Receive a generator of AcquiringCard objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. Ex: 35
    - ids [list of strings, default None]: list of ids to filter retrieved objects. Ex: ["5656565656565656", "4545454545454545"]
    - after [datetime.date or string, default None] filter for objects created only after the specified date. Ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] filter for objects created only before the specified date. Ex: datetime.date(2023, 2, 19)
    - status [list of strings, default None]: filter for status of retrieved objects. Options: ["active", "expired", "canceled", "blocked"]
    - holder_types [list of strings, default None]: filter for holder type. Options: ["business", "individual"]
    - funding_types [list of strings, default None]: filter for funding type. Options: ["credit", "debit"]
    - tags [list of strings, default None]: filter for tags. Ex: ["tony", "stark"]
    - expand [list of strings, default []]: fields to expand information on. Options: ["security_code", "number", "expiration"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - generator of AcquiringCard objects
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        ids=ids,
        after=check_date(after),
        before=check_date(before),
        status=status,
        holder_types=holder_types,
        funding_types=funding_types,
        tags=tags,
        expand=expand,
        user=user,
    )


def page(cursor=None, limit=None, ids=None, after=None, before=None, status=None, holder_types=None, funding_types=None,
         tags=None, expand=None, user=None):
    """# Retrieve paged AcquiringCards
    Receive a paged list of AcquiringCard objects previously created in the Stark Bank API and the cursor to the next page.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. Max = 100. Ex: 35
    - ids [list of strings, default None]: list of ids to filter retrieved objects. Ex: ["5656565656565656", "4545454545454545"]
    - after [datetime.date or string, default None] date filter for objects created only after specified date. Ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. Ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. Options: ["active", "expired", "canceled", "blocked"]
    - holder_types [list of strings, default None]: filter for holder type. Options: ["business", "individual"]
    - funding_types [list of strings, default None]: filter for funding type. Options: ["credit", "debit"]
    - tags [list of strings, default None]: tags to filter retrieved objects. Ex: ["tony", "stark"]
    - expand [list of strings, default []]: fields to expand information. Options: ["security_code", "number", "expiration"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - list of AcquiringCard objects
    - cursor to retrieve the next page of AcquiringCard objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        ids=ids,
        after=check_date(after),
        before=check_date(before),
        status=status,
        holder_types=holder_types,
        funding_types=funding_types,
        tags=tags,
        expand=expand,
        user=user,
    )


def get(id, expand=None, user=None):
    """# Retrieve a specific AcquiringCard
    Receive a single AcquiringCard object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. Ex: "5656565656565656"
    ## Parameters (optional):
    - expand [list of strings, default None]: fields to expand information. Options: ["security_code", "number", "expiration"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - AcquiringCard object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, expand=expand, user=user)


def update(id, status=None, tags=None, user=None):
    """# Update AcquiringCard entity
    Update, block or activate an AcquiringCard through its id.
    ## Parameters (required):
    - id [string]: AcquiringCard id. Ex: '5656565656565656'
    ## Parameters (optional):
    - status [string, default None]: AcquiringCard status. Options: ["active", "blocked"]
    - tags [list of strings]: list of strings for tagging
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - target AcquiringCard with updated attributes
    """
    payload = {
        "tags": tags,
        "status": status,
    }
    return rest.patch_id(resource=_resource, id=id, user=user, payload=payload)
