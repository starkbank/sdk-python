from copy import deepcopy
from datetime import date, timedelta
from hashlib import sha256
from random import choice, randint, randrange
from starkbank import TaxPayment, UtilityPayment
from .businesses.businessInfo import randomTaxBusiness, randomUtilityBusiness


example_utility_payment = UtilityPayment(
    bar_code="83660000001084301380074119002551100010601813",
    scheduled="2020-02-29",
    description="loading a random account",
    tags=["test1", "test2", "test3"]
)
example_tax_payment = TaxPayment(
    bar_code="83660000001084301380074119002551100010601813",
    scheduled="2020-02-29",
    description="loading a random account",
    tags=["test1", "test2", "test3"]
)


def replaceBarcode(barcode, replacement, position):
    length = len(replacement)
    return barcode[:position] + replacement + barcode[position + length:]


def generateExampleNonBoletoPaymentsJson(n=1, amount=None, next_day=None, is_tax=False):
    example_payment = example_tax_payment if is_tax else example_utility_payment
    payments = []
    for _ in range(n):
        barcode = example_payment.bar_code
        randomBusiness = randomTaxBusiness() if is_tax else randomUtilityBusiness()
        randomAmount = amount if amount else str(randint(100, 100000)).zfill(11)
        randomTags = [choice(example_payment.tags) for _ in range(randrange(0, 4))]
        barcode = replaceBarcode(
            barcode=barcode,
            replacement=randomBusiness["segment"],
            position=1,
        )
        barcode = replaceBarcode(
            barcode=barcode,
            replacement=randomAmount,
            position=4,
        )
        barcode = replaceBarcode(
            barcode=barcode,
            replacement=randomBusiness["code"].zfill(4),
            position=15,
        )
        payment = deepcopy(example_payment)
        payment.bar_code = barcode
        payment.scheduled = str(date.today() + timedelta(days=1) if next_day else date.today())
        payment.description = sha256(str(randomAmount).encode('utf-8')).hexdigest()
        payment.tags = randomTags
        payments.append(payment)
    return payments
