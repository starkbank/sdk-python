from time import sleep
import starkbank
from datetime import timedelta, date
from unittest import TestCase, main
from tests.utils.user import exampleProject
from tests.utils.split import generateExampleSplittedInvoices, paySplittedInvoices


starkbank.user = exampleProject


class TestSplitPost(TestCase):

    def test_success(self):
        invoices = generateExampleSplittedInvoices(n=1)
        payments = paySplittedInvoices(invoices)
        for invoice in invoices:
            print(invoice)
        for payment in payments:
            print(payment)
        isInvoicePaid = False
        while not isInvoicePaid:
            for invoice in invoices:
                if starkbank.invoice.get(invoice.id).status == "paid":
                    isInvoicePaid = True
                sleep(2)
        splits = list(starkbank.split.query(tags=["invoice/{id}".format(id=invoice.id) for invoice in invoices]))
        for split in splits:
            print(split)
            self.assertIsNotNone(split.id)


class TestSplitQuery(TestCase):

    def test_success(self):
        splits = list(starkbank.split.query(limit=10))
        assert len(splits) == 10

    def test_success_with_params(self):
        splits = starkbank.split.query(
            limit=10,
            after=date.today() - timedelta(days=100),
            before=date.today(),
            status="success",
            tags=["iron", "bank"],
        )
        self.assertEqual(len(list(splits)), 0)


class TestSplitPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            splits, cursor = starkbank.split.page(limit=2, cursor=cursor)
            for split in splits:
                print(split)
                self.assertFalse(split.id in ids)
                ids.append(split.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestSplitInfoGet(TestCase):

    def test_success(self):
        splits = starkbank.split.query()
        split_id = next(splits).id
        split = starkbank.split.get(id=split_id)
        self.assertIsNotNone(split.id)
        self.assertEqual(split.id, split_id)
    
    def test_success_ids(self):
        splits = starkbank.split.query(limit=5)
        splits_ids_expected = [t.id for t in splits]
        splits_ids_result = [t.id for t in starkbank.split.query(ids=splits_ids_expected)]
        splits_ids_expected.sort()
        splits_ids_result.sort()
        self.assertTrue(splits_ids_result)
        self.assertEqual(splits_ids_expected, splits_ids_result)


if __name__ == '__main__':
    main()
