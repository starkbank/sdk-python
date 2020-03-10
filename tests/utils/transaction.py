from copy import deepcopy
from random import randint
from hashlib import sha256
from uuid import uuid4
from starkbank import Transaction
from starkbank.utils.api import from_api_json
from tests.utils.examples.messages.messages import exampleTransactionsJson


def generateExampleTransactions(n=1):
    transaction = from_api_json(Transaction, exampleTransactionsJson["transactions"][0])
    transactions = []
    for _ in range(n):
        amount = randint(1, 10)
        transaction.receiver_id = "5168326472892416"
        transaction.sender_id = "5647143184367616"
        transaction.amount = amount
        transaction.external_id = str(uuid4())
        transaction.tags = [sha256(str(amount).encode('utf-8')).hexdigest()]
        transactions.append(deepcopy(transaction))
    return transactions
