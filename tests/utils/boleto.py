from copy import deepcopy
from hashlib import sha256
from random import randint

from starkbank import Boleto
from starkbank.utils.api import from_api_json
from tests.utils.examples.messages.messages import exampleBoletosJsonString
from .dateGenerator import randomFutureDate
from .names import get_full_name
from .taxIdGenerator import generateCpf, generateCnpj


def generateExampleBoletosJson(n=1, amount=None):
    exampleBoleto = from_api_json(Boleto, exampleBoletosJsonString["boletos"][0])
    boletos = []
    for _ in range(n):
        if amount is None:
            amount = randint(5, 100)
        exampleBoleto.name = get_full_name()
        exampleBoleto.amount = amount
        exampleBoleto.due = str(randomFutureDate(days=7).date())
        exampleBoleto.tax_id = generateCpf() if randint(0, 1) else generateCnpj()
        exampleBoleto.tags = [sha256(str(amount).encode('utf-8')).hexdigest()]
        boletos.append(deepcopy(exampleBoleto))
    return boletos
