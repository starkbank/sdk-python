from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_datetime_or_date, check_date


class InvoicePullRequest(Resource):
    """# InvoicePullRequest object
    When you initialize an InvoicePullRequest, the entity will not be automatically
    sent to the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    ## Parameters (required):
    - subscription_id [string]: Unique of the InvoicePullSubscription related to the invoice. ex: "5656565656565656"
    - invoice_id [string]: Id of the invoice previously created to be sent for payment. ex: "5656565656565656"
    - due [datetime.datetime or string]: payment scheduled date in UTC ISO format. ex: "2023-10-28T17:59:26.249976+00:00"
    ## Parameters (optional):
    - attempt_type [string, default "default"]: attempt type for the payment. Options: "default", "retry".
    - tags [list of strings, default []]: list of strings for tagging
    - external_id [string, default None]: a string that must be unique among all your InvoicePullRequests. Duplicated external_ids will cause failures. ex: "my-external-id"
    - display_description [string, default None]: Description to be shown to the payer. ex: "Payment for services"
    ## Attributes (return-only):
    - id [string]: unique id returned when InvoicePullRequest is created. ex: "5656565656565656"
    - status [string]: current InvoicePullRequest status. ex: "pending", "scheduled", "success", "failed", "canceled"
    - installment_id [string]: unique id of the installment related to this request. ex: "5656565656565656"
    - created [datetime.datetime]: creation datetime for the InvoicePullRequest. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the InvoicePullRequest. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, subscription_id, invoice_id, due, attempt_type=None, tags=None, external_id=None,
                 display_description=None, id=None, status=None, installment_id=None,
                 created=None, updated=None):
        Resource.__init__(self, id=id)

        self.subscription_id = subscription_id
        self.invoice_id = invoice_id
        self.due = check_datetime_or_date(due)
        self.attempt_type = attempt_type
        self.tags = tags
        self.external_id = external_id
        self.display_description = display_description
        self.status = status
        self.installment_id = installment_id
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": InvoicePullRequest, "name": "InvoicePullRequest"}


def create(requests, user=None):
    """# Create InvoicePullRequests
    Send a list of InvoicePullRequest objects for creation in the Stark Bank API
    ## Parameters (required):
    - requests [list of InvoicePullRequest objects]: list of InvoicePullRequest objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of InvoicePullRequest objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=requests, user=user)


def get(id, user=None):
    """# Retrieve a specific InvoicePullRequest
    Receive a single InvoicePullRequest object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - InvoicePullRequest object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, status=None, invoice_ids=None, subscription_ids=None, external_ids=None, 
          tags=None, ids=None, after=None, before=None, user=None):
    """# Retrieve InvoicePullRequests
    Receive a generator of InvoicePullRequest objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["success", "failed"]
    - invoice_ids [list of strings, default None]: list of Invoice ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - subscription_ids [list of strings, default None]: list of InvoicePullSubscription ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - external_ids [list of strings, default None]: list of external_ids to filter retrieved objects. ex: ["my-external-id-1", "my-external-id-2"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of InvoicePullRequest objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        invoice_ids=invoice_ids,
        subscription_ids=subscription_ids,
        external_ids=external_ids,
        tags=tags,
        ids=ids,
        user=user,
    )


def page(cursor=None, limit=None, status=None, invoice_ids=None, subscription_ids=None, external_ids=None,
         tags=None, ids=None, after=None, before=None, user=None):
    """# Retrieve paged InvoicePullRequests
    Receive a list of up to 100 InvoicePullRequest objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["success", "failed"]
    - invoice_ids [list of strings, default None]: list of Invoice ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - subscription_ids [list of strings, default None]: list of InvoicePullSubscription ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - external_ids [list of strings, default None]: list of external_ids to filter retrieved objects. ex: ["my-external-id-1", "my-external-id-2"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of InvoicePullRequest objects with updated attributes
    - cursor to retrieve the next page of InvoicePullRequest objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        invoice_ids=invoice_ids,
        subscription_ids=subscription_ids,
        external_ids=external_ids,
        tags=tags,
        ids=ids,
        user=user,
    )


def cancel(id, user=None):
    """# Cancel an InvoicePullRequest entity
    Cancel an InvoicePullRequest entity previously created in the Stark Bank API
    ## Parameters (required):
    - id [string]: InvoicePullRequest unique id. ex: '5656565656565656'
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - canceled InvoicePullRequest object
    """
    return rest.delete_id(resource=_resource, id=id, user=user) 