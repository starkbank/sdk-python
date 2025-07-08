import starkbank
from datetime import datetime, timedelta
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestInvoicePullRequestQuery(TestCase):

    def test_success(self):
        requests = list(starkbank.invoicepullrequest.query(limit=5))
        print(f"Number of InvoicePullRequests: {len(requests)}")
        for request in requests:
            self.assertIsNotNone(request.id)
            print(request)


class TestInvoicePullRequestPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            requests, cursor = starkbank.invoicepullrequest.page(limit=2, cursor=cursor)
            for request in requests:
                print(request)
                self.assertFalse(request.id in ids)
                ids.append(request.id)
            if cursor is None:
                break
        print(f"Total unique InvoicePullRequests: {len(ids)}")


class TestInvoicePullRequestGet(TestCase):

    def test_success(self):
        requests = starkbank.invoicepullrequest.query(limit=1)
        for request in requests:
            request_id = request.id
            request = starkbank.invoicepullrequest.get(request_id)
            self.assertEqual(request.id, request_id)
            print(request)
            break


if __name__ == '__main__':
    main() 