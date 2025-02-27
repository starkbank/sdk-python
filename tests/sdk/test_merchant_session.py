import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject
from tests.utils.merchantSession import generate_example_merchant_session_json, \
    generate_example_merchant_session_purchase_challenge_mode_disabled_json, \
    generate_example_merchant_session_purchase_challenge_mode_enabled_json


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


class TestMerchantSessionPurchaseChallengeModeDisabled(TestCase):

    def test_success(self):
        merchant_session = starkbank.merchantsession.create(generate_example_merchant_session_json("disabled"))
        merchant_session_purchase_json = generate_example_merchant_session_purchase_challenge_mode_disabled_json()
        merchant_session_purchase = starkbank.merchantsession.purchase(
            uuid=merchant_session.uuid,
            purchase=merchant_session_purchase_json
        )
        self.assertIsNotNone(merchant_session_purchase.id)


class TestMerchantSessionPurchaseChallengeModeEnabled(TestCase):

    def test_success(self):
        merchant_session_json = generate_example_merchant_session_json("enabled")
        merchant_session = starkbank.merchantsession.create(merchant_session_json)

        merchant_session_purchase_json = generate_example_merchant_session_purchase_challenge_mode_enabled_json()
        purchase = starkbank.merchantsession.purchase(
            uuid=merchant_session.uuid,
            purchase=merchant_session_purchase_json
        )

        self.assertIsNotNone(purchase.id)


if __name__ == '__main__':
    main()

