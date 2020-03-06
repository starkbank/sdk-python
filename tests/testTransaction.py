import starkbank
from unittest import TestCase, main

from tests.utils.transaction import generateExampleTransactions
from tests.utils.user import exampleMember


class TestTransactionPost(TestCase):

    def testSuccess(self):
        transactions = generateExampleTransactions(n=5)
        transactions, errors = starkbank.transaction.create(user=exampleMember, transactions=transactions)
        if len(errors) != 0:
            code = errors[0].code
            self.assertEqual('invalidBalance', code)
        else:
            self.assertEqual(0, len(errors))

    def testFailInvalidArraySize(self):
        transactions = generateExampleTransactions(n=105)
        transactions, errors = starkbank.transaction.create(user=exampleMember, transactions=transactions)
        self.assertEqual(1, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error.code)

    def testFailInvalidJson(self):
        transactions = {}
        transactions, errors = starkbank.transaction.create(user=exampleMember, transactions=transactions)
        self.assertEqual(1, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error.code)

    def testFailInvalidJsonTransaction(self):
        transactions = generateExampleTransactions(n=6)
        print(transactions)
        transactions[0].amount = None  # Required
        transactions[1].receiver_id = None  # Required
        transactions[2].external_id = None  # Required
        transactions[3].description = None  # Required
        transactions[4].tags = None  # Required

        transactions[5].invalid_parameter = "invalidValue"

        transactions, errors = starkbank.transaction.create(user=exampleMember, transactions=transactions)
        for error in errors:
            print(error)
        self.assertEqual(5, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error.code)


class TestTransactionGet(TestCase):
    def testSuccess(self):
        transactions, cursor, errors = starkbank.transaction.list(user=exampleMember)
        self.assertEqual(0, len(errors))
        self.assertIsInstance(transactions, list)
        print("Number of transactions:", len(transactions))

        # def testFields(self):
        #     raise NotImplementedError
        #     fields = {"amount", "id", "created", "invalid"}
        #     fieldsParams = {"fields": ",".join(fields)}
        #     transactions, cursor, errors = starkbank.transaction.list(user=exampleMember, params=fieldsParams)
        #     self.assertEqual(0, len(errors))
        #     for transaction in transactions:
        #         self.assertTrue(set(transaction.keys()).issubset(fields))


class TestTransactionInfoGet(TestCase):
    def testSuccess(self):
        transactions, cursor, errors = starkbank.transaction.list(user=exampleMember)
        transactionId = transactions[0].id
        transactions, errors = starkbank.transaction.retrieve(user=exampleMember, id=transactionId)
        self.assertEqual(0, len(errors))

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     transactions, cursor, errors = starkbank.transaction.list(user=exampleMember)
    #     transactions = content["transactions"]
    #     transactionId = transactions[0]["id"]
    #     transactions, errors = starkbank.transaction.retrieve(user=exampleMember, id=transactionId, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     transaction = content["transaction"]
    #     print(content)
    #     self.assertTrue(set(transaction.keys()).issubset(fields))


if __name__ == '__main__':
    main()
