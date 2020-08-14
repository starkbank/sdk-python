import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject
from tests.utils.taxPayment import generateExampleTaxPaymentsJson


starkbank.user = exampleProject


class TestTaxPaymentGet(TestCase):

    def test_success(self):
        payments = list(starkbank.taxpayment.query(limit=10))
        print("Number of payments:", len(payments))


class TestTaxPaymentInfoGet(TestCase):

    def test_success(self):
        payments = starkbank.taxpayment.query()
        payment_id = next(payments).id
        payment = starkbank.taxpayment.get(id=payment_id)
        self.assertIsNotNone(payment.id)
        self.assertEqual(payment.id, payment_id)


class TestTaxPaymentPdfGet(TestCase):

    def test_success(self):
        payments = starkbank.taxpayment.query(status="processing")
        payment_id = next(payments).id
        pdf = starkbank.taxpayment.pdf(id=payment_id)
        self.assertGreater(len(pdf), 1000)


class TestTaxPaymentDelete(TestCase):

    def test_success(self):
        payments = generateExampleTaxPaymentsJson(n=1, next_day=True)
        payments = starkbank.taxpayment.create(payments)
        starkbank.taxpayment.delete(payments[0].id)


if __name__ == '__main__':
    main()
