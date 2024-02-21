import starkbank
from unittest import TestCase, main
from tests.utils.paymentRequest import generateExamplePaymentRequestsJson, center_id
from tests.utils.user import exampleProject
from tests.utils.date import randomPastDate
from datetime import datetime, timedelta


starkbank.user = exampleProject


class TestPaymentRequestPost(TestCase):

    def test_success(self):
        requests = generateExamplePaymentRequestsJson(n=7)
        requests = starkbank.paymentrequest.create(requests)
        self.assertEqual(len(requests), 7)
        for request in requests:
            print(request)


class TestPaymentRequestQuery(TestCase):
    
    def test_success_after_before(self):
        after = randomPastDate(days=10)
        before = datetime.today()
        requests = starkbank.paymentrequest.query(center_id=center_id, after=after, before=before)
        self.assertTrue(requests)
        i = 0
        for i, request in enumerate(requests):
            self.assertTrue(after.date() <= request.created.date() <= (before + timedelta(hours=3)).date())
            if i >= 200:
                break
        print("Number of payment requests:", i)


class TestPaymentRequestPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            requests, cursor = starkbank.paymentrequest.page(center_id=center_id, limit=2, cursor=cursor)
            for request in requests:
                print(request)
                self.assertFalse(request.id in ids)
                ids.append(request.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


if __name__ == '__main__':
    main()
