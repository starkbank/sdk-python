from ..utils import rest
from ..utils.resource import Resource


class Webhook(Resource):

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
