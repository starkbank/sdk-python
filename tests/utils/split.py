from copy import deepcopy
import starkbank
from starkbank import BrcodePayment
from tests.utils.invoice import generateExampleInvoicesJson

example_payment = BrcodePayment(
    brcode="00020126580014br.gov.bcb.pix0136a629532e-7693-4846-852d-1bbff817b5a8520400005303986540510.005802BR5908T'Challa6009Sao Paulo62090505123456304B14A",
    description="Split test",
    tax_id="20.018.183/0001-80",
)


def generateExampleSplittedInvoices(n=1):
    invoices = generateExampleInvoicesJson(n=n, immediate=True, useSplit=True)

    invoices = starkbank.invoice.create(invoices)

    return invoices


def paySplittedInvoices(invoices):
    payments = []
    for invoice in invoices:
        payment = deepcopy(example_payment)
        payment.brcode = invoice.brcode
        payments.append(payment)
    payments = starkbank.brcodepayment.create(payments)
    return payments
