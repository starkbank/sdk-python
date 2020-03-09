from starkbank import request
from starkbank.utils.base import Base
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_user


class Webhook(Base):
    _known_fields = {
        "id",
        "url",
        "subscriptions",
    }
    _known_camel_fields = {snake_to_camel(field) for field in _known_fields}

    def __init__(self, url, subscriptions, id=None):
        Base.__init__(self, id=id)

        self.url = url
        self.subscriptions = subscriptions


def create(webhook, user=None):
    response = request.post(
        user=check_user(user),
        endpoint="webhook",
        body={snake_to_camel(k): v for k, v in webhook.json().items() if v is not None}
    )

    return Webhook.from_json(response["webhook"])


def retrieve(id, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="webhook/{id}".format(id=id),
    )

    return Webhook.from_json(response["webhook"])


def list(limit=100, cursor=None, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="webhook",
        url_params={
            "limit": limit,
            "cursor": cursor,
        },
    )

    return [Webhook.from_json(transfer) for transfer in response["webhooks"]], response["cursor"]


def delete(ids, user=None):
    if len(ids) > 100:
        raise ValueError("ids cannot have more than 100 elements")

    webhooks = []
    for id in ids:
        response = request.delete(
            user=check_user(user),
            endpoint="webhook/{id}".format(id=id),
        )

        webhooks.append(Webhook.from_json(response["webhook"]))

    return webhooks
