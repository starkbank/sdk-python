import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestMerchantInstallmentQuery(TestCase):

    def test_success(self):
        merchant_installments = starkbank.merchantinstallment.query(limit=3)
        for merchant_installment in merchant_installments:
            self.assertIsInstance(merchant_installment.id, str)


class TestMerchantInstallmentGet(TestCase):

    def test_success(self):
        merchant_installments = starkbank.merchantpurchase.query(limit=3)
        for merchant_installment in merchant_installments:
            merchant_installment = starkbank.merchantpurchase.get(merchant_installment.id)
            self.assertIsInstance(merchant_installment.id, str)


class TestMerchantInstallmentPage(TestCase):

    def test_success(self):
        ids = []
        cursor = None
        for _ in range(2):
            page, cursor = starkbank.merchantinstallment.page(limit=5, cursor=cursor)
            for entity in page:
                self.assertNotIn(entity.id, ids)
                ids.append(entity.id)
            if cursor is None:
                break
        self.assertEqual(len(ids), 10)


if __name__ == '__main__':
    main()

