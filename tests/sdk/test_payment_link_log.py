import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestPaymentLinkLogQuery(TestCase):

    def test_success(self):
        logs = list(starkbank.paymentlink.log.query(limit=10))
        logs = list(starkbank.paymentlink.log.query(
            limit=10,
            payment_link_ids={log.link.id for log in logs},
            types={log.type for log in logs},
        ))
        print("Number of logs:", len(logs))


class TestPaymentLinkLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.paymentlink.log.page(limit=2, cursor=cursor)
            for log in logs:
                print(log)
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestPaymentLinkLogGet(TestCase):

    def test_success(self):
        logs = starkbank.paymentlink.log.query()
        log_id = next(logs).id
        log = starkbank.paymentlink.log.get(id=log_id)
        self.assertIsNotNone(log.id)
        self.assertEqual(log.id, log_id)


if __name__ == '__main__':
    main()
