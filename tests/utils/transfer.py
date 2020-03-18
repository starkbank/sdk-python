from copy import deepcopy
from hashlib import sha256
from random import randint

from starkbank import Transfer
from starkbank.utils.api import from_api_json
from tests.utils.examples.messages.messages import exampleTransfersJson
from .names import get_full_name
from .taxIdGenerator import generateCpf, generateCnpj


def generateExampleTransfersJson(n=1):
    transfer = from_api_json(Transfer, exampleTransfersJson["transfers"][0])
    transfers = []
    for _ in range(n):
        amount = randint(1, 10)
        transfer.name = get_full_name()
        transfer.amount = amount
        transfer.tax_id = generateCpf() if randint(0, 1) else generateCnpj()
        transfers.append(deepcopy(transfer))
    return transfers
