from copy import deepcopy
from random import randint
from starkbank import Transfer
from .names.names import get_full_name
from .taxIdGenerator import generateCpf, generateCnpj


example_transfer = Transfer(
    amount=10,
    name="João",
    tax_id="01234567890",
    bank_code="01",
    branch_code="0001",
    account_number="10000-0"
)


def generateExampleTransfersJson(n=1):
    transfers = []
    for _ in range(n):
        amount = randint(1, 10)
        transfer = deepcopy(example_transfer)
        transfer.name = get_full_name()
        transfer.amount = amount
        transfer.tax_id = generateCpf() if randint(0, 1) else generateCnpj()
        transfers.append(transfer)
    return transfers
