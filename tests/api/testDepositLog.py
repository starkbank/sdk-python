import starkbank
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestDepositLogGet(TestCase):

    def test_success(self):
        logs = list(starkbank.deposit.log.query(limit=10))
        logs = list(starkbank.deposit.log.query(limit=10, deposit_ids={log.deposit.id for log in logs}, types={log.type for log in logs}))
        print("Number of logs:", len(logs))


class TestDepositLogInfoGet(TestCase):
    def test_success(self):
        logs = starkbank.deposit.log.query()
        log_id = next(logs).id
        logs = starkbank.deposit.log.get(id=log_id)

    def test_fail_invalid_log(self):
        log_id = "123"
        with self.assertRaises(InputErrors) as context:
            log = starkbank.deposit.log.get(id=log_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidDepositLog', error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
