from json import dumps

from starkbank.utils.old_request import get, route, delete, post


def postProject(user, name, publicKeyString, platform="api", duration=3600, allowedIps=None):
    url = route(f"/project")
    payload = dumps({
        "platform": platform,
        "name": name,
        "expiration": duration,
        "publicKey": publicKeyString,
        "allowedIps": allowedIps
    })
    headers = user.getHeaders(message=payload)
    return post(url, headers=headers, payload=payload)


def getProject(user, params=None):
    url = route(f"/project")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def getProjectInfo(user, projectId, params=None):
    url = route(f"/project/{projectId}")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def deleteProject(user, projectId):
    url = route(f"/project/{projectId}")
    headers = user.getHeaders()
    return delete(url, headers=headers)
