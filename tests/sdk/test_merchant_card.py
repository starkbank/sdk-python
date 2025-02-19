import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject

starkbank.user = exampleProject

class TestMerchantCardQuery(TestCase):

    def test_success(self):
        merchant_cards = starkbank.merchantcard.query(limit=3)
        for merchant_card in merchant_cards:
            self.assertIsInstance(merchant_card.id, str)


class TestMerchantCardGet(TestCase):

    def test_success(self):
        merchant_cards = starkbank.merchantcard.query(limit=3)
        for purchase in merchant_cards:
            merchant_card = starkbank.merchantcard.get(purchase.id)
            self.assertIsInstance(merchant_card.id, str)


class TestMerchantCardPage(TestCase):

    def test_success(self):
        ids = []
        cursor = None
        for _ in range(2):
            page, cursor = starkbank.merchantcard.page(limit=5, cursor=cursor)
            for entity in page:
                self.assertNotIn(entity.id, ids)
                ids.append(entity.id)
            if cursor is None:
                break
        self.assertEqual(len(ids), 10)


if __name__ == '__main__':
    main()

