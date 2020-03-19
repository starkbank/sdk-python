from copy import deepcopy
from hashlib import sha256
from random import randint

from starkbank import Boleto
from starkbank.utils.api import from_api_json
from tests.utils.examples.messages.messages import exampleBoletosJson
from .dateGenerator import randomFutureDate
from .names import get_full_name
from .taxIdGenerator import generateCpf, generateCnpj


def generateExampleBoletosJson(n=1, amount=None):
    exampleBoleto = from_api_json(Boleto, exampleBoletosJson["boletos"][0])
    boletos = []
    for _ in range(n):
        if amount is None:
            boletoAmount = randint(5, 100)
        else:
            boletoAmount = int(amount)
        exampleBoleto.name = get_full_name()
        exampleBoleto.amount = boletoAmount
        exampleBoleto.due = str(randomFutureDate(days=7).date())
        exampleBoleto.tax_id = generateCpf() if randint(0, 1) else generateCnpj()
        boletos.append(deepcopy(exampleBoleto))
    return boletos
