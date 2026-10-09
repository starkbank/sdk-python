import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject
from starkbank.error import StarkError
from tests.utils.merchantSession import generate_example_merchant_session_json, \
    generate_example_merchant_session_purchase_challenge_mode_disabled_json


starkbank.user = exampleProject


class TestMerchantSessionCreate(TestCase):

    def test_success(self):
        merchant_session_json = generate_example_merchant_session_json("disabled")
        merchant_session = starkbank.merchantsession.create(merchant_session_json)
        self.assertIsNotNone(merchant_session.id)


class TestMerchantSessionQuery(TestCase):

    def test_success(self):
        merchant_sessions = starkbank.merchantsession.query(limit=3)
        for merchant_session in merchant_sessions:
            self.assertIsInstance(merchant_session.id, str)


class TestMerchantSessionGet(TestCase):

    def test_success(self):
        merchant_sessions = starkbank.merchantsession.query(limit=3)
        for session in merchant_sessions:
            merchant_session = starkbank.merchantsession.get(session.id)
            self.assertIsInstance(merchant_session.id, str)


class TestMerchantSessionPage(TestCase):

    def test_success(self):
        ids = []
        cursor = None
        for _ in range(2):
            page, cursor = starkbank.merchantsession.page(limit=5, cursor=cursor)
            for entity in page:
                self.assertNotIn(entity.id, ids)
                ids.append(entity.id)
            if cursor is None:
                break
        self.assertEqual(len(ids), 10)


class TestMerchantSessionPurchase(TestCase):

    def test_deprecated_error(self):
        with self.assertRaises(StarkError) as cm:
            starkbank.merchantsession.purchase(
                uuid="0bb894a2697d41d99fe02cad2c00c9bc",
                purchase=generate_example_merchant_session_purchase_challenge_mode_disabled_json()
            )

        exception = cm.exception
        self.assertIn("Function deprecated since v2.36.0", str(exception))


if __name__ == '__main__':
    main()

