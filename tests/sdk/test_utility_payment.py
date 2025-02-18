import starkbank
from datetime import date, timedelta
from unittest import TestCase, main
from tests.utils.user import exampleProject
from tests.utils.utilityPayment import generateExampleUtilityPaymentsJson


starkbank.user = exampleProject


class TestUtilityPaymentQuery(TestCase):

    def test_success(self):
        payments = list(starkbank.utilitypayment.query(limit=10))
        print("Number of payments:", len(payments))


class TestUtilityPaymentPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            payments, cursor = starkbank.utilitypayment.page(limit=2, cursor=cursor)
            for payment in payments:
                print(payment)
                self.assertFalse(payment.id in ids)
                ids.append(payment.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestUtilityPaymentInfoGet(TestCase):

    def test_success(self):
        payments = starkbank.utilitypayment.query()
        payment_id = next(payments).id
        payment = starkbank.utilitypayment.get(id=payment_id)
        self.assertIsNotNone(payment.id)
        self.assertEqual(payment.id, payment_id)


class TestUtilityPaymentPdfGet(TestCase):

    def test_success(self):
        payments = starkbank.utilitypayment.query(status="success")
        payment_id = next(payments).id
        pdf = starkbank.utilitypayment.pdf(id=payment_id)
        self.assertGreater(len(pdf), 1000)


class TestUtilityPaymentDelete(TestCase):

    def test_success(self):
        payments = [starkbank.UtilityPayment(
            description="e6cba87f05fd73aa49306864ab0098f58e7c43f8a9403475a9f10ac605b6ed87",
            scheduled=str(date.today() + timedelta(days=1)),
            tags=["utility", "payment"],
            line="83640000001 1 08740138007 0 61053026111 0 08067159411 9"
        )]
        payments = starkbank.utilitypayment.create(payments)
        starkbank.utilitypayment.delete(payments[0].id)


if __name__ == '__main__':
    main()
