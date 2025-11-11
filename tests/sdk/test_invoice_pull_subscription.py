import starkbank
from unittest import TestCase, main
from tests.utils.invoicePullSubscription import generateExampleInvoicePullSubscriptionsJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestInvoicePullSubscriptionCreate(TestCase):

    def test_success_push(self):
        subscriptions = generateExampleInvoicePullSubscriptionsJson(n=1, type="push")
        subscriptions = starkbank.invoicepullsubscription.create(subscriptions)

        for subscription in subscriptions:
            self.assertIsNotNone(subscription.id)
    
    def test_success_qrcode(self):
        subscriptions = generateExampleInvoicePullSubscriptionsJson(n=1, type="qrcode")
        subscriptions = starkbank.invoicepullsubscription.create(subscriptions)

        for subscription in subscriptions:
            self.assertIsNotNone(subscription.id)
    
    def test_success_qrcode_and_payment(self):
        subscriptions = generateExampleInvoicePullSubscriptionsJson(n=1, type="qrcodeAndPayment")
        subscriptions = starkbank.invoicepullsubscription.create(subscriptions)

        for subscription in subscriptions:
            self.assertIsNotNone(subscription.id)
    
    def test_success_payment_and_or_qrcode(self):
        subscriptions = generateExampleInvoicePullSubscriptionsJson(n=1, type="paymentAndOrQrcode")
        subscriptions = starkbank.invoicepullsubscription.create(subscriptions)

        for subscription in subscriptions:
            self.assertIsNotNone(subscription.id)

class TestInvoicePullSubscriptionQuery(TestCase):

    def test_success(self):
        subscriptions = list(starkbank.invoicepullsubscription.query(limit=5))
        i = 0
        for subscription in subscriptions:
            i += 1
            self.assertIsNotNone(subscription.id)
        self.assertEqual(i, 5)


class TestInvoicePullSubscriptionPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            subscriptions, cursor = starkbank.invoicepullsubscription.page(limit=2, cursor=cursor)
            for subscription in subscriptions:
                self.assertFalse(subscription.id in ids)
                ids.append(subscription.id)
            if cursor is None:
                break


class TestInvoicePullSubscriptionGet(TestCase):

    def test_success(self):
        subscriptions = starkbank.invoicepullsubscription.query(limit=1)
        for subscription in subscriptions:
            subscription_id = subscription.id
            subscription = starkbank.invoicepullsubscription.get(subscription_id)
            self.assertEqual(subscription.id, subscription_id)
            break


if __name__ == '__main__':
    main()
