from json import dumps

from starkbank.utils.old_request import route, post, get


def postTransaction(user, transactionJson):
    url = route(f"/transaction")
    payload = dumps(transactionJson)
    headers = user.getHeaders(message=payload)
    return post(url, headers=headers, payload=payload)


def getTransaction(user, params=None):
    url = route(f"/transaction")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def getTransactionInfo(user, transactionId, params=None):
    url = route(f"/transaction/{transactionId}")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)
