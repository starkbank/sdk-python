from random import randint
import starkbank


example_withdrawal = starkbank.CorporateWithdrawal(
    amount=10,
    external_id="123"
)


def generateExampleWithdrawalJson():
    example_withdrawal.external_id = str(randint(1, 999999))
    example_withdrawal.amount = randint(100, 1000)
    example_withdrawal.description = "Example Withdrawal"
    return example_withdrawal


def payment_script(balance):
    data = starkbank.CorporateInvoice(amount=balance * -1)
    corporate_invoice = starkbank.corporateinvoice.create(data)
    print(corporate_invoice)
    payload = [starkbank.BrcodePayment(brcode=corporate_invoice.brcode, tax_id="20.018.183/0001-80",
                                       description="paying debts")]
    payments = starkbank.brcodepayment.create(payments=payload)

    return payments
