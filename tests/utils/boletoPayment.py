from copy import deepcopy
from datetime import date
from hashlib import sha256

import starkbank
from starkbank import BoletoPayment
from .boleto import generateExampleBoletosJson
from .examples.messages.messages import exampleBoletoPaymentsJson
from .user import exampleProject

starkbank.user = exampleProject


def generateExampleBoletoPaymentsJson(n=1):
    boletos = generateExampleBoletosJson(n=n)

    boletos = starkbank.boleto.create(boletos)

    lines = [boleto.line for boleto in boletos]
    ids = [boleto.id for boleto in boletos]

    payment = BoletoPayment.from_json(exampleBoletoPaymentsJson["payments"][0])
    payments = []
    for id, line in zip(ids, lines):
        payment.line = line
        payment.scheduled = str(date.today())
        payment.description = sha256(str(id).encode('utf-8')).hexdigest()
        payments.append(deepcopy(payment))
    return payments
