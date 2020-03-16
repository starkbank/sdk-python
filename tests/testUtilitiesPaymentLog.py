from unittest import TestCase, main

import starkbank
from starkbank.exception import InputErrors
from tests.utils.user import exampleProject

starkbank.user = exampleProject


class TestUtilityPaymentLogGet(TestCase):

    def test_success(self):
        logs = list(starkbank.payment.utility.log.query(limit=10))
        print("Number of logs:", len(logs))


class TestUtilityPaymentLogInfoGet(TestCase):

    def test_success(self):
        logs = starkbank.payment.utility.log.query()
        log_id = next(logs).id
        log = starkbank.payment.utility.log.get(log_id)

    def test_fail_invalid_log(self):
        log_id = "0"
        with self.assertRaises(InputErrors) as context:
            log = starkbank.payment.utility.log.get(log_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidPaymentLog', error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
