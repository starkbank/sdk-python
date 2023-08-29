#coding: utf-8
from uuid import uuid4
from copy import deepcopy
from datetime import date, timedelta, datetime
from random import randint, choice
from starkbank import Transfer
from starkbank.transfer import Rule
from .names.names import get_full_name
from .taxIdGenerator import TaxIdGenerator


example_transfer = Transfer(
    amount=10,
    name="João",
    tax_id="01234567890",
    bank_code=choice(["18236120", "60701190"]),
    branch_code="0001",
    account_number="10000-0",
    account_type="checking"
)


def generateExampleTransfersJson(n=1, randomSchedule=False):
    transfers = []
    for _ in range(n):
        amount = randint(100000, 1000000)
        transfer = deepcopy(example_transfer)
        transfer.name = get_full_name()
        transfer.amount = amount
        transfer.branch_code = str(randint(1, 999))
        transfer.tax_id = TaxIdGenerator.taxId()
        transfer.account_type = choice(["checking", "savings", "salary", "payment"])
        transfer.account_number = "{}-{}".format(randint(10000, 100000000), randint(0, 9))
        transfer.external_id = str(uuid4())
        transfer.rules = [
            Rule(
                key="resendingLimit",
                value=randint(0, 10)
            )
        ]
        transfer.description = choice([None, "Test description"])
        if randomSchedule:
            transfer.scheduled = choice([date.today(), datetime.utcnow()]) + timedelta(days=randint(0, 10))
        transfers.append(transfer)
    return transfers
