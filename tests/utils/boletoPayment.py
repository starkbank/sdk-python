from copy import deepcopy
from datetime import date, timedelta
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


def generateExampleBoletoPaymentsJson(n=1, next_day=False):
    boletos = generateExampleBoletosJson(n=n)

    boletos = starkbank.boleto.create(boletos)

    payments = []
    for boleto in boletos:
        payment = deepcopy(example_payment)
        payment.line = boleto.line
        payment.scheduled = min((date.today() + timedelta(days=1)) if next_day else date.today(), (boleto.due - timedelta(hours=3)).date())
        payment.description = sha256(str(boleto.id).encode('utf-8')).hexdigest()
        payments.append(payment)
    return payments
