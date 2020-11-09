import starkbank
from datetime import datetime, timedelta
from unittest import TestCase, main
from tests.utils.invoice import generateExampleInvoicesJson
from tests.utils.date import randomPastDate
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestInvoicePost(TestCase):

    def test_success(self):
        invoices = generateExampleInvoicesJson(n=1)
        invoices = starkbank.invoice.create(invoices)
        for invoice in invoices:
            self.assertIsNotNone(invoice.id)
            print(invoice)


class TestInvoiceGet(TestCase):

    def test_success_after_before(self):
        after = randomPastDate(days=10)
        before = datetime.today()
        invoices = starkbank.invoice.query(after=after.date(), before=before.date())
        i = 0
        for i, invoice in enumerate(invoices):
            self.assertTrue(after.date() <= invoice.created.date() <= (before + timedelta(hours=3)).date())
            if i >= 200:
                break
        print("Number of invoices:", i)


class TestInvoiceInfoGet(TestCase):

    def test_success(self):
        invoices = starkbank.invoice.query(limit=10)
        for invoice in invoices:
            invoice_id = invoice.id
            invoice = starkbank.invoice.get(invoice_id)
            self.assertEqual(invoice.id, invoice_id)

class TestInvoiceInfoPatch(TestCase):
    
    def test_success_cancel(self):
        invoices = starkbank.invoice.query(status="created", limit=1)
        for invoice in invoices:
            self.assertIsNotNone(invoice.id)
            self.assertEqual(invoice.status, "created")
            updated_invoice = starkbank.invoice.update(invoice.id, status="canceled")
            self.assertEqual(updated_invoice.status, "canceled")

    def test_success_amount(self):
        invoices = starkbank.invoice.query(status="created", limit=1)
        invoice_amount = 4321
        for invoice in invoices:
            self.assertIsNotNone(invoice.id)
            updated_invoice = starkbank.invoice.update(
                invoice.id,
                amount=invoice_amount,
                due=datetime.utcnow() + timedelta(hours=1),
                expiration=timedelta(hours=2),
            )
            print(updated_invoice)
            self.assertEqual(updated_invoice.amount, invoice_amount)


class TestInvoiceQrcodeGet(TestCase):

    def test_success(self):
        invoices = starkbank.invoice.query()
        invoice_id = next(invoices).id
        qrcode = starkbank.invoice.qrcode(invoice_id)
        self.assertGreater(len(qrcode), 1000)
        default_qrcode = starkbank.invoice.qrcode(invoice_id)
        self.assertGreater(len(default_qrcode), 1000)
        big_qrcode = starkbank.invoice.qrcode(invoice_id, size=25)
        self.assertGreater(len(big_qrcode), 1000)


if __name__ == '__main__':
    main()
