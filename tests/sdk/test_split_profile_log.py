import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestSplitProfileLogQuery(TestCase):

    def test_success(self):
        ids = []
        logs = list(starkbank.splitprofile.log.query(limit=10))
        for log in logs:
            print(log)
            self.assertFalse(log.id in ids)
            ids.append(log.id)
        self.assertTrue(len(ids) == 10)


class TestSplitProfileLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.splitprofile.log.page(limit=2, cursor=cursor)
            for log in logs:
                print(log)
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestSplitProfileLogInfoGet(TestCase):

    def test_success(self):
        logs = starkbank.splitprofile.log.query()
        log_id = next(logs).id
        log = starkbank.splitprofile.log.get(id=log_id)
        print(log)


if __name__ == '__main__':
    main()
