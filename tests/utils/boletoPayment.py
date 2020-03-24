from copy import deepcopy
from datetime import date
from hashlib import sha256
import starkbank
from starkbank import BoletoPayment
from .boleto import generateExampleBoletosJson


example_payment = BoletoPayment(
    line="34191.09008 61713.957308 71444.640008 2 83430000984732",
    scheduled="2020-02-29",
    description="loading a random account",
    tax_id="20.018.183/0001-80",
)


def generateExampleBoletoPaymentsJson(n=1):
    boletos = generateExampleBoletosJson(n=n)

    boletos = starkbank.boleto.create(boletos)

    lines = [boleto.line for boleto in boletos]
    ids = [boleto.id for boleto in boletos]

    payments = []
    for id, line in zip(ids, lines):
        payment = deepcopy(example_payment)
        payment.line = line
        payment.scheduled = str(date.today())
        payment.description = sha256(str(id).encode('utf-8')).hexdigest()
        payments.append(payment)
    return payments
