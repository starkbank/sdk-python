import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBrcodePaymentLogQuery(TestCase):

    def test_success(self):
        logs = list(starkbank.brcodepayment.log.query(limit=10))
        logs = list(starkbank.brcodepayment.log.query(limit=10, payment_ids={log.payment.id for log in logs}, types={log.type for log in logs}))
        self.assertEqual(len(logs), 10)
        for log in logs:
            print(log)


class TestBrcodePaymentLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.brcodepayment.log.page(limit=2, cursor=cursor)
            for log in logs:
                print(log)
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestBrcodePaymentLogInfoGet(TestCase):

    def test_success(self):
        logs = starkbank.brcodepayment.log.query()
        log_id = next(logs).id
        log = starkbank.brcodepayment.log.get(log_id)
        self.assertIsNotNone(log.id)
        self.assertEqual(log.id, log_id)


if __name__ == '__main__':
    main()
