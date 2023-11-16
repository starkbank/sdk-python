import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestSplitLogQuery(TestCase):

    def test_success(self):
        logs = list(starkbank.split.log.query(limit=10))
        logs = list(starkbank.split.log.query(limit=10, split_ids={log.split.id for log in logs}, types={log.type for log in logs}))
        self.assertEqual(10, len(logs))
        print("Number of logs:", len(logs))


class TestSplitLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.split.log.page(limit=2, cursor=cursor)
            for log in logs:
                print(log)
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestSplitLogInfoGet(TestCase):

    def test_success(self):
        logs = starkbank.split.log.query()
        log_id = next(logs).id
        logs = starkbank.split.log.get(id=log_id)


if __name__ == '__main__':
    main()
