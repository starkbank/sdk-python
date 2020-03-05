from copy import deepcopy
from random import randint
from hashlib import sha256

from .names import get_full_name

from .taxIdGenerator import generateCpf, generateCnpj

from tests.utils.examples.messages.messages import exampleTransfersJson


def generateExampleTransfers(n=1):
    transfer = exampleTransfersJson["transfers"][0]
    transfers = []
    for _ in range(n):
        amount = randint(1, 10)
        transfer["name"] = get_full_name()
        transfer["amount"] = amount
        transfer["taxId"] = generateCpf() if randint(0, 1) else generateCnpj()
        transfer["tags"] = [sha256(str(amount).encode('utf-8')).hexdigest()]
        transfers.append(deepcopy(transfer))
    return {"transfers": transfers}
