import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestDepositLogQuery(TestCase):

    def test_success(self):
        logs = list(starkbank.deposit.log.query(limit=10))
        logs = list(starkbank.deposit.log.query(limit=10, deposit_ids={log.deposit.id for log in logs}, types={log.type for log in logs}))
        print("Number of logs:", len(logs))


class TestDepositLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.deposit.log.page(limit=2, cursor=cursor)
            for log in logs:
                print(log)
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestDepositLogInfoGet(TestCase):
    def test_success(self):
        logs = starkbank.deposit.log.query()
        log_id = next(logs).id
        log = starkbank.deposit.log.get(id=log_id)
        print(log)


class TestDepositLogPdfGet(TestCase):

    def test_success(self):
        logs = starkbank.deposit.log.query(types="reversed", limit=1)
        log_id = next(logs).id
        pdf = starkbank.deposit.log.pdf(log_id)
        self.assertGreater(len(pdf), 1000)


if __name__ == '__main__':
    main()
