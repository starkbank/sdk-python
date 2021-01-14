import starkbank
from unittest import TestCase, main
from tests.utils.paymentRequest import generateExamplePaymentRequestsJson, center_id
from tests.utils.user import exampleProject
from tests.utils.date import randomPastDate
from datetime import datetime, timedelta


starkbank.user = exampleProject


class TestPaymentRequestPost(TestCase):

    def test_success(self):
        requests = generateExamplePaymentRequestsJson(n=5)
        requests = starkbank.paymentrequest.create(requests)
        self.assertEqual(len(requests), 5)
        for request in requests:
            print(request)


class TestPaymentRequestGet(TestCase):
    
    def test_success(self):
        requests = list(starkbank.paymentrequest.query(center_id=center_id))
        self.assertTrue(requests)
        print("Number of payment requests:", len(requests))

    def test_success_after_before(self):
        after = randomPastDate(days=10)
        before = datetime.today()
        requests = starkbank.paymentrequest.query(center_id=center_id, after=after.date(), before=before.date())
        self.assertTrue(requests)
        i = 0
        for i, request in enumerate(requests):
            self.assertTrue(after.date() <= request.created.date() <= (before + timedelta(hours=3)).date())
            if i >= 200:
                break
        print("Number of payment requests:", i)


if __name__ == '__main__':
    main()
