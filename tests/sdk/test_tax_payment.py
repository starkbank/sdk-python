import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject
from tests.utils.taxPayment import generateExampleTaxPaymentsJson


starkbank.user = exampleProject


class TestTaxPaymentGet(TestCase):

    def test_success(self):
        payments = list(starkbank.taxpayment.query(limit=10))
        print("Number of payments:", len(payments))


class TestTaxPaymentPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            transfers, cursor = starkbank.taxpayment.page(limit=2, cursor=cursor)
            for transfer in transfers:
                print(transfer)
                self.assertFalse(transfer.id in ids)
                ids.append(transfer.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestTaxPaymentInfoGet(TestCase):

    def test_success(self):
        payments = starkbank.taxpayment.query()
        payment_id = next(payments).id
        payment = starkbank.taxpayment.get(id=payment_id)
        print(payment)
        self.assertIsNotNone(payment.id)
        self.assertEqual(payment.id, payment_id)


class TestTaxPaymentPdfGet(TestCase):

    def test_success(self):
        payments = starkbank.taxpayment.query(limit=1, status="success")
        for payment in payments:
            print(payment)
            pdf = starkbank.taxpayment.pdf(id=payment.id)
            self.assertGreater(len(pdf), 1000)


class TestTaxPaymentDelete(TestCase):

    def test_success(self):
        payments = generateExampleTaxPaymentsJson(n=1, next_day=True)
        payments = starkbank.taxpayment.create(payments)
        starkbank.taxpayment.delete(payments[0].id)


if __name__ == '__main__':
    main()
