import starkbank
from unittest import TestCase, main
from tests.utils.boletoPayment import generateExampleBoletoPaymentsJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBoletoPaymentPost(TestCase):

    def test_success(self):
        payments = generateExampleBoletoPaymentsJson(n=5, next_day=True)
        payments = starkbank.boletopayment.create(payments)
        for payment in payments:
            print(payment)


class TestBoletoPaymentGet(TestCase):

    def test_success(self):
        payments = list(starkbank.boletopayment.query(limit=10))
        print(payments)
        self.assertEqual(10, len(payments))


class TestBoletoPaymentInfoGet(TestCase):

    def test_success(self):
        payments = starkbank.boletopayment.query()
        payment_id = next(payments).id
        payment = starkbank.boletopayment.get(id=payment_id)


class TestBoletoPaymentPdfGet(TestCase):

    def test_success(self):
        payments = starkbank.boletopayment.query(status="success")
        payment_id = next(payments).id
        pdf = starkbank.boletopayment.pdf(id=payment_id)
        self.assertGreater(len(pdf), 1000)


class TestBoletoPaymentDelete(TestCase):

    def test_success(self):
        payments = generateExampleBoletoPaymentsJson(n=1, next_day=True)
        payments = starkbank.boletopayment.create(payments)
        starkbank.boletopayment.delete(payments[0].id)


if __name__ == '__main__':
    main()
