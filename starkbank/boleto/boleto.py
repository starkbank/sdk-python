from json import dumps

from starkbank.utils.request import route, post, get, delete


def postBoleto(user, boletosJson):
    url = route(f"/boleto")
    payload = dumps(boletosJson)
    headers = user.getHeaders(message=payload)
    return post(url, headers=headers, payload=payload)


def getBoleto(user, params=None):
    url = route(f"/boleto")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def deleteBoleto(user, boletoId):
    url = route(f"/boleto/{boletoId}")
    headers = user.getHeaders()
    return delete(url, headers=headers)


def getBoletoInfo(user, boletoId, params=None):
    url = route(f"/boleto/{boletoId}")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def getBoletoPdf(user, boletoId, params=None):
    url = route(f"/boleto/{boletoId}/pdf")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)