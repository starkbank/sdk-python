import starkbank
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBoletoPaymentLogGet(TestCase):

    def test_success(self):
        logs = list(starkbank.boletopayment.log.query(limit=10))
        logs = list(starkbank.boletopayment.log.query(limit=10, payment_ids={log.payment.id for log in logs}, types={log.type for log in logs}))
        print("Number of logs:", len(logs))

    def test_fail(self):
        with self.assertRaises(InputErrors) as context:
            list(starkbank.boletopayment.log.query(limit=10, types=["random"]))
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidPaymentLog', error.code)


class TestBoletoPaymentLogInfoGet(TestCase):

    def test_success(self):
        logs = starkbank.boletopayment.log.query()
        log_id = next(logs).id
        log = starkbank.boletopayment.log.get(log_id)

    def test_fail_invalid_log(self):
        log_id = "0"
        with self.assertRaises(InputErrors) as context:
            log = starkbank.boletopayment.log.get(log_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidPaymentLog', error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
