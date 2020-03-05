from starkbank.utils.request import route, get


def getBalance(user, params=None):
    url = route(f"/balance")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)