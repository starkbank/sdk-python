import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject

starkbank.user = exampleProject


class TestCorporateHolderLogQuery(TestCase):

    def test_success(self):
        logs = starkbank.corporateholder.log.query(limit=10)
        for log in logs:
            self.assertEqual(log.id, str(log.id))


class TestCorporateHolderLogGet(TestCase):

    def test_success(self):
        logs = starkbank.corporateholder.log.query(limit=1)
        log = starkbank.corporateholder.log.get(id=next(logs).id)
        self.assertEqual(log.id, str(log.id))


class TestCorporateHolderLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.corporateholder.log.page(limit=2, cursor=cursor)
            for log in logs:
                print(log)
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


if __name__ == '__main__':
    main()
