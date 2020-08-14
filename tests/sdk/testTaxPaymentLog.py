import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestTaxPaymentLogGet(TestCase):

    def test_success(self):
        logs = list(starkbank.taxpayment.log.query(limit=10))
        logs = list(starkbank.taxpayment.log.query(limit=10, payment_ids={log.payment.id for log in logs}, types={log.type for log in logs}))
        self.assertEqual(10, len(logs))
        print("Number of logs:", len(logs))


class TestTaxPaymentLogInfoGet(TestCase):

    def test_success(self):
        logs = starkbank.taxpayment.log.query()
        log_id = next(logs).id
        log = starkbank.taxpayment.log.get(log_id)


if __name__ == '__main__':
    main()
