import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestMerchantPurchaseQueryLog(TestCase):

    def test_success(self):
        merchant_purchase_logs = starkbank.merchantpurchase.log.query(limit=3)
        for log in merchant_purchase_logs:
            print(log)
            self.assertIsInstance(log.id, str)


class TestMerchantPurchaseGetLog(TestCase):

    def test_success(self):
        merchant_purchase_logs = starkbank.merchantpurchase.log.query(limit=3)
        for log in merchant_purchase_logs:
            print(log.id)
            log = starkbank.merchantpurchase.log.get(log.id)
            self.assertIsInstance(log.id, str)


class TestMerchantPurchasePageLog(TestCase):

    def test_success(self):
        ids = []
        cursor = None
        for _ in range(2):
            page, cursor = starkbank.merchantpurchase.log.page(limit=5, cursor=cursor)
            for entity in page:
                self.assertNotIn(entity.id, ids)
                ids.append(entity.id)
            if cursor is None:
                break
        self.assertEqual(len(ids), 10)


if __name__ == '__main__':
    main()

