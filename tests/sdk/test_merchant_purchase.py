import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject
from tests.utils.merchantPurchase import generate_example_merchant_purchase_json


starkbank.user = exampleProject


class TestMerchantPurchaseCreate(TestCase):

    def test_success(self):
        merchant_purchases = starkbank.merchantpurchase.query(status="confirmed", limit=1)
        for merchant_purchase in merchant_purchases:
            merchant_purchase_json = generate_example_merchant_purchase_json(merchant_purchase.card_id)
            merchant_purchase_created = starkbank.merchantpurchase.create(merchant_purchase_json)
            self.assertIsNotNone(merchant_purchase_created.id)


class TestMerchantPurchaseQuery(TestCase):

    def test_success(self):
        merchant_purchases = starkbank.merchantpurchase.query(limit=3)
        for merchant_purchase in merchant_purchases:
            self.assertIsInstance(merchant_purchase.id, str)


class TestMerchantPurchaseGet(TestCase):

    def test_success(self):
        merchant_purchases = starkbank.merchantpurchase.query(limit=3)
        for purchase in merchant_purchases:
            merchant_purchase = starkbank.merchantpurchase.get(purchase.id)
            self.assertIsInstance(merchant_purchase.id, str)


class TestMerchantPurchasePage(TestCase):

    def test_success(self):
        ids = []
        cursor = None
        for _ in range(2):
            page, cursor = starkbank.merchantpurchase.page(limit=5, cursor=cursor)
            for entity in page:
                self.assertNotIn(entity.id, ids)
                ids.append(entity.id)
            if cursor is None:
                break
        self.assertEqual(len(ids), 10)


class TestMerchantPurchaseUpdate(TestCase):

    def test_success(self):
        merchant_purchases = starkbank.merchantpurchase.query(limit=1, status="confirmed")
        for merchant_purchase in merchant_purchases:
            if merchant_purchase.amount == 0:
                continue

            merchant_purchase = starkbank.merchantpurchase.update(id=merchant_purchase.id, status="reversed", amount=0)
            self.assertIsInstance(merchant_purchase.id, str)


if __name__ == '__main__':
    main()

