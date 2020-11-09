#coding: utf-8
from copy import deepcopy
from datetime import date, timedelta, datetime
from random import randint, choice
from starkbank import Transfer
from .names.names import get_full_name
from .taxIdGenerator import TaxIdGenerator


example_transfer = Transfer(
    amount=10,
    name="João",
    tax_id="01234567890",
    bank_code="01",
    branch_code="0001",
    account_number="10000-0"
)


def generateExampleTransfersJson(n=1, randomSchedule=False):
    transfers = []
    for _ in range(n):
        amount = randint(1, 10)
        transfer = deepcopy(example_transfer)
        transfer.name = get_full_name()
        transfer.amount = amount
        transfer.tax_id = TaxIdGenerator.taxId()
        if randomSchedule:
            transfer.scheduled = choice([date.today(), datetime.utcnow()]) + timedelta(days=randint(0, 10))
        transfers.append(transfer)
    return transfers
