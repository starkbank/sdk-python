# coding: utf-8
from copy import deepcopy
from random import randint
from datetime import timedelta, datetime
from starkbank import Invoice
from .names.names import get_full_name
from .taxIdGenerator import TaxIdGenerator
from .date import randomDatetimeBetween, randomFutureDatetime


example_invoice = Invoice(
    amount=400000,
    due=(datetime.now() + timedelta(days=3)).date(),
    tax_id="012.345.678-90",
    name="Iron Bank S.A.",
    expiration=123456789,
    fine=2.5,
    interest=1.3,
    discounts=[
        {
            "percentage": 10,
            "due": (datetime.now() + timedelta(days=1)).date()
        }
    ],
    tags=[
        "War supply",
        "Invoice #1234"
    ],
    descriptions=[
        {
            "key": "Field1",
            "value": "Something"
        }
    ],
)


def generateExampleInvoicesJson(n=1, amount=None, useRandomFutureDueDate=True, immediate=True):
    invoices = []
    for _ in range(n):
        if amount is None:
            invoiceAmount = randint(205, 300)
        else:
            invoiceAmount = int(amount)
        example_invoice.name = get_full_name()
        example_invoice.amount = invoiceAmount
        if useRandomFutureDueDate:
            example_invoice.due = randomFutureDatetime(days=200)
            for discount in example_invoice.discounts:
                discount["due"] = randomDatetimeBetween(datetime.now() + timedelta(seconds=300), example_invoice.due)
                if not immediate:
                    discount["due"] = discount["due"].date()
            if not immediate:
                example_invoice.due = example_invoice.due.date()
        example_invoice.tax_id = TaxIdGenerator.taxId()
        invoices.append(deepcopy(example_invoice))
    return invoices
