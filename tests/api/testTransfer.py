import starkbank
from datetime import timedelta, date, datetime
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.transfer import generateExampleTransfersJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestTransferPost(TestCase):

    def test_success(self):
        transfers = generateExampleTransfersJson(n=5, randomSchedule=True)
        transfers[0].scheduled = None
        transfers = starkbank.transfer.create(transfers)
        for transfer in transfers:
            print(transfer)
        if (datetime.utcnow() - timedelta(hours=3)).hour > 19:
            scheduled = (datetime.fromisoformat(transfers[0].scheduled) - timedelta(hours=3)).date()
            today = (datetime.utcnow() - timedelta(hours=3)).date()
            self.assertGreater(scheduled, today)

    def test_fail_invalid_array_size(self):
        transfers = generateExampleTransfersJson(n=105)
        with self.assertRaises(InputErrors) as context:
            transfers = starkbank.transfer.create(transfers)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual("invalidJson", error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json(self):
        transfers = {}
        with self.assertRaises(InputErrors) as context:
            transfers = starkbank.transfer.create(transfers)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual("invalidJson", error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json_transfer(self):
        transfers = generateExampleTransfersJson(n=6)
        transfers[0].tax_id = None
        transfers[1].amount = None
        transfers[2].name = None
        transfers[3].bank_code = None
        transfers[4].branch_code = None
        transfers[5].account_number = None
        with self.assertRaises(InputErrors) as context:
            transfers = starkbank.transfer.create(transfers)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(6, len(errors))

    def test_fail_invalid_tax_id(self):
        transfers = generateExampleTransfersJson(n=5)
        transfers[0].tax_id = "000.000.000-00"
        transfers[1].tax_id = "00.000.000/0000-00"
        transfers[2].tax_id = "abc"
        transfers[3].tax_id = 123  # 2 errors
        transfers[4].tax_id = {}  # 2 errors
        with self.assertRaises(InputErrors) as context:
            transfers = starkbank.transfer.create(transfers)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidTaxId', error.code)
        self.assertEqual(5, len(errors))

    def test_fail_invalid_amount(self):
        transfers = generateExampleTransfersJson(n=5)
        transfers[0].amount = "123"
        transfers[1].amount = -5
        transfers[2].amount = 0
        transfers[3].amount = 1000000000000000
        transfers[4].amount = {}
        with self.assertRaises(InputErrors) as context:
            transfers = starkbank.transfer.create(transfers)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidAmount', error.code)
        self.assertEqual(5, len(errors))

    def test_fail_invalid_scheduled(self):
        transfers = generateExampleTransfersJson(n=1)
        transfers[0].scheduled = datetime.now() - timedelta(days=1)
        with self.assertRaises(InputErrors) as context:
            transfers = starkbank.transfer.create(transfers)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertTrue(error.code in ["invalidDate", "invalidDateTime"])
        self.assertEqual(1, len(errors))


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
            tax_id="012.345.678-90",
            transaction_ids=["1", "2", "3"],
        )
        for transfer in transfers:
            print(transfer.id)


class TestTransferInfoGet(TestCase):
    def test_success(self):
        transfers = starkbank.transfer.query(user=exampleProject)
        transfer_id = next(transfers).id
        transfer = starkbank.transfer.get(id=transfer_id)

    def test_fail_invalid_transfer(self):
        transfer_id = "0"
        with self.assertRaises(InputErrors) as context:
            transfer = starkbank.transfer.get(id=transfer_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidTransfer', error.code)
        self.assertEqual(1, len(errors))


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
        transfers = starkbank.transfer.query(user=exampleProject)
        transfer_id = next(transfers).id
        try:
            pdf = starkbank.transfer.pdf(id=transfer_id)
            self.assertGreater(len(pdf), 1000)
        except InputErrors as e:
            errors = e.errors
            for error in errors:
                self.assertEqual("invalidTransfer", error.code)


if __name__ == '__main__':
    main()
