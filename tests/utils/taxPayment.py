from starkbank import TaxPayment
from .nonBoletoPayment import generateExampleNonBoletoPaymentsJson

example_payment = TaxPayment(
    bar_code="83660000001084301380074119002551100010601813",
    scheduled="2020-03-29",
    description="pagando a conta",
)


def generateExampleTaxPaymentsJson(n=1, amount=None, next_day=False):
    return generateExampleNonBoletoPaymentsJson(
        n=n,
        amount=amount,
        next_day=next_day,
        is_tax=True,
    )
