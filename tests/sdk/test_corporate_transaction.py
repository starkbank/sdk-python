import starkbank
from unittest import TestCase, main
from datetime import date, timedelta
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestCorporateTransactionQuery(TestCase):

    def test_success(self):
        transactions = starkbank.corporatetransaction.query(
            limit=10,
            after=date.today() - timedelta(days=100),
            before=date.today(),
        )
        for transaction in transactions:
            self.assertIsInstance(transaction.amount, int)


class TestCorporateTransactionPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            transactions, cursor = starkbank.corporatetransaction.page(
                limit=2,
                after=date.today() - timedelta(days=100),
                before=date.today(),
                cursor=cursor
            )
            for transaction in transactions:
                self.assertFalse(transaction.id in ids)
                ids.append(transaction.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestCorporateTransactionGet(TestCase):

    def test_success(self):
        transactions = starkbank.corporatetransaction.query(limit=1)
        transaction = starkbank.corporatetransaction.get(id=next(transactions).id)
        self.assertIsInstance(transaction.amount, int)


if __name__ == '__main__':
    main()
