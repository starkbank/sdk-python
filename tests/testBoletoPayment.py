from unittest import TestCase, main

from starkbank.old_boletoPayment.boletoPayment import getBoletoPayment, postBoletoPayment, getBoletoPaymentInfo, \
    getBoletoPaymentPdf
from tests.utils.boletoPayment import generateExampleBoletoPayments
from tests.utils.user import exampleMemberOld


class TestBoletoPaymentPost(TestCase):

    def testSuccess(self):
        paymentsJson = generateExampleBoletoPayments(n=5)
        content, status = postBoletoPayment(exampleMemberOld, paymentsJson=paymentsJson)
        print(content)
        if status != 200:
            code = content["errors"][0]["code"]
            self.assertEqual('immediatePaymentOutOfTime', code)
        else:
            self.assertEqual(200, status)

    def testFailInvalidArraySize(self):
        paymentsJson = generateExampleBoletoPayments(n=50)
        paymentsJson2 = generateExampleBoletoPayments(n=55)
        paymentsJson["payments"] = paymentsJson["payments"] + paymentsJson2["payments"]
        content, status = postBoletoPayment(exampleMemberOld, paymentsJson=paymentsJson)
        print(content)
        errors = content["errors"]
        self.assertEqual(1, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error["code"])

    def testFailInvalidJson(self):
        paymentsJson = {}
        content, status = postBoletoPayment(exampleMemberOld, paymentsJson=paymentsJson)
        print(content)
        errors = content["errors"]
        self.assertEqual(1, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error["code"])

    def testFailInvalidJsonPayment(self):
        paymentsJson = generateExampleBoletoPayments(n=4)
        paymentsJson["payments"][0].pop("line")
        paymentsJson["payments"][1].pop("scheduled")
        paymentsJson["payments"][2].pop("description")
        paymentsJson["payments"][3].pop("taxId")
        content, status = postBoletoPayment(exampleMemberOld, paymentsJson=paymentsJson)
        print(content)
        errors = content["errors"]
        for error in errors:
            print(error)
        self.assertTrue(len(errors) == 3 or len(errors) == 6)
        for error in errors:
            self.assertTrue(error["code"] in ["invalidJson", "invalidPayment", "immediatePaymentOutOfTime"])

    def testFailInvalidTaxId(self):
        paymentsJson = generateExampleBoletoPayments(n=5)
        paymentsJson["payments"][0]["taxId"] = "000.000.000-00"
        paymentsJson["payments"][1]["taxId"] = "00.000.000/0000-00"
        paymentsJson["payments"][2]["taxId"] = "abc"
        paymentsJson["payments"][3]["taxId"] = 123
        paymentsJson["payments"][4]["taxId"] = {}
        content, status = postBoletoPayment(exampleMemberOld, paymentsJson=paymentsJson)
        print(content)
        errors = content["errors"]
        for error in errors:
            print(error)
        self.assertTrue(len(errors) == 5 or len(errors) == 10)
        for error in errors:
            self.assertTrue(error["code"] in ["invalidTaxId", "immediatePaymentOutOfTime"])


class TestBoletoPaymentGet(TestCase):
    def testSuccess(self):
        content, status = getBoletoPayment(exampleMemberOld)
        self.assertEqual(200, status)
        payments = content["payments"]
        print("Number of payments:", len(payments))
        print(content)
        self.assertIsInstance(payments, list)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getBoletoPayment(exampleMemberOld, params=fieldsParams)
        self.assertEqual(200, status)
        for boleto in content["payments"]:
            self.assertTrue(set(boleto.keys()).issubset(fields))
        print(content)


class TestBoletoPaymentInfoGet(TestCase):
    def testSuccess(self):
        content, status = getBoletoPayment(exampleMemberOld)
        payments = content["payments"]
        paymentId = payments[0]["id"]
        content, status = getBoletoPaymentInfo(exampleMemberOld, paymentId=paymentId)
        print(content)
        self.assertEqual(200, status)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getBoletoPayment(exampleMemberOld)
        payments = content["payments"]
        paymentId = payments[0]["id"]
        content, status = getBoletoPaymentInfo(exampleMemberOld, paymentId=paymentId, params=fieldsParams)
        self.assertEqual(200, status)
        payment = content["payment"]
        print(content)
        self.assertTrue(set(payment.keys()).issubset(fields))


class TestBoletoPaymentPdfGet(TestCase):
    def testSuccess(self):
        content, status = getBoletoPayment(exampleMemberOld)
        payments = content["payments"]
        paymentId = payments[0]["id"]
        content, status = getBoletoPaymentPdf(exampleMemberOld, paymentId=paymentId)
        print(content)
        if status != 200:
            code = content["errors"][0]["code"]
            self.assertEqual('invalidTransfer', code)
        else:
            self.assertEqual(200, status)


if __name__ == '__main__':
    main()
