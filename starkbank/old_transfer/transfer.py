from json import dumps

from starkbank.utils.old_request import route, post, get


def postTransfer(user, transfersJson):
    url = route(f"/transfer")
    payload = dumps(transfersJson)
    headers = user.getHeaders(message=payload)
    return post(url, headers=headers, payload=payload)


def getTransfer(user, params=None):
    url = route(f"/transfer")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def deleteTransfer(user, transferId):
    raise NotImplementedError
    # url = apiUrl(f"/transfer/{transferId}")
    # headers = user.getHeaders()
    # return delete(url, headers=headers)


def getTransferInfo(user, transferId, params=None):
    url = route(f"/transfer/{transferId}")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def getTransferPdf(user, transferId, params=None):
    url = route(f"/transfer/{transferId}/pdf")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)