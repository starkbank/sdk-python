from ..utils import rest
from starkcore.utils.resource import Resource


class Webhook(Resource):
    """# Webhook subscription object
    A Webhook is used to subscribe to notification events on a user-selected endpoint.
    Currently, available services for subscription are transfer, boleto, boleto-holmes,
    boleto-payment, brcode-payment, utility-payment, deposit and invoice.
    ## Parameters (required):
    - url [string]: Url that will be notified when an event occurs.
    - subscriptions [list of strings]: list of any non-empty combination of the available services. ex: ["transfer", "invoice", "deposit"]
    ## Attributes (return-only):
    - id [string]: unique id returned when the webhook is created. ex: "5656565656565656"
    """

    def __init__(self, url, subscriptions, id=None):
        Resource.__init__(self, id=id)

        self.url = url
        self.subscriptions = subscriptions


_resource = {"class": Webhook, "name": "Webhook"}


def create(url, subscriptions, user=None):
    """# Create Webhook subscription
    Send a single Webhook subscription for creation in the Stark Bank API
    ## Parameters (required):
    - url [string]: url to which notification events will be sent to. ex: "https://webhook.site/60e9c18e-4b5c-4369-bda1-ab5fcd8e1b29"
    - subscriptions [list of strings]: list of any non-empty combination of the available services. ex: ["transfer", "boleto-payment"]
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Webhook object with updated attributes
    """
    return rest.post_single(resource=_resource, entity=Webhook(url=url, subscriptions=subscriptions), user=user)


def get(id, user=None):
    """# Retrieve a specific Webhook subscription
    Receive a single Webhook subscription object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Webhook object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, user=None):
    """# Retrieve Webhook subscriptions
    Receive a generator of Webhook subscription objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of Webhook objects with updated attributes
    """
    return rest.get_stream(resource=_resource, limit=limit, user=user)


def page(cursor=None, limit=None, user=None):
    """# Retrieve paged Webhook subscriptions
    Receive a list of up to 100 Webhook subscription objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of Webhook objects with updated attributes
    - cursor to retrieve the next page of Webhook objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        user=user,
    )


def delete(id, user=None):
    """# Delete a Webhook subscription entity
    Delete a Webhook subscription entity previously created in the Stark Bank API
    ## Parameters (required):
    - id [string]: Webhook unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - deleted Webhook object
    """
    return rest.delete_id(resource=_resource, id=id, user=user)
