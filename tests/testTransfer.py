import starkbank
from unittest import TestCase, main

from tests.utils.transfer import generateExampleTransfersJson
from tests.utils.user import exampleProject


class TestTransferPost(TestCase):

    def testSuccess(self):
        transfers = generateExampleTransfersJson(n=5)
        transfers, errors = starkbank.transfer.create(user=exampleProject, transfers=transfers)
        self.assertEqual(0, len(errors))

    def testFailInvalidArraySize(self):
        transfers = generateExampleTransfersJson(n=105)
        transfers, errors = starkbank.transfer.create(user=exampleProject, transfers=transfers)
        self.assertEqual(1, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error.code)

    def testFailInvalidJson(self):
        transfers = {}
        transfers, errors = starkbank.transfer.create(user=exampleProject, transfers=transfers)
        self.assertEqual(1, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error.code)

    def testFailInvalidJsonTransfer(self):
        transfers = generateExampleTransfersJson(n=7)
        transfers[0].tax_id = None
        transfers[1].amount = None
        transfers[2].name = None
        transfers[3].bank_code = None
        transfers[4].branch_code = None
        transfers[5].account_number = None
        transfers[6].tags = None
        transfers, errors = starkbank.transfer.create(user=exampleProject, transfers=transfers)
        for error in errors:
            print(error)
        self.assertEqual(7, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error.code)

    def testFailInvalidTaxId(self):
        transfers = generateExampleTransfersJson(n=5)
        transfers[0].tax_id = "000.000.000-00"
        transfers[1].tax_id = "00.000.000/0000-00"
        transfers[2].tax_id = "abc"
        transfers[3].tax_id = 123
        transfers[4].tax_id = {}
        transfers, errors = starkbank.transfer.create(user=exampleProject, transfers=transfers)
        for error in errors:
            print(error)
        self.assertEqual(5, len(errors))
        for error in errors:
            self.assertEqual('invalidTaxId', error.code)

    def testFailInvalidAmount(self):
        transfers = generateExampleTransfersJson(n=5)
        transfers[0].amount = "123"
        transfers[1].amount = -5
        transfers[2].amount = 0
        transfers[3].amount = 1000000000000000
        transfers[4].amount = {}
        transfers = starkbank.transfer.create(user=exampleProject, transfers=transfers)


class TestTransferGet(TestCase):
    def testSuccess(self):
        transfers, errors = starkbank.transfer.list(user=exampleProject)
        self.assertEqual(0, len(errors))
        print("Number of transfers:", len(transfers))
        self.assertIsInstance(transfers, list)

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     transfers, errors = starkbank.transfer.list(user=exampleMember, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     for transfer in content["transfers"]:
    #         self.assertTrue(set(transfer.keys()).issubset(fields))
    #     print(content)


class TestTransferInfoGet(TestCase):
    def testSuccess(self):
        transfers = starkbank.transfer.list(user=exampleProject)
        transferId = transfers[0].id
        transfer = starkbank.transfer.retrieve(user=exampleProject, id=transferId)

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     transfers, errors = starkbank.transfer.list(user=exampleMember)
    #     transfers = content["transfers"]
    #     transferId = transfers[0]["id"]
    #     transfers, errors = starkbank.transfer.retrieve(user=exampleMember, id=transferId, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     transfer = content["transfer"]
    #     print(content)
    #     self.assertTrue(set(transfer.keys()).issubset(fields))


class TestTransferPdfGet(TestCase):
    def testSuccess(self):
        transfers, errors = starkbank.transfer.list(user=exampleProject)
        transferId = transfers[0].id
        transfers, errors = starkbank.transfer.retrieve_pdf(user=exampleProject, id=transferId)
        if len(errors) > 0:
            code = errors[0].code
            self.assertEqual('invalidTransfer', code)
        else:
            self.assertEqual(0, len(errors))


# class TestTransferPostAndDelete(TestCase):
#     def testSuccess(self):
#         transfers = generateExampleTransfers(n=1)
#         transfers, errors = starkbank.transfer.create(exampleMember, transfers=transfers)
#         self.assertEqual(0, len(errors))
#         transferId = content["transfers"][0]["id"]
#         transfers, errors = deleteTransfer(exampleMember, id=transferId)
#         self.assertEqual(0, len(errors))
#         print(content)


if __name__ == '__main__':
    main()
