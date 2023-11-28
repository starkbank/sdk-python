# coding: utf-8
from copy import deepcopy
from random import randint
from datetime import timedelta, datetime
from starkbank import splitreceiver
from starkbank import Invoice, Split
from starkbank.invoice import Rule
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


def generateExampleInvoicesJson(n=1, amount=None, useRandomFutureDueDate=True, useSplit=False, immediate=True):
    invoices = []
    receivers = []
    receivers_length = 0
    if useSplit:
        receivers_length = 2
        receivers = list(splitreceiver.query(limit=receivers_length, tags="sdk-receiver"))
    for _ in range(n):
        if amount is None:
            invoiceAmount = randint(205, 300)
        else:
            invoiceAmount = int(amount)
        example_invoice.name = get_full_name()
        example_invoice.amount = invoiceAmount
        example_invoice.rules = [
            Rule(
                key="allowedTaxIds",
                value=[ "012.345.678-90" ]
            )
        ]
        if useRandomFutureDueDate:
            example_invoice.due = randomFutureDatetime(days=200)
            for discount in example_invoice.discounts:
                discount["due"] = randomDatetimeBetween(datetime.now() + timedelta(seconds=300), example_invoice.due)
                if not immediate:
                    discount["due"] = discount["due"].date()
            if not immediate:
                example_invoice.due = example_invoice.due.date()
        if useSplit:
            example_invoice.rules = None
            example_invoice.discounts = []
            amount_steps = sorted([0] + [randint(0, example_invoice.amount - receivers_length) for _ in receivers])
            receiver_amounts = [amount_steps[i+1] - amount_steps[i] + 1 for i in range(len(receivers))]
            example_invoice.splits = [
                Split(amount=receiver_amount, receiver_id=receiver.id)
                for receiver, receiver_amount in zip(receivers, receiver_amounts)
            ]
        example_invoice.tax_id = TaxIdGenerator.taxId()
        invoices.append(deepcopy(example_invoice))
    return invoices
