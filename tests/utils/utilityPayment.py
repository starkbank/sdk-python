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
        examplePayment.line = (str(randint(0, 1.e49 - 1)) + 48 * "0")[:48]
        examplePayment.due = str(randomFutureDate(days=7).date())
        examplePayment.scheduled = examplePayment.due
        examplePayment.tags = [sha256(str(amount).encode('utf-8')).hexdigest()]
        payments.append(deepcopy(examplePayment))
    return payments
