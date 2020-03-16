from ..utils import rest
from ..utils.resource import Resource


class Webhook(Resource):
    """Description: Webhook subscription object

    A Webhook is used to subscribe to receive notification events on
    a user-selected endpoint for the specified list of services.
    Currently available services for subscription are transfer,
    charge and charge-payment

    Parameters (required):
        url [string]: Webhook subcriptionPayment entity to which the log refers to.
        subscriptions [list of strings]: list of any non-empty combination of the available services. ex: ["transfer", "boleto-payment"]
    Attributes:
        id [string, default None]: unique id returned when log is created. ex: "5656565656565656"
    """

    def __init__(self, url, subscriptions, id=None):
        Resource.__init__(self, id=id)

        self.url = url
        self.subscriptions = subscriptions


def create(url, subscriptions, user=None):
    """Create Webhook subscription

    Send a single Webhook subscription for creation in the Stark Bank API

    Parameters (required):
        url [string]: user endpoint to which notification events will be sent to. ex: "https://webhook.site/60e9c18e-4b5c-4369-bda1-ab5fcd8e1b29"
        subscriptions [list of strings]: list of any non-empty combination of the available services. ex: ["transfer", "boleto-payment"]
    Parameters (optional):
        user [Project object]: optional Project object. Not necessary if starkbank.user was set before function call
    Return
        Webhook object with updated return-only attributes
    """
    return rest.post_single(resource=Webhook, entity=Webhook(url=url, subscriptions=subscriptions), user=user)


def get(id, user=None):
    """Retrieve a single Webhook subscription

    Receive a single Webhook subscription object previously created in the Stark Bank API by passing its id

    Parameters (required):
        id [string]: object unique id. ex: "5656565656565656"
    Parameters (optional):
        user [Project object]: optional Project object. Not necessary if starkbank.user was set before function call
    Return
        Webhook object with updated return-only attributes
    """
    return rest.get_id(resource=Webhook, id=id, user=user)


def query(limit=None, user=None):
    """Retrieve Webhook subcriptions

    Receive a generator of Webhook subcription objects previously created in the Stark Bank API

    Parameters (optional):
        limit [integer, default None]: optional number of objects to be retrieved. Unlimited if None. ex: 35
        user [Project object, default None]: optional Project object. Not necessary if starkbank.user was set before function call
    Return
        generator of Webhook objects with updated return-only attributes
    """
    return rest.get_list(resource=Webhook, limit=limit, user=user)


def delete(ids, user=None):
    """Delete list of Webhook subscription entities

    Delete list of Webhook subscription entities previously created in the Stark Bank API

    Parameters (required):
        ids [list of strings]: list of object unique ids. ex: ["5656565656565656", "4545454545454545"]
    Parameters (optional):
        user [Project object]: optional Project object. Not necessary if starkbank.user was set before function call
    Return
        list of deleted objects with updated return-only attributes
    """
    return rest.delete_list(resource=Webhook, ids=ids, user=user)
