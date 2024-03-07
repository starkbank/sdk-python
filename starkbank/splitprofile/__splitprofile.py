from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date


class SplitProfile(Resource):
    """# SplitProfile object
    When you create a Split, the entity SplitProfile will be automatically created, if you haven't create a Split yet, you can use the put method to create your SplitProfile.

    ## Parameters (optional):
    - interval [string]: frequency of transfer, default "week". Options: "day", "week", "month"
    - delay [DateInterval or integer]:  how long the amount will stay at the workspace in milliseconds, ex: 604800
    - tags [list of strings, default []]: list of strings for tagging
    ## Attributes (return-only):
    - id [string]: unique id returned when the splitProfile is created. ex: "5656565656565656"
    - status [string]: current splitProfile status. ex: "created"
    - created [datetime.datetime]: creation datetime for the splitProfile. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the splitProfile. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, delay, interval, tags=None, id=None, status=None, created=None, updated=None):
        Resource.__init__(self, id=id)

        self.interval = interval
        self.delay = delay
        self.tags = tags
        self.status = status
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": SplitProfile, "name": "SplitProfile"}


def put(splitProfile, user=None):
    """# Create SplitProfile or update it if you already have it created
    Send a list of SplitProfile objects for creation in the Stark Bank API
    ## Parameters (required):
    - splitProfile [list of SplitProfile objects]: list of SplitProfile objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of SplitProfile objects with updated attributes
    """
    return rest.put_multi(resource=_resource, entities=splitProfile, user=user)


def get(id, user=None):
    """# Retrieve a specific SplitProfile
    Receive a single SplitProfile object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - SplitProfile object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, transaction_ids=None, status=None, tax_id=None, sort=None, tags=None, ids=None, user=None):
    """# Retrieve SplitProfile
    Receive a generator of SplitProfile objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created or updated only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created or updated only before specified date. ex: datetime.date(2020, 3, 10)
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of SplitProfile objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        user=user,
    )


def page(cursor=None, after=None, before=None, tags=None, ids=None, receiver_ids=None, status=None, limit=None, user=None):
    """# Retrieve paged Split Profiles
    Receive a list of up to 100 Split Profiles objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - receiver_ids [list of strings, default None]: list of receiver ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - status [string, default None]: filter for status of retrieved objects. ex: "success"
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of Split objects with updated attributes
    - cursor to retrieve the next page of Split objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        tags=tags,
        ids=ids,
        receiver_ids=receiver_ids,
        status=status,
        user=user,
    )
