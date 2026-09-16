from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_date, check_datetime, check_datetime_or_date

class MerchantCard(Resource):
    """# MerchantCard object
    Stores information about a card used in an approved purchase, so it can be reused in new purchases without a new MerchantSession.
    ## Attributes (return-only):
    - id, ending, funding_type, holder_name, network [string]
    - status [string]: current status. ex: "active", "expired", "canceled" or "blocked"
    - tags [list of strings]
    - expiration, created, updated [datetime]
    """

    def __init__(self, id=None, ending=None , funding_type=None, holder_name=None, network=None, status=None, tags=None,
                 expiration=None, created=None, updated=None):
        Resource.__init__(self, id=id)
        self.ending = ending
        self.funding_type = funding_type
        self.holder_name = holder_name
        self.network = network
        self.status = status
        self.tags = tags
        self.expiration = check_datetime_or_date(expiration)
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": MerchantCard, "name": "MerchantCard"}


def get(id, user=None):
    """# Retrieve a specific MerchantCard
    Receive a single MerchantCard object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - MerchantCard object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, status=None, tags=None, ids=None, user=None):
    """# Retrieve MerchantCards
    Receive a generator of MerchantCard objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "active"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of MerchantCard objects with updated attributes
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
    """# Retrieve paged MerchantCards
    Receive a list of up to 100 MerchantCard objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "active"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of MerchantCard objects with updated attributes
    - cursor to retrieve the next page of MerchantCard objects
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
