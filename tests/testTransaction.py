from unittest import TestCase, main

from starkbank.old_ledger.transaction import postTransaction, getTransaction, getTransactionInfo
from tests.utils.transaction import generateExampleTransactions
from tests.utils.user import exampleMember


class TestTransactionPost(TestCase):

    def testSuccess(self):
        transactionJson = generateExampleTransactions(n=5)
        content, status = postTransaction(exampleMember, transactionJson=transactionJson)
        if status != 200:
            code = content["errors"][0]["code"]
            self.assertEqual('invalidBalance', code)
        else:
            self.assertEqual(200, status)
        print(content)

    def testFailInvalidArraySize(self):
        transactionJson = generateExampleTransactions(n=105)
        content, status = postTransaction(exampleMember, transactionJson=transactionJson)
        print(content)
        errors = content["errors"]
        self.assertEqual(1, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error["code"])

    def testFailInvalidJson(self):
        transactionJson = {}
        content, status = postTransaction(exampleMember, transactionJson=transactionJson)
        errors = content["errors"]
        self.assertEqual(1, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error["code"])

    def testFailInvalidJsonTransaction(self):
        transactionJson = generateExampleTransactions(n=7)
        print(transactionJson)
        transactionJson["transactions"][0].pop("amount")  # Required
        transactionJson["transactions"][1].pop("receiverId")  # Required
        transactionJson["transactions"][2].pop("externalId")  # Required
        transactionJson["transactions"][3].pop("description")  # Required
        transactionJson["transactions"][4].pop("tags")  # Required

        transactionJson["transactions"][6]["invalidParameter"] = "invalidValue"

        content, status = postTransaction(exampleMember, transactionJson=transactionJson)
        print(content)
        errors = content["errors"]
        for error in errors:
            print(error)
        self.assertEqual(5, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error["code"])


class TestTransactionGet(TestCase):
    def testSuccess(self):
        content, status = getTransaction(exampleMember)
        self.assertEqual(200, status)
        transactions = content["transactions"]
        self.assertIsInstance(transactions, list)
        print("Number of transactions:", len(transactions))
        print(content)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getTransaction(exampleMember, params=fieldsParams)
        self.assertEqual(200, status)
        for transaction in content["transactions"]:
            self.assertTrue(set(transaction.keys()).issubset(fields))
        print(content)


class TestTransactionInfoGet(TestCase):
    def testSuccess(self):
        content, status = getTransaction(exampleMember)
        transactions = content["transactions"]
        transactionId = transactions[0]["id"]
        content, status = getTransactionInfo(exampleMember, transactionId=transactionId)
        print(content)
        self.assertEqual(200, status)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getTransaction(exampleMember)
        transactions = content["transactions"]
        transactionId = transactions[0]["id"]
        content, status = getTransactionInfo(exampleMember, transactionId=transactionId, params=fieldsParams)
        self.assertEqual(200, status)
        transaction = content["transaction"]
        print(content)
        self.assertTrue(set(transaction.keys()).issubset(fields))


if __name__ == '__main__':
    main()
