import starkbank
from unittest import TestCase, main
from datetime import date, timedelta
from tests.utils.verifiedAccount import generateExampleBankInfoVerifiedAccountJson, generateExamplePixKeyVerifiedAccountJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestVerifiedAccountCreate(TestCase):

    def test_success(self):
        accounts = starkbank.verifiedaccount.create([generateExampleBankInfoVerifiedAccountJson()])
        self.assertEqual(len(accounts), 1)
        self.assertIsNotNone(accounts[0].id)


class TestVerifiedAccountCreateWithPixKey(TestCase):

    def test_success(self):
        accounts = starkbank.verifiedaccount.create([generateExamplePixKeyVerifiedAccountJson()])
        self.assertEqual(len(accounts), 1)
        self.assertIsNotNone(accounts[0].id)


class TestVerifiedAccountCreateAndGet(TestCase):

    def test_success(self):
        accounts = starkbank.verifiedaccount.create([generateExampleBankInfoVerifiedAccountJson()])
        created = accounts[0]
        self.assertIsNotNone(created.id)
        retrieved = starkbank.verifiedaccount.get(created.id)
        self.assertEqual(retrieved.id, created.id)


class TestVerifiedAccountCreateAndCancel(TestCase):

    def test_success(self):
        accounts = starkbank.verifiedaccount.create([generateExampleBankInfoVerifiedAccountJson()])
        created = accounts[0]
        self.assertIsNotNone(created.id)
        canceled = starkbank.verifiedaccount.cancel(created.id)
        self.assertEqual(canceled.id, created.id)
        self.assertEqual(canceled.status, "canceled")


class TestVerifiedAccountQuery(TestCase):

    def test_success(self):
        accounts = list(starkbank.verifiedaccount.query(limit=3, status="active"))
        self.assertLessEqual(len(accounts), 3)
        for account in accounts:
            self.assertIsNotNone(account.id)


class TestVerifiedAccountQueryFilters(TestCase):

    def test_success(self):
        created = starkbank.verifiedaccount.create([generateExampleBankInfoVerifiedAccountJson()])[0]

        accounts = list(starkbank.verifiedaccount.query(
            tags=["verified-account-test"],
            after=date.today() - timedelta(days=100),
            before=date.today(),
        ))
        self.assertGreater(len(accounts), 0)
        found = False
        for account in accounts:
            self.assertIsNotNone(account.id)
            if account.id == created.id:
                found = True
        self.assertTrue(found)

        accounts_by_id = list(starkbank.verifiedaccount.query(ids=[created.id]))
        self.assertEqual(len(accounts_by_id), 1)
        self.assertEqual(accounts_by_id[0].id, created.id)


class TestVerifiedAccountPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            accounts, cursor = starkbank.verifiedaccount.page(limit=5, cursor=cursor)
            for account in accounts:
                self.assertFalse(account.id in ids)
                ids.append(account.id)
            if cursor is None:
                break
        self.assertGreater(len(ids), 0)


if __name__ == '__main__':
    main()
