import starkbank
from unittest import TestCase, main
from datetime import timedelta, date
from tests.utils.user import exampleProject
from tests.utils.transfer import generateExampleTransfersJson


starkbank.user = exampleProject


class TestTransferPost(TestCase):

    def test_success(self):
        transfers = generateExampleTransfersJson(n=5, randomSchedule=True)
        transfers = starkbank.transfer.create(transfers)
        self.assertEqual(len(transfers), 5)
        for transfer in transfers:
            self.assertIsNotNone(transfer.id)
            for rule in transfer.rules:
                if rule.key == "resendingLimit":
                    self.assertIsNotNone(rule.value)


class TestTransferQuery(TestCase):

    def test_success(self):
        transfers = list(starkbank.transfer.query(limit=10))
        assert len(transfers) == 10

    def test_success_with_params(self):
        transfers = starkbank.transfer.query(
            limit=10,
            after=date.today() - timedelta(days=100),
            before=date.today(),
            status="failed",
            tags=["iron", "bank"],
            tax_id="012.345.678-90",
            transaction_ids=["1", "2", "3"],
        )
        self.assertEqual(len(list(transfers)), 0)


class TestTransferPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            transfers, cursor = starkbank.transfer.page(limit=2, cursor=cursor)
            for transfer in transfers:
                print(transfer)
                self.assertFalse(transfer.id in ids)
                ids.append(transfer.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestTransferInfoGet(TestCase):

    def test_success(self):
        transfers = starkbank.transfer.query()
        transfer_id = next(transfers).id
        transfer = starkbank.transfer.get(id=transfer_id)
        self.assertIsNotNone(transfer.id)
        self.assertEqual(transfer.id, transfer_id)
    
    def test_success_ids(self):
        transfers = starkbank.transfer.query(limit=5)
        transfers_ids_expected = [t.id for t in transfers]
        transfers_ids_result = [t.id for t in starkbank.transfer.query(ids=transfers_ids_expected)]
        transfers_ids_expected.sort()
        transfers_ids_result.sort()
        self.assertTrue(transfers_ids_result)
        self.assertEqual(transfers_ids_expected, transfers_ids_result)


class TestTransferInfoDelete(TestCase):

    def test_success(self):
        transfers = generateExampleTransfersJson(n=1)
        transfers[0].scheduled = date.today() + timedelta(days=1)
        transfers = starkbank.transfer.create(transfers)
        transfer = starkbank.transfer.delete(transfers[0].id)
        self.assertIsNotNone(transfer.id)
        self.assertEqual(transfer.id, transfers[0].id)
        self.assertEqual(transfer.status, "canceled")


class TestTransferPdfGet(TestCase):

    def test_success(self):
        transfers = starkbank.transfer.query(limit=1, status="success")
        transfer_id = next(transfers).id
        pdf = starkbank.transfer.pdf(id=transfer_id)
        self.assertGreater(len(pdf), 1000)


if __name__ == '__main__':
    main()
