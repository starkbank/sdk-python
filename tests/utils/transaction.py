from copy import deepcopy
from datetime import datetime
from random import randint
from hashlib import sha256

from tests.utils.examples.messages.messages import exampleTransactionsJson


def generateExampleTransactions(n=1):
    transaction = exampleTransactionsJson["transactions"][0]
    transactions = []
    for _ in range(n):
        amount = randint(1, 10)
        transaction["receiverId"] = "5168326472892416"
        transaction["amount"] = amount
        transaction["externalId"] = str(datetime.now())
        transaction["tags"] = [sha256(str(amount).encode('utf-8')).hexdigest()]
        transactions.append(deepcopy(transaction))
    return {"transactions": transactions}
