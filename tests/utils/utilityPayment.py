from copy import deepcopy
from hashlib import sha256
from random import randint
from .date import randomFutureDate
from starkbank import UtilityPayment


example_payment = UtilityPayment(
    bar_code="83660000001084301380074119002551100010601813",
    scheduled="2020-03-29",
    description="pagando a conta"
)


def generateExampleUtilityPaymentsJson(n=1, amount=None):
    payments = []
    for _ in range(n):
        bar_code = "83660000001084301380074119002551100010601813"
        payment = deepcopy(example_payment)
        payment.bar_code = bar_code[:4] + str(randint(100, 100000)).zfill(11) + bar_code[15:]
        payment.scheduled = str(randomFutureDate(days=7).date())
        payment.tags = [sha256(str(amount).encode('utf-8')).hexdigest()]
        payments.append(deepcopy(payment))
    return payments
