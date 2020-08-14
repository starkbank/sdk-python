import starkbank
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.user import exampleProject
from tests.utils.utilityPayment import generateExampleUtilityPaymentsJson


starkbank.user = exampleProject


class TestUtilityPaymentPost(TestCase):

    def test_success(self):
        payments = generateExampleUtilityPaymentsJson(n=5)
        try:
            payments = starkbank.utilitypayment.create(payments)
        except InputErrors as e:
            for error in e.errors:
                print(error)
                self.assertEqual('immediatePaymentOutOfTime', error.code)

    def test_fail_invalid_array_size(self):
        payments = generateExampleUtilityPaymentsJson(n=50)
        payments2 = generateExampleUtilityPaymentsJson(n=55)
        payments = payments + payments2
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.utilitypayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json(self):
        payments = {}
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.utilitypayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json_payment(self):
        payments = generateExampleUtilityPaymentsJson(n=4)
        payments[0].bar_code = None
        payments[2].description = None
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.utilitypayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertTrue(error.code in ["invalidJson", "invalidPayment", "immediatePaymentOutOfTime"])
        self.assertTrue(len(errors) == 2)


class TestUtilityPaymentGet(TestCase):

    def test_success(self):
        payments = list(starkbank.utilitypayment.query(limit=10))
        print("Number of payments:", len(payments))


class TestUtilityPaymentInfoGet(TestCase):

    def test_success(self):
        payments = starkbank.utilitypayment.query()
        payment_id = next(payments).id
        payment = starkbank.utilitypayment.get(id=payment_id)

    def test_fail_invalid_payment(self):
        payment_id = "0"
        with self.assertRaises(InputErrors) as context:
            payment = starkbank.utilitypayment.get(payment_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidPayment', error.code)
        self.assertEqual(1, len(errors))


class TestUtilityPaymentPdfGet(TestCase):

    def test_success(self):
        payments = starkbank.utilitypayment.query(status="success")
        payment_id = next(payments).id
        pdf = starkbank.utilitypayment.pdf(id=payment_id)
        self.assertGreater(len(pdf), 1000)


class TestUtilityPaymentDelete(TestCase):

    def test_success(self):
        payments = generateExampleUtilityPaymentsJson(n=1, next_day=True)
        try:
            payments = starkbank.utilitypayment.create(payments)
        except InputErrors as e:
            for error in e.errors:
                print(error)
                self.assertEqual('immediatePaymentOutOfTime', error.code)
        else:
            try:
                starkbank.utilitypayment.delete(payments[0].id)
            except InputErrors as e:
                for error in e.errors:
                    print(error)
                    self.assertEqual('invalidAction', error.code)


if __name__ == '__main__':
    main()
