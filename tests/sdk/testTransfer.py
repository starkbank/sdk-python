import starkbank
from datetime import timedelta, date
from unittest import TestCase, main
from tests.utils.transfer import generateExampleTransfersJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestTransferPost(TestCase):

    def test_success(self):
        transfers = generateExampleTransfersJson(n=5)
        transfers = starkbank.transfer.create(transfers)
        for transfer in transfers:
            print(transfer.id)


class TestTransferGet(TestCase):

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
            transaction_ids=["1", "2", "3"],
        )
        self.assertEqual(len(list(transfers)), 0)


class TestTransferInfoGet(TestCase):
    def test_success(self):
        transfers = starkbank.transfer.query()
        transfer_id = next(transfers).id
        transfer = starkbank.transfer.get(id=transfer_id)
        self.assertIsNotNone(transfer.id)
        self.assertEqual(transfer.id, transfer_id)


class TestTransferPdfGet(TestCase):

    def test_success(self):
        transfers = starkbank.transfer.query(limit=1, status="success")
        transfer_id = next(transfers).id
        pdf = starkbank.transfer.pdf(id=transfer_id)
        self.assertGreater(len(pdf), 1000)


if __name__ == '__main__':
    main()
