from datetime import datetime

import starkbank
from unittest import TestCase, main

from tests.utils.dateGenerator import randomPastDate, randomDateBetween
from tests.utils.transaction import generateExampleTransactions
from tests.utils.user import exampleProject


class TestTransactionPost(TestCase):

    def testSuccess(self):
        transactions = generateExampleTransactions(n=5)
        transactions = starkbank.transaction.create(transactions)

    def testFailInvalidArraySize(self):
        transactions = generateExampleTransactions(n=105)
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            transactions = starkbank.transaction.create(transactions)
        errors = context.exception.elements
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def testFailInvalidJson(self):
        transactions = {}
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            transactions = starkbank.transaction.create(transactions)
        errors = context.exception.elements
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def testFailInvalidJsonTransaction(self):
        transactions = generateExampleTransactions(n=6)
        print(transactions)
        transactions[0].amount = None  # Required
        transactions[1].receiver_id = None  # Required
        transactions[2].external_id = None  # Required
        transactions[3].description = None  # Required
        transactions[4].tags = None  # Required

        transactions[5].invalid_parameter = "invalidValue"

        with self.assertRaises(starkbank.exceptions.InputError) as context:
            transactions = starkbank.transaction.create(transactions)
        errors = context.exception.elements
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(5, len(errors))


class TestTransactionGet(TestCase):
    def testSuccess(self):
        transactions = list(starkbank.transaction.query(limit=10))
        print("Number of transactions:", len(transactions))

    def testSuccessAfterBefore(self):
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
    def testSuccess(self):
        transactions = starkbank.transaction.query()
        transactionId = next(transactions).id
        transaction = starkbank.transaction.get(id=transactionId)


if __name__ == '__main__':
    main()
