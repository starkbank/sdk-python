from copy import deepcopy
from random import randint
from hashlib import sha256

from starkbank import Transfer
from starkbank.utils.api import from_api_json
from .names import get_full_name

from .taxIdGenerator import generateCpf, generateCnpj

from tests.utils.examples.messages.messages import exampleTransfersJsonString


def generateExampleTransfersJson(n=1):
    transfer = from_api_json(Transfer, exampleTransfersJsonString["transfers"][0])
    transfers = []
    for _ in range(n):
        amount = randint(1, 10)
        transfer.name = get_full_name()
        transfer.amount = amount
        transfer.tax_id = generateCpf() if randint(0, 1) else generateCnpj()
        transfer.tags = [sha256(str(amount).encode('utf-8')).hexdigest()]
        transfers.append(deepcopy(transfer))
    return transfers
