from copy import deepcopy
from random import randrange
from datetime import datetime
from starkbank import DarfPayment
from .taxIdGenerator import TaxIdGenerator
from .date import randomPastDate, randomFutureDate
from .nonBoletoPayment import generateExampleNonBoletoPaymentsJson


example_darf_payment = DarfPayment(
    revenue_code="1240",
    tax_id="012.345.678-90",
    competence="2020-09-01",
    reference_number="2340978970",
    nominal_amount=1234,
    fine_amount=12,
    interest_amount=34,
    due=randomFutureDate(),
    scheduled="2020-09-08",
    tags=["tag1", "tag2"],
    description=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)


def generateExampleTaxPaymentsJson(n=1, amount=None, next_day=False):
    return generateExampleNonBoletoPaymentsJson(
        n=n,
        amount=amount,
        next_day=next_day,
        is_tax=True,
    )


def generateExampleDarfPaymentsJson(n=1, randomSchedule=False):
    payments = []
    for _ in range(n):
        payment = deepcopy(example_darf_payment)
        payment.revenue_code = str(randrange(0, 9999)).zfill(4)
        payment.nominal_amount = randrange(100, 1000)
        payment.fine_amount = randrange(10, 100)
        payment.interest_amount = randrange(10, 100)
        payment.reference_number = randomPastDate(90).strftime("%m%Y")
        payment.competence = randomPastDate().date()
        payment.tax_id = TaxIdGenerator.taxId()
        payment.scheduled = datetime.today().date()
        if randomSchedule:
            payment.scheduled = randomFutureDate()
        payments.append(payment)
    return payments
