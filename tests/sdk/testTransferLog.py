import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestTransferLogGet(TestCase):

    def test_success(self):
        logs = list(starkbank.transfer.log.query(limit=10))
        logs = list(starkbank.transfer.log.query(limit=10, transfer_ids={log.transfer.id for log in logs}, types={log.type for log in logs}))
        self.assertEqual(10, len(logs))
        print("Number of logs:", len(logs))


class TestTransferLogInfoGet(TestCase):
    def test_success(self):
        logs = starkbank.transfer.log.query()
        log_id = next(logs).id
        logs = starkbank.transfer.log.get(id=log_id)


if __name__ == '__main__':
    main()
