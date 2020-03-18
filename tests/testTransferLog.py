from unittest import TestCase, main

import starkbank
from starkbank.exception import InputErrors
from tests.utils.user import exampleProject

starkbank.user = exampleProject


class TestTransferLogGet(TestCase):

    def test_success(self):
        logs = starkbank.transfer.log.query(limit=10)
        logs = list(starkbank.transfer.log.query(limit=10, transfer_ids={log.transfer.id for log in logs},
                                                 types={log.type for log in logs}))
        print("Number of logs:", len(logs))


class TestTransferLogInfoGet(TestCase):
    def test_success(self):
        logs = starkbank.transfer.log.query()
        log_id = next(logs).id
        logs = starkbank.transfer.log.get(id=log_id)

    def test_fail_invalid_log(self):
        log_id = "0"
        with self.assertRaises(InputErrors) as context:
            log = starkbank.transfer.log.get(id=log_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidTransferLog', error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
