import starkbank
from starkbank.exceptions import InputError
from unittest import TestCase, main


class TestBoletoPaymentLogGet(TestCase):

    def test_success(self):
        logs = list(starkbank.payment.boleto.log.query(limit=10))
        print("Number of logs:", len(logs))


class TestBoletoPaymentLogInfoGet(TestCase):
    def test_success(self):
        logs = starkbank.payment.boleto.log.query()
        logId = next(logs).id
        logs = starkbank.payment.boleto.log.get(logId)

    def test_fail_invalid_log(self):
        logId = "0"
        with self.assertRaises(InputError) as context:
            log = starkbank.payment.boleto.log.get(logId)
        errors = context.exception.elements
        for error in errors:
            print(error)
            self.assertEqual('invalidPaymentLog', error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
