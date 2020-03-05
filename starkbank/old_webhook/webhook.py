from json import dumps

from starkbank.utils.old_request import route, post, get, delete


def postWebhook(user, webhookUrl, subscriptions=None):
    if not subscriptions:
        subscriptions = ["transfer", "boleto", "boleto-payment"]
    url = route(f"/webhook")
    payload = dumps({
        "url": webhookUrl,
        "subscriptions": subscriptions
    })
    headers = user.getHeaders(message=payload)
    return post(url, headers=headers, payload=payload)


def getWebhook(user, params=None):
    url = route(f"/webhook")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def getWebhookInfo(user, webhookId, params=None):
    url = route(f"/webhook/{webhookId}")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def deleteWebhook(user, webhookId):
    url = route(f"/webhook/{webhookId}")
    headers = user.getHeaders()
    return delete(url, headers=headers)
