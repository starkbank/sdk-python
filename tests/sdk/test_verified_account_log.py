import starkbank
from unittest import TestCase, main
from tests.utils.verifiedAccount import generateExampleBankInfoVerifiedAccountJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestVerifiedAccountLogQuery(TestCase):

    def test_success(self):
        logs = list(starkbank.verifiedaccount.log.query(limit=3))
        self.assertLessEqual(len(logs), 3)
        for log in logs:
            self.assertIsNotNone(log.id)


class TestVerifiedAccountLogQueryByAccountIds(TestCase):

    def test_success(self):
        account = starkbank.verifiedaccount.create([generateExampleBankInfoVerifiedAccountJson()])[0]
        logs = list(starkbank.verifiedaccount.log.query(account_ids=[account.id], limit=1))
        self.assertGreater(len(logs), 0)
        for log in logs:
            self.assertIsNotNone(log.id)
            self.assertEqual(log.account.id, account.id)


class TestVerifiedAccountLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.verifiedaccount.log.page(limit=5, cursor=cursor)
            for log in logs:
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertGreater(len(ids), 0)


class TestVerifiedAccountLogGet(TestCase):

    def test_success(self):
        logs = list(starkbank.verifiedaccount.log.query(limit=5))
        self.assertGreater(len(logs), 0)
        log_id = logs[0].id
        log = starkbank.verifiedaccount.log.get(log_id)
        self.assertEqual(log.id, log_id)
        self.assertIsNotNone(log.account.id)


if __name__ == '__main__':
    main()
