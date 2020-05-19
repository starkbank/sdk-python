import starkbank
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.boletoPayment import generateExampleBoletoPaymentsJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBoletoPaymentPost(TestCase):

    def test_success(self):
        payments = generateExampleBoletoPaymentsJson(n=5)
        try:
            payments = starkbank.boletopayment.create(payments)
        except InputErrors as e:
            for error in e.errors:
                print(error)
                self.assertEqual('immediatePaymentOutOfTime', error.code)

    def test_fail_invalid_array_size(self):
        payments = generateExampleBoletoPaymentsJson(n=50)
        payments2 = generateExampleBoletoPaymentsJson(n=55)
        payments = payments + payments2
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.boletopayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json(self):
        payments = {}
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.boletopayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json_payment(self):
        payments = generateExampleBoletoPaymentsJson(n=4)
        payments[0].line = None
        payments[1].scheduled = None
        payments[2].description = None
        payments[3].tax_id = None
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.boletopayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertTrue(error.code in ["invalidJson", "invalidPayment", "immediatePaymentOutOfTime"])
        self.assertTrue(len(errors) == 3 or len(errors) == 6)

    def test_fail_invalid_tax_id(self):
        payments = generateExampleBoletoPaymentsJson(n=5)
        payments[0].tax_id = "000.000.000-00"
        payments[1].tax_id = "00.000.000/0000-00"
        payments[2].tax_id = "abc"
        payments[3].tax_id = 123
        payments[4].tax_id = {}
        with self.assertRaises(InputErrors) as context:
            payments = starkbank.boletopayment.create(payments)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertTrue(error.code in ["invalidTaxId", "immediatePaymentOutOfTime"])
        self.assertTrue(len(errors) == 5 or len(errors) == 10)


class TestBoletoPaymentGet(TestCase):

    def test_success(self):
        payments = list(starkbank.boletopayment.query(limit=10))
        print("Number of payments:", len(payments))


class TestBoletoPaymentInfoGet(TestCase):

    def test_success(self):
        payments = starkbank.boletopayment.query()
        payment_id = next(payments).id
        payment = starkbank.boletopayment.get(id=payment_id)

    def test_fail_invalid_payment(self):
        payment_id = "0"
        with self.assertRaises(InputErrors) as context:
            payment = starkbank.boletopayment.get(payment_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidPayment', error.code)
        self.assertEqual(1, len(errors))


class TestBoletoPaymentPdfGet(TestCase):

    def test_success(self):
        payments = starkbank.boletopayment.query(status="success")
        payment_id = next(payments).id
        pdf = starkbank.boletopayment.pdf(id=payment_id)
        self.assertGreater(len(pdf), 1000)


class TestBoletoPaymentDelete(TestCase):

    def test_success(self):
        payments = generateExampleBoletoPaymentsJson(n=1)
        try:
            payments = starkbank.boletopayment.create(payments)
        except InputErrors as e:
            for error in e.errors:
                print(error)
                self.assertEqual('immediatePaymentOutOfTime', error.code)
        else:
            try:
                starkbank.boletopayment.delete(payments[0].id)
            except InputErrors as e:
                for error in e.errors:
                    print(error)
                    self.assertEqual('invalidAction', error.code)


if __name__ == '__main__':
    main()
