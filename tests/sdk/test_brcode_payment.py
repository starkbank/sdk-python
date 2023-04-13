import starkbank
from unittest import TestCase, main
from tests.utils.brcodePayment import generateExampleBrcodePaymentsJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBrcodePaymentPost(TestCase):

    def test_success(self):
        payments = generateExampleBrcodePaymentsJson(n=5, next_day=True)
        payments = starkbank.brcodepayment.create(payments)
        for payment in payments:
            self.assertIsNotNone(payment.id)
            for rule in payment.rules:
                if rule.key == "resendingLimit":
                    self.assertIsNotNone(rule.value)


class TestBrcodePaymentQuery(TestCase):

    def test_success(self):
        payments = list(starkbank.brcodepayment.query(limit=10))
        print(payments)
        self.assertEqual(10, len(payments))


class TestBrcodePaymentPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            payments, cursor = starkbank.brcodepayment.page(limit=2, cursor=cursor)
            for payment in payments:
                print(payment)
                self.assertFalse(payment.id in ids)
                ids.append(payment.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestBrcodePaymentInfoGet(TestCase):

    def test_success(self):
        payments = starkbank.brcodepayment.query()
        payment_id = next(payments).id
        payment = starkbank.brcodepayment.get(id=payment_id)


class TestBrcodePaymentInfoPatch(TestCase):

    def test_success_cancel(self):
        payments = starkbank.brcodepayment.query(status="created", limit=1)
        for payment in payments:
            self.assertIsNotNone(payment.id)
            self.assertEqual(payment.status, "created")
            updated_payment = starkbank.brcodepayment.update(payment.id, status="canceled")
            self.assertEqual(updated_payment.status, "canceled")


if __name__ == '__main__':
    main()
