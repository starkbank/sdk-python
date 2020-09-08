from copy import deepcopy
from random import randint
from uuid import uuid4
from starkbank import Transaction


example_transaction = Transaction(
    amount=50,
    receiver_id="12345",
    external_id="unique identifier",
    description="Transferencia para Workspace aleatorio",
)


def generateExampleTransactionsJson(n=1):
    transactions = []
    for _ in range(n):
        amount = randint(1, 10)
        transaction = deepcopy(example_transaction)
        transaction.receiver_id = "5768064935133184"
        transaction.amount = amount
        transaction.external_id = str(uuid4())
        transactions.append(transaction)
    return transactions
