from unittest import TestCase, main

from starkbank.old_transfer.transfer import postTransfer, getTransfer, getTransferInfo, deleteTransfer, getTransferPdf
from tests.utils.transfer import generateExampleTransfers
from tests.utils.user import exampleMember


class TestTransferPost(TestCase):

    def testSuccess(self):
        transfersJson = generateExampleTransfers(n=5)
        content, status = postTransfer(exampleMember, transfersJson=transfersJson)
        print(content)
        self.assertEqual(200, status)

    def testFailInvalidJson(self):
        transfersJson = {}
        content, status = postTransfer(exampleMember, transfersJson=transfersJson)
        print(content)
        errors = content["errors"]
        self.assertEqual(1, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error["code"])

    def testFailInvalidJsonTransfer(self):
        transfersJson = generateExampleTransfers(n=7)
        transfersJson["transfers"][0].pop("taxId")
        transfersJson["transfers"][1].pop("amount")
        transfersJson["transfers"][2].pop("name")
        transfersJson["transfers"][3].pop("bankCode")
        transfersJson["transfers"][4].pop("branchCode")
        transfersJson["transfers"][5].pop("accountNumber")
        transfersJson["transfers"][6].pop("tags")
        content, status = postTransfer(exampleMember, transfersJson=transfersJson)
        print(content)
        errors = content["errors"]
        self.assertEqual(7, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error["code"])

    def testFailInvalidTaxId(self):
        transfersJson = generateExampleTransfers(n=5)
        transfersJson["transfers"][0]["taxId"] = "000.000.000-00"
        transfersJson["transfers"][1]["taxId"] = "00.000.000/0000-00"
        transfersJson["transfers"][2]["taxId"] = "abc"
        transfersJson["transfers"][3]["taxId"] = 123
        transfersJson["transfers"][4]["taxId"] = {}
        content, status = postTransfer(exampleMember, transfersJson=transfersJson)
        print(content)
        errors = content["errors"]
        self.assertEqual(5, len(errors))
        for error in errors:
            self.assertEqual('invalidTaxId', error["code"])

    def testFailInvalidAmount(self):
        transfersJson = generateExampleTransfers(n=5)
        transfersJson["transfers"][0]["amount"] = "123"
        transfersJson["transfers"][1]["amount"] = -5
        transfersJson["transfers"][2]["amount"] = 0
        transfersJson["transfers"][3]["amount"] = 1000000000000000
        transfersJson["transfers"][4]["amount"] = {}
        content, status = postTransfer(exampleMember, transfersJson=transfersJson)
        print(content)
        errors = content["errors"]
        self.assertEqual(5, len(errors))
        for error in errors:
            self.assertEqual('invalidAmount', error["code"])


class TestTransferGet(TestCase):
    def testSuccess(self):
        content, status = getTransfer(exampleMember)
        self.assertEqual(200, status)
        transfers = content["transfers"]
        print("Number of transfers:", len(transfers))
        print(content)
        self.assertIsInstance(transfers, list)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getTransfer(exampleMember, params=fieldsParams)
        self.assertEqual(200, status)
        for transfer in content["transfers"]:
            self.assertTrue(set(transfer.keys()).issubset(fields))
        print(content)


class TestTransferInfoGet(TestCase):
    def testSuccess(self):
        content, status = getTransfer(exampleMember)
        transfers = content["transfers"]
        transferId = transfers[0]["id"]
        content, status = getTransferInfo(exampleMember, transferId=transferId)
        print(content)
        self.assertEqual(200, status)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getTransfer(exampleMember)
        transfers = content["transfers"]
        transferId = transfers[0]["id"]
        content, status = getTransferInfo(exampleMember, transferId=transferId, params=fieldsParams)
        self.assertEqual(200, status)
        transfer = content["transfer"]
        print(content)
        self.assertTrue(set(transfer.keys()).issubset(fields))


class TestTransferPdfGet(TestCase):
    def testSuccess(self):
        content, status = getTransfer(exampleMember)
        transfers = content["transfers"]
        transferId = transfers[0]["id"]
        content, status = getTransferPdf(exampleMember, transferId=transferId)
        print(content)
        if status != 200:
            code = content["errors"][0]["code"]
            self.assertEqual('invalidTransfer', code)
        else:
            self.assertEqual(200, status)


# class TestTransferPostAndDelete(TestCase):
#     def testSuccess(self):
#         transfersJson = generateExampleTransfers(n=1)
#         content, status = postTransfer(exampleMember, transfersJson=transfersJson)
#         self.assertEqual(200, status)
#         transferId = content["transfers"][0]["id"]
#         content, status = deleteTransfer(exampleMember, transferId=transferId)
#         self.assertEqual(200, status)
#         print(content)


if __name__ == '__main__':
    main()
