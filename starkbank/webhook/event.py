from starkbank.utils.request import route, get


def getEvent(user, params=None):
    url = route(f"/event")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def getEventInfo(user, eventId, params=None):
    url = route(f"/event/{eventId}")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)