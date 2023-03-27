import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestUtilityPaymentLogQuery(TestCase):

    def test_success(self):
        logs = list(starkbank.utilitypayment.log.query(limit=10))
        logs = list(starkbank.utilitypayment.log.query(limit=10, payment_ids={log.payment.id for log in logs}, types={log.type for log in logs}))
        self.assertEqual(10, len(logs))
        print("Number of logs:", len(logs))


class TestUtilityPaymentLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.utilitypayment.log.page(limit=2, cursor=cursor)
            for log in logs:
                print(log)
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestUtilityPaymentLogInfoGet(TestCase):

    def test_success(self):
        logs = starkbank.utilitypayment.log.query()
        log_id = next(logs).id
        log = starkbank.utilitypayment.log.get(log_id)


if __name__ == '__main__':
    main()
