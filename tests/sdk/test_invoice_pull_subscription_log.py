import starkbank
from datetime import datetime, timedelta
from unittest import TestCase, main
from tests.utils.date import randomPastDate
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestInvoicePullSubscriptionLogQuery(TestCase):

    def test_success(self):
        logs = list(starkbank.invoicepullsubscription.log.query(limit=10))
        print(f"Number of InvoicePullSubscription logs: {len(logs)}")
        for log in logs:
            self.assertIsNotNone(log.id)
            self.assertIsNotNone(log.subscription.id)
            print(log)

    def test_success_with_filters(self):
        after = randomPastDate(days=10)
        before = datetime.today()
        logs = starkbank.invoicepullsubscription.log.query(
            after=after.date(),
            before=before.date(),
            limit=10
        )
        for log in logs:
            self.assertTrue(after.date() <= log.created.date() <= (before + timedelta(hours=3)).date())
            print(log)


class TestInvoicePullSubscriptionLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.invoicepullsubscription.log.page(limit=2, cursor=cursor)
            for log in logs:
                print(log)
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        print(f"Total unique InvoicePullSubscription logs: {len(ids)}")


class TestInvoicePullSubscriptionLogGet(TestCase):

    def test_success(self):
        logs = starkbank.invoicepullsubscription.log.query(limit=1)
        for log in logs:
            log_id = log.id
            log = starkbank.invoicepullsubscription.log.get(log_id)
            self.assertEqual(log.id, log_id)
            print(log)
            break


if __name__ == '__main__':
    main()
