from random import randint
from starkbank import CorporateInvoice


example_invoice = CorporateInvoice(
    amount=1000,
)


def generateExampleInvoicesJson():
    example_invoice.amount = randint(1, 1000)
    return example_invoice
