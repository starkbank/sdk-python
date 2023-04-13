import starkbank
from unittest import TestCase, main
from starkcore.error import InputErrors
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestDarfPaymentLogGet(TestCase):

    def test_success(self):
        logs = list(starkbank.darfpayment.log.query(limit=10))
        logs = list(starkbank.darfpayment.log.query(limit=10, payment_ids={log.payment.id for log in logs}, types={log.type for log in logs}))
        for log in logs:
            print(log)
        print("Number of logs:", len(logs))


class TestDarfPaymentLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.darfpayment.log.page(limit=2, cursor=cursor)
            for log in logs:
                print(log)
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestDarfPaymentLogInfoGet(TestCase):

    def test_success(self):
        logs = starkbank.darfpayment.log.query()
        log_id = next(logs).id
        log = starkbank.darfpayment.log.get(log_id)


if __name__ == '__main__':
    main()
