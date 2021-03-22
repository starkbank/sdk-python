from starkbank.utils import rest
from starkbank.utils.resource import Resource
from starkbank.utils.checks import check_datetime, check_date


class Attempt(Resource):
    """# Event.Attempt object
    When an Event delivery fails, an event attempt will be registered.
    It carries information meant to help you debug event reception issues.
    ## Attributes:
    - id [string]: unique id that identifies the delivery attempt. ex: "5656565656565656"
    - code [string]: delivery error code. ex: badHttpStatus, badConnection, timeout
    - message [string]: delivery error full description. ex: "HTTP POST request returned status 404"
    - event_id [string]: ID of the Event whose delivery failed. ex: "4848484848484848"
    - webhook_id [string]: ID of the Webhook that triggered this event. ex: "5656565656565656"
    - created [datetime.datetime]: datetime representing the moment when the attempt was made. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, id, code, message, event_id, webhook_id, created):
        Resource.__init__(self, id=id)

        self.code = code
        self.message = message
        self.webhook_id = webhook_id
        self.event_id = event_id
        self.created = check_datetime(created)


_resource = {"class": Attempt, "name": "EventAttempt"}


def get(id, user=None):
    """# Retrieve a specific event.Attempt
    Receive a single event.Attempt object previously created by the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - event.Attempt object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, event_ids=None, webhook_ids=None, user=None):
    """# Retrieve event.Attempts
    Receive a generator of event.Attempt objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - event_ids [list of strings, default None]: list of Event ids to filter attempts. ex: ["5656565656565656", "4545454545454545"]
    - webhook_ids [list of strings, default None]: list of Webhook ids to filter attempts. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of event.Attempt objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        event_ids=event_ids,
        webhook_ids=webhook_ids,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, event_ids=None, webhook_ids=None, user=None):
    """# Retrieve paged event.Attempts
    Receive a list of up to 100 event.Attempt objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - event_ids [list of strings, default None]: list of Event ids to filter attempts. ex: ["5656565656565656", "4545454545454545"]
    - webhook_ids [list of strings, default None]: list of Webhook ids to filter attempts. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of event.Attempt objects with updated attributes
    - cursor to retrieve the next page of event.Attempt objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        event_ids=event_ids,
        webhook_ids=webhook_ids,
        user=user,
    )
