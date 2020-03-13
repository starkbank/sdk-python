from ..utils import rest
from ..utils.resource import Resource


class Webhook(Resource):
    """Description: Webhook subscription object

    A Webhook is used to subscribe to receive notification events on
    a user-selected endpoint for the specified list of services.
    Currently available services for subscription are transfer,
    charge and charge-payment

    Parameters (required):
        url [string]: BoletoPayment entity to which the log refers to.
        subscriptions [list of strings]: list of any non-empty combination of the three available services. ex: ["transfer", "charge"]
    Attributes:
        id [string, default None]: unique id returned when log is created. ex: "5656565656565656"
    """

    def __init__(self, url, subscriptions, id=None):
        Resource.__init__(self, id=id)

        self.url = url
        self.subscriptions = subscriptions


def create(url, subscriptions, user=None):
    return rest.post_single(resource=Webhook, entity=Webhook(url=url, subscriptions=subscriptions), user=user)


def get(id, user=None):
    return rest.get_id(resource=Webhook, id=id, user=user)


def query(limit=None, user=None):
    return rest.get_list(resource=Webhook, limit=limit, user=user)


def delete(ids, user=None):
    return rest.delete_list(resource=Webhook, ids=ids, user=user)
