import starkbank
from datetime import datetime
from unittest import TestCase, main
from starkcore.error import InputErrors
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestFixedInvestmentLogQuery(TestCase):

    def test_success_investment_ids(self):
        investment_ids = {log.investment.id for log in starkbank.fixedinvestment.log.query(limit=10)}
        self.assertTrue(len(investment_ids) > 0)
        logs = list(starkbank.fixedinvestment.log.query(limit=50, investment_ids=investment_ids))
        self.assertTrue(len(logs) > 0)
        for log in logs:
            self.assertIsInstance(log, starkbank.fixedinvestment.Log)
            self.assertIsInstance(log.investment, starkbank.FixedInvestment)
            self.assertIn(log.investment.id, investment_ids)
            self.assertIsInstance(log.created, datetime)

    def test_success_withdrawn_amounts(self):
        for log in starkbank.fixedinvestment.log.query(limit=100):
            if log.type != "withdrawn":
                continue
            print(log)
            taxes = sum(tax["amount"] for tax in log.taxes)
            self.assertIsNotNone(log.transaction_id)
            self.assertEqual(log.transaction_amount, log.withdrawn_invested_amount + log.yield_amount - taxes)
            return
        self.skipTest("no withdrawn log in the last 100 logs")


class TestFixedInvestmentLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.fixedinvestment.log.page(limit=2, cursor=cursor)
            for log in logs:
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) > 0)


class TestFixedInvestmentLogGet(TestCase):

    def test_success(self):
        log_id = next(starkbank.fixedinvestment.log.query(limit=1)).id
        log = starkbank.fixedinvestment.log.get(log_id)
        print(log)
        self.assertEqual(log.id, log_id)
        self.assertIsInstance(log.investment, starkbank.FixedInvestment)

    def test_fail_invalid_id(self):
        with self.assertRaises(InputErrors) as context:
            starkbank.fixedinvestment.log.get("123")
        for error in context.exception.errors:
            print(error)


if __name__ == '__main__':
    main()
