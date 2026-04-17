import starkbank
from unittest import TestCase, main
from datetime import date, timedelta
from starkcore.error import InputErrors
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestVerifiedAccountLogQuery(TestCase):

    def test_success(self):
        logs = list(starkbank.verifiedaccount.log.query(limit=10))
        self.assertLessEqual(len(logs), 10)
        for log in logs:
            self.assertIsNotNone(log.id)
            self.assertIsNotNone(log.type)
            self.assertIsNotNone(log.created)
            self.assertIsNotNone(log.account)
            self.assertIsNotNone(log.account.id)

    def test_success_with_filters(self):
        logs = list(starkbank.verifiedaccount.log.query(limit=10))
        if not logs:
            return
        account_ids = {log.account.id for log in logs}
        types = {log.type for log in logs}
        filtered_logs = list(starkbank.verifiedaccount.log.query(
            limit=10,
            account_ids=account_ids,
            types=types,
        ))
        for log in filtered_logs:
            self.assertIn(log.account.id, account_ids)
            self.assertIn(log.type, types)

    def test_success_with_date_filters(self):
        logs = list(starkbank.verifiedaccount.log.query(
            limit=10,
            after=date.today() - timedelta(days=30),
            before=date.today(),
        ))
        self.assertLessEqual(len(logs), 10)


class TestVerifiedAccountLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.verifiedaccount.log.page(limit=2, cursor=cursor)
            for log in logs:
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestVerifiedAccountLogInfoGet(TestCase):

    def test_success(self):
        logs = starkbank.verifiedaccount.log.query()
        log_id = next(logs).id
        log = starkbank.verifiedaccount.log.get(id=log_id)
        self.assertIsNotNone(log.id)
        self.assertEqual(log.id, log_id)
        self.assertIsNotNone(log.type)
        self.assertIsNotNone(log.created)
        self.assertIsNotNone(log.account)
        self.assertIsNotNone(log.account.id)

    def test_fail_invalid_log(self):
        log_id = "123"
        with self.assertRaises(InputErrors) as context:
            starkbank.verifiedaccount.log.get(id=log_id)
        errors = context.exception.errors
        for error in errors:
            self.assertEqual('invalidVerifiedAccountLog', error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
