from starkbank.utils.base import Base, Post, Get, GetId, Delete


class Webhook(Post, Get, GetId, Delete):

    def __init__(self, url, subscriptions, id=None):
        Base.__init__(self, id=id)

        self.url = url
        self.subscriptions = subscriptions


Webhook._define_known_fields()


create = Webhook._post_single
get = Webhook._get_id
list = Webhook._get
delete = Webhook._delete
