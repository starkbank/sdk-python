import starkbank
from unittest import TestCase, main
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
        log = starkbank.deposit.log.get(id=log_id)
        print(log)


if __name__ == '__main__':
    main()
