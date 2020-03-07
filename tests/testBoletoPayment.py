import starkbank
from unittest import TestCase, main

from tests.utils.boletoPayment import generateExampleBoletoPaymentsJson
from tests.utils.user import exampleProject


class TestBoletoPaymentPost(TestCase):

    def testSuccess(self):
        payments = generateExampleBoletoPaymentsJson(n=5)
        payments = starkbank.boleto_payment.create(user=exampleProject, payments=payments)

    def testFailInvalidArraySize(self):
        payments = generateExampleBoletoPaymentsJson(n=50)
        payments2 = generateExampleBoletoPaymentsJson(n=55)
        payments = payments + payments2
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            payments = starkbank.boleto_payment.create(user=exampleProject, payments=payments)
        errors = context.exception.elements
        for error in errors:
            print(errors)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def testFailInvalidJson(self):
        payments = {}
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            payments = starkbank.boleto_payment.create(user=exampleProject, payments=payments)
        errors = context.exception.elements
        for error in errors:
            print(errors)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def testFailInvalidJsonPayment(self):
        payments = generateExampleBoletoPaymentsJson(n=4)
        payments[0].line = None
        payments[1].scheduled = None
        payments[2].description = None
        payments[3].tax_id = None
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            payments = starkbank.boleto_payment.create(user=exampleProject, payments=payments)
        errors = context.exception.elements
        for error in errors:
            print(error)
            self.assertTrue(error.code in ["invalidJson", "invalidPayment", "immediatePaymentOutOfTime"])
        self.assertTrue(len(errors) == 3 or len(errors) == 6)

    def testFailInvalidTaxId(self):
        payments = generateExampleBoletoPaymentsJson(n=5)
        payments[0].tax_id = "000.000.000-00"
        payments[1].tax_id = "00.000.000/0000-00"
        payments[2].tax_id = "abc"
        payments[3].tax_id = 123
        payments[4].tax_id = {}
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            payments = starkbank.boleto_payment.create(user=exampleProject, payments=payments)
        errors = context.exception.elements
        for error in errors:
            print(error)
            self.assertTrue(error.code in ["invalidTaxId", "immediatePaymentOutOfTime"])
        self.assertTrue(len(errors) == 5 or len(errors) == 10)


class TestBoletoPaymentGet(TestCase):
    def testSuccess(self):
        payments, cursor = starkbank.boleto_payment.list(user=exampleProject)
        print("Number of payments:", len(payments))

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     payments = starkbank.boleto_payment.list(user=exampleMember, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     for payment in payments:
    #         self.assertTrue(set(payments.keys()).issubset(fields))


class TestBoletoPaymentInfoGet(TestCase):
    def testSuccess(self):
        payments, cursor = starkbank.boleto_payment.list(user=exampleProject)
        paymentId = payments[0].id
        payment = starkbank.boleto_payment.retrieve(user=exampleProject, id=paymentId)

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     payments = starkbank.boleto_payment.list(user=exampleMember)
    #     paymentId = payments[0].id
    #     payments = starkbank.boleto_payment.retrieve(user=exampleMember, id=paymentId, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     payment = content["payment"]
    #     print(content)
    #     self.assertTrue(set(payment.keys()).issubset(fields))


class TestBoletoPaymentPdfGet(TestCase):
    def testSuccess(self):
        payments, cursor = starkbank.boleto_payment.list(user=exampleProject)
        paymentId = payments[0].id
        payments = starkbank.boleto_payment.retrieve_pdf(user=exampleProject, id=paymentId)


if __name__ == '__main__':
    main()
