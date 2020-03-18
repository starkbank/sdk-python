from copy import deepcopy
from hashlib import sha256
from random import randint

import starkbank
from starkbank import UtilityPayment
from starkbank.utils.api import from_api_json
from .dateGenerator import randomFutureDate
from .examples.messages.messages import exampleUtilityPaymentsJson
from .user import exampleProject

starkbank.user = exampleProject


def generateExampleUtilityPaymentsJson(n=1, amount=None):
    examplePayment = from_api_json(UtilityPayment, exampleUtilityPaymentsJson["payments"][0])
    payments = []
    for _ in range(n):
        bar_code = "83660000001084301380074119002551100010601813"
        examplePayment.bar_code = bar_code[:4] + str(randint(100, 100000)).zfill(11) + bar_code[15:]
        examplePayment.scheduled = str(randomFutureDate(days=7).date())
        examplePayment.tags = [sha256(str(amount).encode('utf-8')).hexdigest()]
        payments.append(deepcopy(examplePayment))
    return payments
