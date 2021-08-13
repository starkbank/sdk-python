import starkbank
from datetime import datetime, date, timedelta
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.invoice import generateExampleInvoicesJson
from tests.utils.date import randomPastDate
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestInvoicePost(TestCase):

    def test_success(self):
        invoices = generateExampleInvoicesJson(n=2, immediate=True) + generateExampleInvoicesJson(n=2, immediate=False)
        invoices = starkbank.invoice.create(invoices)
        for invoice in invoices:
            print(invoice)

    def test_fail_invalid_array_size(self):
        invoices = generateExampleInvoicesJson(n=105)
        with self.assertRaises(InputErrors) as context:
            invoices = starkbank.invoice.create(invoices)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual("invalidJson", error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json(self):
        invoices = {}
        with self.assertRaises(InputErrors) as context:
            invoices = starkbank.invoice.create(invoices)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual("invalidJson", error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json_invoice(self):
        invoices = generateExampleInvoicesJson(n=17)
        invoices[0].amount = None  # Required
        invoices[1].due = None  # Required
        invoices[2].tax_id = None  # Required
        invoices[3].name = None  # Required

        invoices[9].expiration = None  # Optional
        invoices[10].fine = None  # Optional
        invoices[11].interest = None  # Optional
        invoices[12].discounts = None  # Optional
        invoices[13].tags = None  # Optional
        invoices[14].descriptions = None  # Optional

        invoices[16].invalid_parameter = "invalidValue"

        with self.assertRaises(InputErrors) as context:
            invoices = starkbank.invoice.create(invoices)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertIn(error.code, ["invalidJson", "invalidInvoice", "invalidDate", "invalidExpiration", "invalidDiscount"])
        self.assertEqual(5, len(errors))

    def test_fail_invalid_description(self):
        invoices = generateExampleInvoicesJson(n=18)
        invoices[0].descriptions = [{"key": "abc"}]  # Valid (correct)
        invoices[1].descriptions = [{"key": "abc", "value": "abc"}]  # Valid (correct)
        invoices[2].descriptions = None  # Valid (Null)
        invoices[3].descriptions = {}  # Valid (Null)
        invoices[4].descriptions = []  # Valid (Null)
        invoices[5].descriptions = ""  # Valid (Null)
        invoices[6].descriptions = 0  # Valid (Null)
        invoices[7].descriptions = [1]
        invoices[8].descriptions = [{}]
        invoices[9].descriptions = [["abc", 2]]
        invoices[10].descriptions = [{"a": "1"}]
        invoices[11].descriptions = [{"value": 1}]
        invoices[12].descriptions = [{"key": 1, "value": 1}]
        invoices[13].descriptions = [{"key": [], "value": 1}]
        invoices[14].descriptions = [{"key": "abc", "value": []}]
        invoices[15].descriptions = [{"key": "abc", "value": {}}]
        invoices[16].descriptions = [{"key": "abc", "value": "abc"}]
        invoices[17].descriptions = [{"key": "abc", "value": 1, "test": "abc"}]
        with self.assertRaises(InputErrors) as context:
            invoices = starkbank.invoice.create(invoices)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertIn(error.code, ["invalidInvoice", "invalidJson", "invalidDescription"])
        self.assertEqual(13, len(errors))

    def test_fail_invalid_discounts(self):
        invoices = generateExampleInvoicesJson(n=19, useRandomFutureDueDate=False)
        invoices[0].discounts = None  # Valid (correct)
        invoices[1].discounts = []  # Valid (correct)
        invoices[2].discounts = [{"percentage": 3, "due": date.today() + timedelta(days=1)},
                                {"percentage": 5, "due": date.today()},
                                {"percentage": 2.5, "due": date.today() + timedelta(days=2)}]  # Valid (correct)
        invoices[3].discounts = [{"percentage": 5, "due": date.today()},
                                {"percentage": 3, "due": date.today() + timedelta(days=1)},
                                {"percentage": 2.5, "due": date.today() + timedelta(days=2)}]  # Valid (correct)
        invoices[4].discounts = [{"percentage": 5, "due": date.today()},
                                {"percentage": 4, "due": date.today() + timedelta(days=1)},
                                {"percentage": 3, "due": date.today() + timedelta(days=2)},
                                {"percentage": 2, "due": date.today() + timedelta(days=3)},
                                {"percentage": 1, "due": date.today() + timedelta(days=4)},
                                {"percentage": 0.5, "due": date.today() + timedelta(days=5)}]  # too many discounts
        invoices[5].discounts = [{"percentage": 1, "due": date.today()},
                                {"percentage": 3, "due": date.today() + timedelta(days=1)}]  # ascending discount
        invoices[6].discounts = [{"percentage": 3, "due": date.today()},
                                {"percentage": 3, "due": date.today() + timedelta(days=1)}]  # repeated percentage
        invoices[7].discounts = [{"percentage": -1, "due": date.today()}]  # invalid percentage
        invoices[8].discounts = [{"percentage": 0, "due": date.today()}]  # invalid percentage
        invoices[9].discounts = [{"percentage": 110, "due": date.today()}]  # invalid percentage
        invoices[10].discounts = [{"percentage": "wrong", "due": date.today()}]  # invalid percentage
        invoices[11].discounts = [{"percentages": 5, "due": date.today()}]  # invalid argument
        invoices[12].discounts = [{"percentage": 5, "due": date.today(), "wrong": 0}]  # invalid argument
        invoices[13].discounts = [{"date": date.today()}]  # missing percentage
        invoices[14].discounts = [{}]  # missing percentage and date
        invoices[14].discounts = [{"wrong": "wrong"}]  # missing percentage and date
        invoices[15].discounts = [{"percentages": 5}]  # missing date
        invoices[16].discounts = [{"percentage": 5, "due": date.today() - timedelta(days=1)}]  # invalid date
        invoices[17].discounts = [{"percentage": 5, "due": invoices[17].due + timedelta(days=1)}]  # invalid date
        invoices[18].discounts = [{"percentage": 5, "due": "wrong"}]  # invalid date

        with self.assertRaises(InputErrors) as context:
            starkbank.invoice.create(invoices)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertTrue(error.code in ['invalidInvoice', 'invalidDiscount', 'invalidDiscountDate'])
        self.assertEqual(17, len(errors))

    def test_fail_invalid_tax_id(self):
        invoices = generateExampleInvoicesJson(n=5)
        invoices[0].tax_id = "000.000.000-00"
        invoices[1].tax_id = "00.000.000/0000-00"
        invoices[2].tax_id = "abc"
        invoices[3].tax_id = 123
        invoices[4].tax_id = {}
        with self.assertRaises(InputErrors) as context:
            invoices = starkbank.invoice.create(invoices)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidTaxId', error.code)
        self.assertEqual(5, len(errors))

    def test_fail_invalid_amount(self):
        invoices = generateExampleInvoicesJson(n=5)
        invoices[0].amount = "123"
        invoices[1].amount = -5
        invoices[2].amount = 0
        invoices[3].amount = 1000000000000000
        invoices[4].amount = {}
        with self.assertRaises(InputErrors) as context:
            invoices = starkbank.invoice.create(invoices)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidAmount', error.code)
        self.assertEqual(4, len(errors))


class TestInvoiceGet(TestCase):

    def test_success(self):
        invoices = list(starkbank.invoice.query(limit=100))
        print("Number of invoices:", len(invoices))

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
        invoices = starkbank.invoice.query()
        invoice_id = next(invoices).id
        invoice = starkbank.invoice.get(invoice_id)

    def test_fail_invalid_invoice(self):
        invoice_id = "0"
        with self.assertRaises(InputErrors) as context:
            invoice = starkbank.invoice.get(invoice_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidInvoice', error.code)
        self.assertEqual(1, len(errors))


class TestInvoiceInfoPatch(TestCase):

    def test_success_cancel(self):
        invoices = starkbank.invoice.query(status="created")
        invoice_id = next(invoices).id
        invoice = starkbank.invoice.update(invoice_id, status="canceled")

    def test_success_amount(self):
        invoices = starkbank.invoice.query(status="created")
        invoice_id = next(invoices).id
        updated_invoice = starkbank.invoice.update(
            invoice_id,
            amount=100,
            due=datetime.utcnow() + timedelta(hours=1),
            expiration=timedelta(hours=2),
        )
        print(updated_invoice)

    def test_fail_invalid_operation(self):
        invoice_id = "0"
        with self.assertRaises(InputErrors) as context:
            invoice = starkbank.invoice.get(invoice_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidInvoice', error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json(self):
        invoices = starkbank.invoice.query(status="canceled", limit=1)
        invoice_amount = 4321
        for invoice in invoices:
            self.assertIsNotNone(invoice.id)
            with self.assertRaises(InputErrors) as context:
                updated_invoice = starkbank.invoice.update(
                    invoice.id,
                    amount=invoice_amount,
                    due=datetime.utcnow() + timedelta(hours=1),
                    expiration=timedelta(hours=2),
                )
                self.assertEqual(updated_invoice.amount, invoice_amount)
            errors = context.exception.errors
            for error in errors:
                print(error)
                self.assertEqual('invalidOperation', error.code)
            self.assertEqual(1, len(errors))


class TestInvoicePdfGet(TestCase):

    def test_success(self):
        invoices = starkbank.invoice.query()
        invoice_id = next(invoices).id
        pdf = starkbank.invoice.pdf(invoice_id)
        self.assertGreater(len(pdf), 1000)

class TestInvoiceQrcodeGet(TestCase):

    def test_success(self):
        invoices = starkbank.invoice.query()
        invoice_id = next(invoices).id
        qrcode = starkbank.invoice.qrcode(invoice_id)
        self.assertGreater(len(qrcode), 1000)
        big_qrcode = starkbank.invoice.qrcode(invoice_id, size=25)
        self.assertGreater(len(big_qrcode), 1000)

    def test_fail_invalid_invoice(self):
        with self.assertRaises(InputErrors) as context:
            pdf = starkbank.invoice.pdf("123")

if __name__ == '__main__':
    main()
