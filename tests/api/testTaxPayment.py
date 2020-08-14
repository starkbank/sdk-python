import starkbank
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.user import exampleProject
from tests.utils.taxPayment import generateExampleTaxPaymentsJson


starkbank.user = exampleProject


class TestTaxPaymentPost(TestCase):

    def test_success(self):
        payments = generateExampleTaxPaymentsJson(n=5)
        try:
            [print(p.bar_code) for p in payments]
            payments = starkbank.taxpayment.create(payments)
        except InputErrors as e:
            for error in e.errors:
                print(error)
                self.assertEqual('immediatePaymentOutOfTime', error.code)

    def test_fail_invalid_array_size(self):
        payments = generateExampleTaxPaymentsJson(n=50)
        payments2 = generateExampleTaxPaymentsJson(n=55)
        payments = payments + payments2
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.taxpayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json(self):
        payments = {}
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.taxpayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json_payment(self):
        payments = generateExampleTaxPaymentsJson(n=4)
        payments[0].bar_code = None
        payments[2].description = None
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.taxpayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertTrue(error.code in ["invalidJson", "invalidPayment", "immediatePaymentOutOfTime"])
        self.assertTrue(len(errors) == 2)


class TestTaxPaymentGet(TestCase):

    def test_success(self):
        payments = list(starkbank.taxpayment.query(limit=10))
        print("Number of payments:", len(payments))


class TestTaxPaymentInfoGet(TestCase):

    def test_success(self):
        payments = starkbank.taxpayment.query()
        payment_id = next(payments).id
        payment = starkbank.taxpayment.get(id=payment_id)

    def test_fail_invalid_payment(self):
        payment_id = "0"
        with self.assertRaises(InputErrors) as context:
            payment = starkbank.taxpayment.get(payment_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidPayment', error.code)
        self.assertEqual(1, len(errors))


class TestTaxPaymentPdfGet(TestCase):

    def test_success(self):
        payments = starkbank.taxpayment.query(status="processing")
        payment_id = next(payments).id
        pdf = starkbank.taxpayment.pdf(id=payment_id)
        self.assertGreater(len(pdf), 1000)


class TestTaxPaymentDelete(TestCase):

    def test_success(self):
        payments = generateExampleTaxPaymentsJson(n=1)
        try:
            payments = starkbank.taxpayment.create(payments)
        except InputErrors as e:
            for error in e.errors:
                print(error)
                self.assertEqual('immediatePaymentOutOfTime', error.code)
        else:
            try:
                starkbank.taxpayment.delete(payments[0].id)
            except InputErrors as e:
                for error in e.errors:
                    print(error)
                    self.assertEqual('invalidAction', error.code)


if __name__ == '__main__':
    main()
