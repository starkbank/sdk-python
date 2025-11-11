import starkbank
from unittest import TestCase, main
from tests.utils.invoice import generateExampleInvoicesJson
from tests.utils.invoicePullRequest import generateExampleInvoicePullRequestJson
from tests.utils.invoicePullSubscription import generateExampleInvoicePullSubscriptionsJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestInvoicePullRequestCreate(TestCase):

    def test_success(self):
        invoices = starkbank.invoice.create(generateExampleInvoicesJson(n=1))
        invoice_id = invoices[0].id
        subscriptions = starkbank.invoicepullsubscription.create(generateExampleInvoicePullSubscriptionsJson(n=1, type="qrcodeAndPayment"))
        subscription_id = subscriptions[0].id
        request = starkbank.invoicepullrequest.create([generateExampleInvoicePullRequestJson(
            invoice_id=invoice_id,
            subscription_id=subscription_id
        )])
        self.assertIsNotNone(request.id)


class TestInvoicePullRequestQuery(TestCase):

    def test_success(self):
        requests = list(starkbank.invoicepullrequest.query(limit=5))
        i = 0
        for request in requests:
            i += 1
            self.assertIsNotNone(request.id)
        self.assertEqual(i, 5)


class TestInvoicePullRequestPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            requests, cursor = starkbank.invoicepullrequest.page(limit=2, cursor=cursor)
            for request in requests:
                self.assertFalse(request.id in ids)
                ids.append(request.id)
            if cursor is None:
                break


class TestInvoicePullRequestGet(TestCase):

    def test_success(self):
        requests = starkbank.invoicepullrequest.query(limit=1)
        for request in requests:
            request_id = request.id
            request = starkbank.invoicepullrequest.get(request_id)
            self.assertEqual(request.id, request_id)
            break


if __name__ == '__main__':
    main()
