from starkbank.utils.request import route, get


def getBoletoLog(user, params=None):
    url = route(f"/boleto/log")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def getBoletoLogInfo(user, logId, params=None):
    url = route(f"/boleto/log/{logId}")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)