from copy import deepcopy
from random import randint
from hashlib import sha256

from .dateGenerator import randomFutureDate
from tests.utils.examples.messages.messages import exampleBoletosJson
from .taxIdGenerator import generateCpf, generateCnpj

from .names import get_full_name


def generateExampleBoletos(n=1, amount=None):

    boleto = exampleBoletosJson["boletos"][0]
    boletos = []
    for _ in range(n):
        if amount is None:
            amount = randint(5, 100)
        boleto["name"] = get_full_name()
        boleto["amount"] = amount
        boleto["dueDate"] = str(randomFutureDate(days=7))
        boleto["taxId"] = generateCpf() if randint(0, 1) else generateCnpj()
        boleto["tags"] = [sha256(str(amount).encode('utf-8')).hexdigest()]
        boletos.append(deepcopy(boleto))
    return {"boletos": boletos}
