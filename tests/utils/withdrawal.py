from random import randint
from starkbank import CorporateWithdrawal


example_withdrawal = CorporateWithdrawal(
    amount=10,
    external_id="123"
)


def generateExampleWithdrawalJson():
    example_withdrawal.external_id = str(randint(1, 999999))
    example_withdrawal.amount = randint(100, 1000)
    example_withdrawal.description = "Example Withdrawal"
    return example_withdrawal
