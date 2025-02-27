import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestCorporateCardLogQuery(TestCase):

    def test_success(self):
        logs = starkbank.corporatecard.log.query(limit=5)
        for log in logs:
            self.assertEqual(log.id, str(log.id))


class TestCorporateCardLogGet(TestCase):

    def test_success(self):
        logs = starkbank.corporatecard.log.query(limit=1, types=["created"])
        log = starkbank.corporatecard.log.get(id=next(logs).id)
        self.assertEqual(log.id, str(log.id))


class TestCorporateCardLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.corporatecard.log.page(limit=2, cursor=cursor)
            for log in logs:
                print(log)
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


if __name__ == '__main__':
    main()
