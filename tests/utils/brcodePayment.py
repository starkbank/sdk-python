from copy import deepcopy
from datetime import date, timedelta
from hashlib import sha256
import starkbank
from starkbank import BrcodePayment
from .invoice import generateExampleInvoicesJson

example_payment = BrcodePayment(
    brcode="00020126580014br.gov.bcb.pix0136a629532e-7693-4846-852d-1bbff817b5a8520400005303986540510.005802BR5908T'Challa6009Sao Paulo62090505123456304B14A",
    scheduled="2020-02-29",
    description="loading a random account",
    tax_id="20.018.183/0001-80",
)


def generateExampleBrcodePaymentsJson(n=1, next_day=False):
    invoices = generateExampleInvoicesJson(n=n)

    invoices = starkbank.invoice.create(invoices)

    payments = []
    for invoice in invoices:
        payment = deepcopy(example_payment)
        payment.brcode = invoice.brcode
        payment.scheduled = min((date.today() + timedelta(days=1)) if next_day else date.today(), (invoice.due - timedelta(hours=3)).date())
        payment.description = sha256(str(invoice.id).encode('utf-8')).hexdigest()
        payments.append(payment)
    return payments
