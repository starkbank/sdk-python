from starkbank.utils.old_request import route, get


def getBalance(user, params=None):
    url = route(f"/balance")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)