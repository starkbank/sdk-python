import starkbank
from unittest import TestCase, main
from starkcore.error import InputErrors
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


class TestDarfPaymentPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            transfers, cursor = starkbank.darfpayment.page(limit=2, cursor=cursor)
            for transfer in transfers:
                print(transfer)
                self.assertFalse(transfer.id in ids)
                ids.append(transfer.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestDarfPaymentGet(TestCase):

    def test_success(self):
        payments = list(starkbank.darfpayment.query(limit=10))
        print("Number of payments:", len(payments))


class TestDarfPaymentInfoGet(TestCase):

    def test_success(self):
        payments = starkbank.darfpayment.query()
        payment_id = next(payments).id
        payment = starkbank.darfpayment.get(id=payment_id)


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
