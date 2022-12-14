import starkbank
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.brcodePayment import generateExampleBrcodePaymentsJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBrcodePaymentPost(TestCase):

    def test_success(self):
        payments = generateExampleBrcodePaymentsJson(n=5)
        try:
            payments = starkbank.brcodepayment.create(payments)
        except InputErrors as e:
            for error in e.errors:
                print(error)
                self.assertEqual('immediatePaymentOutOfTime', error.code)

    def test_fail_invalid_array_size(self):
        payments = generateExampleBrcodePaymentsJson(n=50)
        payments2 = generateExampleBrcodePaymentsJson(n=55)
        payments = payments + payments2
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.brcodepayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json(self):
        payments = {}
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.brcodepayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json_payment(self):
        payments = generateExampleBrcodePaymentsJson(n=4)
        payments[0].line = None
        payments[1].scheduled = None
        payments[2].description = None
        payments[3].tax_id = None
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.brcodepayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertTrue(error.code in ["invalidJson", "invalidBrcode", "invalidPayment", "invalidBrcodePayment"])
        self.assertTrue(len(errors) >= 2)

    def test_fail_invalid_tax_id(self):
        payments = generateExampleBrcodePaymentsJson(n=5)
        payments[0].tax_id = "000.000.000-00"
        payments[1].tax_id = "00.000.000/0000-00"
        payments[2].tax_id = "abc"
        payments[3].tax_id = 123
        payments[4].tax_id = {}
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.brcodepayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertTrue(error.code in ["invalidTaxId", "immediatePaymentOutOfTime"])
        self.assertTrue(len(errors) == 5 or len(errors) == 10)


class TestBrcodePaymentGet(TestCase):

    def test_success(self):
        payments = list(starkbank.brcodepayment.query(limit=10))
        print("Number of payments:", len(payments))


class TestBrcodePaymentInfoGet(TestCase):

    def test_success(self):
        payments = starkbank.brcodepayment.query()
        payment_id = next(payments).id
        payment = starkbank.brcodepayment.get(id=payment_id)

    def test_fail_invalid_payment(self):
        payment_id = "0"
        with self.assertRaises(InputErrors) as context:
            payment = starkbank.brcodepayment.get(payment_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidBrcodePayment', error.code)
        self.assertEqual(1, len(errors))


class TestBrcodePaymentInfoPatch(TestCase):

    def test_success_cancel(self):
        payments = starkbank.brcodepayment.query(status="created", limit=1)
        for payment in payments:
            self.assertIsNotNone(payment.id)
            self.assertEqual(payment.status, "created")
            updated_payment = starkbank.brcodepayment.update(payment.id, status="canceled")
            self.assertEqual(updated_payment.status, "canceled")


class TestBrcodePaymentPdfGet(TestCase):

    def test_success(self):
        payments = starkbank.brcodepayment.query(status="success")
        payment_id = next(payments).id
        pdf = starkbank.brcodepayment.pdf(payment_id)
        self.assertGreater(len(pdf), 1000)


if __name__ == '__main__':
    main()
