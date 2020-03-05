from json import dumps

from starkbank.utils.old_request import route, post, get, delete


def postSession(user, publicKeyString, platform="api", duration=3600):
    url = route(f"/session")
    payload = dumps({
        "platform": platform,
        "expiration": duration,
        "publicKey": publicKeyString,
    })
    headers = user.getHeaders(message=payload)
    return post(url, headers=headers, payload=payload)


def getSession(user, params=None):
    url = route(f"/session")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def getSessionInfo(user, sessionId, params=None):
    url = route(f"/session/{sessionId}")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def deleteSession(user, sessionId):
    url = route(f"/session/{sessionId}")
    headers = user.getHeaders()
    return delete(url, headers=headers)
