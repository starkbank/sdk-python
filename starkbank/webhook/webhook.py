from starkbank.utils import rest
from starkbank.utils.base import Base


class Webhook(Base):

    def __init__(self, url, subscriptions, id=None):
        Base.__init__(self, id=id)

        self.url = url
        self.subscriptions = subscriptions


Webhook._define_known_fields()


def create(url, subscriptions, user=None):
    webhook = Webhook(url=url, subscriptions=subscriptions)
    return rest.post_single(resource=Webhook, entity=webhook, user=user)


def get(id, user=None):
    return rest.get_id(resource=Webhook, id=id, user=user)


def query(limit=100, user=None):
    return rest.query(resource=Webhook, limit=limit, user=user)


def delete(ids, user=None):
    return rest.delete(resource=Webhook, ids=ids, user=user)
