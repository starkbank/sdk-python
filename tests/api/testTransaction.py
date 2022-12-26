import starkbank
from datetime import datetime
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.date import randomPastDate
from tests.utils.transaction import generateExampleTransactionsJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestTransactionPost(TestCase):

    def test_success(self):
        old_balance = starkbank.balance.get().amount
        print("old balance: {}".format(old_balance))
        transactions = starkbank.transaction.create(generateExampleTransactionsJson(n=5))
        for transaction in transactions:
            print(transaction)
        new_balance = starkbank.balance.get().amount
        print("new balance: {}".format(new_balance))

        balance = old_balance
        for transaction in transactions:
            balance += transaction.amount - transaction.fee
            self.assertEqual(balance, transaction.balance)
        self.assertEqual(balance, new_balance)

    def test_fail_invalid_array_size(self):
        transactions = generateExampleTransactionsJson(n=105)
        with self.assertRaises(InputErrors) as context:
            transactions = starkbank.transaction.create(transactions)
        errors = context.exception.errors
        for error in errors:
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json(self):
        transactions = {}
        with self.assertRaises(InputErrors) as context:
            transactions = starkbank.transaction.create(transactions)
        errors = context.exception.errors
        for error in errors:
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json_transaction(self):
        transactions = generateExampleTransactionsJson(n=6)
        transactions[0].amount = None  # Required
        transactions[1].receiver_id = None  # Required
        transactions[2].external_id = None  # Required
        transactions[3].description = None  # Required
        transactions[4].tags = None  # Required

        transactions[5].invalid_parameter = "invalidValue"

        with self.assertRaises(InputErrors) as context:
            transactions = starkbank.transaction.create(transactions)
        errors = context.exception.errors
        for error in errors:
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(5, len(errors))


class TestTransactionGet(TestCase):

    def test_success(self):
        transactions = list(starkbank.transaction.query(limit=10))
        print("Number of transactions:", len(transactions))

    def test_success_after_before(self):
        after = randomPastDate(days=10)
        before = datetime.today()
        transactions = starkbank.transaction.query(after=after.date(), before=before.date())
        i = 0
        for i, transaction in enumerate(transactions):
            self.assertTrue(after.date() <= transaction.created.date() <= before.date())
            if i >= 200:
                break
        print("Number of transactions:", i)


class TestTransactionInfoGet(TestCase):

    def test_success(self):
        transactions = starkbank.transaction.query()
        transaction_id = next(transactions).id
        transaction = starkbank.transaction.get(id=transaction_id)


if __name__ == '__main__':
    main()

