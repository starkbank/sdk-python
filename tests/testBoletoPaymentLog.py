import starkbank
from unittest import TestCase, main

starkbank.debug = True


class TestBoletoPaymentLogGet(TestCase):

    def testSuccess(self):
        logs = list(starkbank.payment.boleto.log.query(limit=10))
        print("Number of logs:", len(logs))


class TestBoletoPaymentLogInfoGet(TestCase):
    def testSuccess(self):
        logs = starkbank.payment.boleto.log.query()
        logId = next(logs).id
        logs = starkbank.payment.boleto.log.get(logId)

    def testFailInvalidLog(self):
        logId = "0"
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            log = starkbank.payment.boleto.log.get(logId)
        errors = context.exception.elements
        for error in errors:
            print(error)
            self.assertEqual('invalidPaymentLog', error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
