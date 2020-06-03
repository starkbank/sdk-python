import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestUtilityPaymentLogGet(TestCase):

    def test_success(self):
        logs = list(starkbank.utilitypayment.log.query(limit=10))
        logs = list(starkbank.utilitypayment.log.query(limit=10, payment_ids={log.payment.id for log in logs}, types={log.type for log in logs}))
        self.assertEqual(10, len(logs))
        print("Number of logs:", len(logs))


class TestUtilityPaymentLogInfoGet(TestCase):

    def test_success(self):
        logs = starkbank.utilitypayment.log.query()
        log_id = next(logs).id
        log = starkbank.utilitypayment.log.get(log_id)


if __name__ == '__main__':
    main()
