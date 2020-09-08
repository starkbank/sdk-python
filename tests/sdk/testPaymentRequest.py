import starkbank
from unittest import TestCase, main
from tests.utils.paymentRequest import generateExamplePaymentRequestsJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestPaymentRequestPost(TestCase):

    def test_success(self):
        requests = generateExamplePaymentRequestsJson(n=5)
        requests = starkbank.paymentrequest.create(requests)
        for request in requests:
            print(request)


if __name__ == '__main__':
    main()
