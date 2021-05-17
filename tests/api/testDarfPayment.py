import starkbank
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.user import exampleProject
from tests.utils.taxPayment import generateExampleDarfPaymentsJson


starkbank.user = exampleProject


class TestDarfPaymentPost(TestCase):

    def test_success(self):
        payments = generateExampleDarfPaymentsJson(n=5)
        try:
            payments = starkbank.darfpayment.create(payments)
            for payment in payments:
                print(payment)
        except InputErrors as e:
            for error in e.errors:
                print(error)
                self.assertEqual('immediatePaymentOutOfTime', error.code)

    def test_fail_invalid_array_size(self):
        payments = generateExampleDarfPaymentsJson(n=50)
        payments2 = generateExampleDarfPaymentsJson(n=55)
        payments = payments + payments2
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.darfpayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json(self):
        payments = {}
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.darfpayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json_payment(self):
        payments = generateExampleDarfPaymentsJson(n=4)
        payments[2].description = None
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.darfpayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertTrue(error.code in ["invalidJson", "invalidPayment", "immediatePaymentOutOfTime"])
        self.assertTrue(len(errors) == 1)


class TestDarfPaymentGet(TestCase):

    def test_success(self):
        payments = list(starkbank.darfpayment.query(limit=10))
        print("Number of payments:", len(payments))


class TestDarfPaymentInfoGet(TestCase):

    def test_success(self):
        payments = starkbank.darfpayment.query()
        payment_id = next(payments).id
        payment = starkbank.darfpayment.get(id=payment_id)

    def test_fail_invalid_payment(self):
        payment_id = "0"
        with self.assertRaises(InputErrors) as context:
            payment = starkbank.darfpayment.get(payment_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidPayment', error.code)
        self.assertEqual(1, len(errors))


class TestDarfPaymentPdfGet(TestCase):

    def test_success(self):
        payments = starkbank.darfpayment.query(limit=1, status="success")
        payment_id = next(payments).id
        pdf = starkbank.darfpayment.pdf(id=payment_id)
        self.assertGreater(len(pdf), 1000)


class TestDarfPaymentDelete(TestCase):

    def test_success(self):
        payments = generateExampleDarfPaymentsJson(n=1)
        try:
            payments = starkbank.darfpayment.create(payments)
        except InputErrors as e:
            for error in e.errors:
                print(error)
                self.assertEqual('immediatePaymentOutOfTime', error.code)
        else:
            try:
                starkbank.darfpayment.delete(payments[0].id)
            except InputErrors as e:
                for error in e.errors:
                    print(error)
                    self.assertEqual('invalidAction', error.code)


if __name__ == '__main__':
    main()
