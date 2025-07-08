import starkbank
from datetime import datetime, timedelta
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestInvoicePullSubscriptionQuery(TestCase):

    def test_success(self):
        subscriptions = list(starkbank.invoicepullsubscription.query(limit=5))
        print(f"Number of InvoicePullSubscriptions: {len(subscriptions)}")
        for subscription in subscriptions:
            self.assertIsNotNone(subscription.id)
            print(subscription)


class TestInvoicePullSubscriptionPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            subscriptions, cursor = starkbank.invoicepullsubscription.page(limit=2, cursor=cursor)
            for subscription in subscriptions:
                print(subscription)
                self.assertFalse(subscription.id in ids)
                ids.append(subscription.id)
            if cursor is None:
                break
        print(f"Total unique InvoicePullSubscriptions: {len(ids)}")


class TestInvoicePullSubscriptionGet(TestCase):

    def test_success(self):
        subscriptions = starkbank.invoicepullsubscription.query(limit=1)
        for subscription in subscriptions:
            subscription_id = subscription.id
            subscription = starkbank.invoicepullsubscription.get(subscription_id)
            self.assertEqual(subscription.id, subscription_id)
            print(subscription)
            break


if __name__ == '__main__':
    main() 