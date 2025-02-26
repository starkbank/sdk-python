import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestMerchantSessionQueryLog(TestCase):

    def test_success(self):
        merchant_session_logs = starkbank.merchantsession.log.query(limit=3)
        for log in merchant_session_logs:
            print(log)
            self.assertIsInstance(log.id, str)


class TestMerchantSessionGetLog(TestCase):

    def test_success(self):
        merchant_session_logs = starkbank.merchantsession.log.query(limit=3)
        for log in merchant_session_logs:
            log = starkbank.merchantsession.log.get(log.id)
            self.assertIsInstance(log.id, str)


class TestMerchantSessionPageLog(TestCase):

    def test_success(self):
        ids = []
        cursor = None
        for _ in range(2):
            page, cursor = starkbank.merchantsession.log.page(limit=5, cursor=cursor)
            for entity in page:
                self.assertNotIn(entity.id, ids)
                ids.append(entity.id)
            if cursor is None:
                break
        self.assertEqual(len(ids), 10)


if __name__ == '__main__':
    main()

