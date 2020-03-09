import time

import starkbank
from unittest import TestCase, main

from tests.utils.transfer import generateExampleTransfersJson
from tests.utils.user import exampleProject


class TestTransferPost(TestCase):

    def testSuccess(self):
        transfers = generateExampleTransfersJson(n=5)
        transfers = starkbank.transfer.create(transfers)
        for transfer in transfers:
            print(transfer.id)

    def testFailInvalidArraySize(self):
        transfers = generateExampleTransfersJson(n=105)
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            transfers = starkbank.transfer.create(transfers)
        errors = context.exception.elements
        for error in errors:
            print(error)
            self.assertEqual("invalidJson", error.code)
        self.assertEqual(1, len(errors))

    def testFailInvalidJson(self):
        transfers = {}
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            transfers = starkbank.transfer.create(transfers)
        errors = context.exception.elements
        for error in errors:
            print(error)
            self.assertEqual("invalidJson", error.code)
        self.assertEqual(1, len(errors))

    def testFailInvalidJsonTransfer(self):
        transfers = generateExampleTransfersJson(n=7)
        transfers[0].tax_id = None
        transfers[1].amount = None
        transfers[2].name = None
        transfers[3].bank_code = None
        transfers[4].branch_code = None
        transfers[5].account_number = None
        transfers[6].tags = None
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            transfers = starkbank.transfer.create(transfers)
        errors = context.exception.elements
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(7, len(errors))

    def testFailInvalidTaxId(self):
        transfers = generateExampleTransfersJson(n=5)
        transfers[0].tax_id = "000.000.000-00"
        transfers[1].tax_id = "00.000.000/0000-00"
        transfers[2].tax_id = "abc"
        transfers[3].tax_id = 123  # 2 errors
        transfers[4].tax_id = {}  # 2 errors
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            transfers = starkbank.transfer.create(transfers)
        errors = context.exception.elements
        for error in errors:
            print(error)
            self.assertEqual('invalidTaxId', error.code)
        self.assertEqual(5, len(errors))

    def testFailInvalidAmount(self):
        transfers = generateExampleTransfersJson(n=5)
        transfers[0].amount = "123"
        transfers[1].amount = -5
        transfers[2].amount = 0
        transfers[3].amount = 1000000000000000
        transfers[4].amount = {}
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            transfers = starkbank.transfer.create(transfers)
        errors = context.exception.elements
        for error in errors:
            print(error)
            self.assertEqual('invalidAmount', error.code)
        self.assertEqual(5, len(errors))

    def testFailInvalidBalance(self):
        balance = starkbank.balance.get()
        transfer = generateExampleTransfersJson(n=1)[0]
        transfer.amount = 2 * balance.amount
        transfers = starkbank.transfer.create([transfer])
        time.sleep(3)
        transfer = starkbank.transfer.get(id=transfers[0].id)
        self.assertEqual("failed", transfer.status)

    def testFailInvalidBalanceWithFee(self):
        balances = starkbank.balance.query()
        transfer = generateExampleTransfersJson(n=1)[0]
        transfer.amount = next(balances).amount
        transfers = starkbank.transfer.create([transfer])
        time.sleep(3)
        transfer = starkbank.transfer.get(id=transfers[0].id)
        self.assertEqual("failed", transfer.status)


class TestTransferGet(TestCase):
    def testSuccess(self):
        transfers = list(starkbank.transfer.query(limit=10))
        assert len(transfers) == 10

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     transfers = starkbank.transfer.list(params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     for transfer in content["transfers"]:
    #         self.assertTrue(set(transfer.keys()).issubset(fields))
    #     print(content)


class TestTransferInfoGet(TestCase):
    def testSuccess(self):
        transfers = starkbank.transfer.query(user=exampleProject)
        transferId = next(transfers).id
        transfer = starkbank.transfer.get(id=transferId)

    def testFailInvalidTransfer(self):
        transferId = "0"
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            transfer = starkbank.transfer.get(id=transferId)
        errors = context.exception.elements
        for error in errors:
            print(error)
            self.assertEqual('invalidTransfer', error.code)
        self.assertEqual(1, len(errors))

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     transfers = starkbank.transfer.list(user=exampleMember)
    #     transfers = content["transfers"]
    #     transferId = transfers[0]["id"]
    #     transfers = starkbank.transfer.get(id=transferId, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     transfer = content["transfer"]
    #     print(content)
    #     self.assertTrue(set(transfer.keys()).issubset(fields))


class TestTransferPdfGet(TestCase):
    def testSuccess(self):
        transfers = starkbank.transfer.query(user=exampleProject)
        transferId = next(transfers).id
        try:
            pdf = starkbank.transfer.get_pdf(id=transferId)
            print(str(pdf))
        except starkbank.exceptions.InputError as e:
            errors = e.elements
            for error in errors:
                self.assertEqual("invalidTransfer", error.code)


# class TestTransferPostAndDelete(TestCase):
#     def testSuccess(self):
#         transfers = generateExampleTransfers(n=1)
#         transfers = starkbank.transfer.create(transfers=transfers)
#         self.assertEqual(0, len(errors))
#         transferId = content["transfers"][0]["id"]
#         transfers = deleteTransfer(id=transferId)
#         self.assertEqual(0, len(errors))
#         print(content)


if __name__ == '__main__':
    main()
