from json import dumps

from starkbank.utils.old_request import route, post, get


def postBoletoPayment(user, paymentsJson):
    url = route(f"/boleto-payment")
    payload = dumps(paymentsJson)
    headers = user.getHeaders(message=payload)
    return post(url, headers=headers, payload=payload)


def getBoletoPayment(user, params=None):
    url = route(f"/boleto-payment")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def getBoletoPaymentInfo(user, paymentId, params=None):
    url = route(f"/boleto-payment/{paymentId}")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)


def getBoletoPaymentPdf(user, paymentId, params=None):
    url = route(f"/boleto-payment/{paymentId}/pdf")
    headers = user.getHeaders()
    return get(url, headers=headers, params=params)