import starkbank
from datetime import date, timedelta
from unittest import TestCase, main
from tests.utils.user import exampleProject
from tests.utils.paymentLink import generateExamplePaymentLinksJson


starkbank.user = exampleProject


class TestPaymentLinkPost(TestCase):

    def test_success(self):
        links = generateExamplePaymentLinksJson(n=5)
        links = starkbank.paymentlink.create(links)
        self.assertEqual(len(links), 5)
        for link in links:
            self.assertIsNotNone(link.id)
            print(link)


class TestPaymentLinkQuery(TestCase):

    def test_success(self):
        links = list(starkbank.paymentlink.query(limit=10))
        assert len(links) == 10

    def test_success_with_params(self):
        links = starkbank.paymentlink.query(
            limit=10,
            after=date.today() - timedelta(days=100),
            before=date.today(),
            status="active",
            tags=["sdk-test", "payment-link"],
            ids=["1", "2", "3"],
        )
        self.assertEqual(len(list(links)), 0)


class TestPaymentLinkPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            links, cursor = starkbank.paymentlink.page(limit=2, cursor=cursor)
            for link in links:
                print(link)
                self.assertFalse(link.id in ids)
                ids.append(link.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestPaymentLinkGet(TestCase):

    def test_success(self):
        links = starkbank.paymentlink.query()
        link_id = next(links).id
        link = starkbank.paymentlink.get(id=link_id)
        self.assertIsNotNone(link.id)
        self.assertEqual(link.id, link_id)


class TestPaymentLinkUpdate(TestCase):

    def test_success_cancel(self):
        links = starkbank.paymentlink.query(status="active", limit=1)
        for link in links:
            self.assertIsNotNone(link.id)
            updated_link = starkbank.paymentlink.update(link.id, status="canceling")
            self.assertEqual(updated_link.status, "canceling")


if __name__ == '__main__':
    main()
