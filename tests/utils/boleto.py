from starkbank import Boleto
from copy import deepcopy
from random import randint
from hashlib import sha256

from .dateGenerator import randomFutureDate
from tests.utils.examples.messages.messages import exampleBoletosJsonString
from .taxIdGenerator import generateCpf, generateCnpj

from .names import get_full_name


def generateExampleBoletosJsonOld(n=1, amount=None):

    boleto = exampleBoletosJsonString["boletos"][0]
    boletos = []
    for _ in range(n):
        if amount is None:
            amount = randint(5, 100)
        boleto["name"] = get_full_name()
        boleto["amount"] = amount
        boleto["due"] = str(randomFutureDate(days=7))
        boleto["tax_id"] = generateCpf() if randint(0, 1) else generateCnpj()
        boleto["tags"] = [sha256(str(amount).encode('utf-8')).hexdigest()]
        boletos.append(deepcopy(boleto))
    return {"boletos": boletos}


def generateExampleBoletosJson(n=1, amount=None):

    exampleBoleto = Boleto.from_json(exampleBoletosJsonString["boletos"][0])
    boletos = []
    for _ in range(n):
        if amount is None:
            amount = randint(5, 100)
        exampleBoleto.name = get_full_name()
        exampleBoleto.amount = amount
        exampleBoleto.due = str(randomFutureDate(days=7))
        exampleBoleto.tax_id = generateCpf() if randint(0, 1) else generateCnpj()
        exampleBoleto.tags = [sha256(str(amount).encode('utf-8')).hexdigest()]
        boletos.append(deepcopy(exampleBoleto))
    return boletos
