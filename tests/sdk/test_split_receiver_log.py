import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestSplitReceiverLogQuery(TestCase):

    def test_success(self):
        logs = list(starkbank.splitreceiver.log.query(limit=10))
        logs = list(starkbank.splitreceiver.log.query(limit=10, receiver_ids={log.receiver.id for log in logs}, types={log.type for log in logs}))
        self.assertEqual(10, len(logs))
        print("Number of logs:", len(logs))


class TestSplitReceiverLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.splitreceiver.log.page(limit=2, cursor=cursor)
            for log in logs:
                print(log)
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestSplitReceiverLogInfoGet(TestCase):

    def test_success(self):
        logs = starkbank.splitreceiver.log.query()
        log_id = next(logs).id
        logs = starkbank.splitreceiver.log.get(id=log_id)


if __name__ == '__main__':
    main()
