import starkbank
from unittest import TestCase, main
from datetime import date, timedelta
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestVerifiedAccountPost(TestCase):

    def test_success(self):
        verified_accounts = starkbank.verifiedaccount.create([
            starkbank.VerifiedAccount(
                tax_id="012.345.678-90",
                name="Anthony Edward Stark",
                bank_code="20018183",
                branch_code="1357-9",
                number="876543-2",
                type="checking",
                tags=["test-create", "bank-details"],
            )
        ])
        self.assertEqual(len(verified_accounts), 1)
        account = verified_accounts[0]
        self.assertIsNotNone(account.id)
        self.assertIsNotNone(account.status)
        self.assertIsNotNone(account.created)
        self.assertIsNotNone(account.updated)
        self.assertIn(account.status, ["creating", "created", "processing", "active", "failed"])

    def test_success_with_pix_key(self):
        verified_accounts = starkbank.verifiedaccount.create([
            starkbank.VerifiedAccount(
                tax_id="012.345.678-90",
                key_id="tony@starkbank.com",
                tags=["test-create", "pix-key"],
            )
        ])
        self.assertEqual(len(verified_accounts), 1)
        account = verified_accounts[0]
        self.assertIsNotNone(account.id)
        self.assertIsNotNone(account.status)
        self.assertIsNotNone(account.created)
        self.assertIn(account.status, ["creating", "created", "processing", "active", "failed"])


class TestVerifiedAccountQuery(TestCase):

    def test_success(self):
        accounts = list(starkbank.verifiedaccount.query(limit=10))
        self.assertLessEqual(len(accounts), 10)
        for account in accounts:
            self.assertIsNotNone(account.id)
            self.assertIsNotNone(account.status)

    def test_success_with_date_filters(self):
        accounts = list(starkbank.verifiedaccount.query(
            limit=10,
            after=date.today() - timedelta(days=100),
            before=date.today(),
        ))
        self.assertLessEqual(len(accounts), 10)

    def test_success_with_status_filter(self):
        accounts = list(starkbank.verifiedaccount.query(limit=5, status="active"))
        for account in accounts:
            self.assertEqual(account.status, "active")

    def test_success_with_ids_filter(self):
        all_accounts = list(starkbank.verifiedaccount.query(limit=2))
        if not all_accounts:
            return
        ids = [account.id for account in all_accounts]
        filtered = list(starkbank.verifiedaccount.query(ids=ids))
        returned_ids = [account.id for account in filtered]
        for account_id in ids:
            self.assertIn(account_id, returned_ids)


class TestVerifiedAccountPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            accounts, cursor = starkbank.verifiedaccount.page(limit=2, cursor=cursor)
            for account in accounts:
                self.assertFalse(account.id in ids)
                ids.append(account.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestVerifiedAccountInfoGet(TestCase):

    def test_success(self):
        accounts = starkbank.verifiedaccount.query()
        account_id = next(accounts).id
        account = starkbank.verifiedaccount.get(id=account_id)
        self.assertIsNotNone(account.id)
        self.assertEqual(account.id, account_id)
        self.assertIsNotNone(account.status)
        self.assertIsNotNone(account.created)
        self.assertIsNotNone(account.updated)
        self.assertIn(account.status, ["creating", "created", "processing", "active", "failed", "canceled"])


class TestVerifiedAccountCancel(TestCase):

    def test_success(self):
        accounts = starkbank.verifiedaccount.create([
            starkbank.VerifiedAccount(
                tax_id="012.345.678-90",
                key_id="tony@starkbank.com",
            )
        ])
        account = starkbank.verifiedaccount.cancel(accounts[0].id)
        self.assertIsNotNone(account.id)
        self.assertEqual(account.id, accounts[0].id)
        self.assertEqual(account.status, "canceled")


if __name__ == '__main__':
    main()
