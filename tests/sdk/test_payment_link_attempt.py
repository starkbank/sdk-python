import starkbank
from datetime import date, timedelta
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestPaymentLinkAttemptQuery(TestCase):

    def test_success(self):
        attempts = list(starkbank.paymentlink.attempt.query(limit=10))
        print("Number of attempts:", len(attempts))
        for attempt in attempts:
            self.assertIsNotNone(attempt.id)
            self.assertIsNotNone(attempt.payment_link_id)

    def test_success_with_params(self):
        attempts = starkbank.paymentlink.attempt.query(
            limit=10,
            after=date.today() - timedelta(days=100),
            before=date.today(),
            status="success",
            payment_link_ids=["1", "2", "3"],
            ids=["1", "2", "3"],
        )
        self.assertEqual(len(list(attempts)), 0)


class TestPaymentLinkAttemptPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            attempts, cursor = starkbank.paymentlink.attempt.page(limit=2, cursor=cursor)
            for attempt in attempts:
                print(attempt)
                self.assertFalse(attempt.id in ids)
                ids.append(attempt.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestPaymentLinkAttemptGet(TestCase):

    def test_success(self):
        attempts = starkbank.paymentlink.attempt.query()
        attempt_id = next(attempts).id
        attempt = starkbank.paymentlink.attempt.get(id=attempt_id)
        self.assertIsNotNone(attempt.id)
        self.assertEqual(attempt.id, attempt_id)


if __name__ == '__main__':
    main()
