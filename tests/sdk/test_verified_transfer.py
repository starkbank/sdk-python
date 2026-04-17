import uuid
import starkbank
from unittest import TestCase, main
from datetime import datetime, timedelta
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestVerifiedTransferPost(TestCase):

    def test_success(self):
        accounts = list(starkbank.verifiedaccount.query(limit=1, status="active"))
        if not accounts:
            return
        account_id = accounts[0].id
        verified_transfers = starkbank.verifiedtransfer.create([
            starkbank.VerifiedTransfer(
                amount=1234,
                account_id=account_id,
            )
        ])
        self.assertEqual(len(verified_transfers), 1)
        transfer = verified_transfers[0]
        self.assertIsNotNone(transfer.id)
        self.assertIsNotNone(transfer.status)
        self.assertIsNotNone(transfer.created)
        self.assertIn(transfer.status, ["created", "processing", "success", "failed"])

    def test_success_with_optional_params(self):
        accounts = list(starkbank.verifiedaccount.query(limit=1, status="active"))
        if not accounts:
            return
        account_id = accounts[0].id
        verified_transfers = starkbank.verifiedtransfer.create([
            starkbank.VerifiedTransfer(
                amount=5000,
                account_id=account_id,
                description="Payment for service #1234",
                display_description="Service payment",
                tags=["employees", "monthly"],
                rules=[starkbank.transfer.Rule(key="resendingLimit", value=5)],
            )
        ])
        self.assertEqual(len(verified_transfers), 1)
        transfer = verified_transfers[0]
        self.assertIsNotNone(transfer.id)
        self.assertIsNotNone(transfer.status)
        self.assertIsNotNone(transfer.created)
        for rule in transfer.rules:
            if rule.key == "resendingLimit":
                self.assertEqual(rule.value, 5)

    def test_success_with_external_id(self):
        accounts = list(starkbank.verifiedaccount.query(limit=1, status="active"))
        if not accounts:
            return
        account_id = accounts[0].id
        external_id = str(uuid.uuid4())
        verified_transfers = starkbank.verifiedtransfer.create([
            starkbank.VerifiedTransfer(
                amount=100,
                account_id=account_id,
                external_id=external_id,
            )
        ])
        self.assertEqual(len(verified_transfers), 1)
        self.assertIsNotNone(verified_transfers[0].id)

    def test_success_with_scheduled(self):
        accounts = list(starkbank.verifiedaccount.query(limit=1, status="active"))
        if not accounts:
            return
        account_id = accounts[0].id
        scheduled = datetime.now() + timedelta(days=1)
        verified_transfers = starkbank.verifiedtransfer.create([
            starkbank.VerifiedTransfer(
                amount=200,
                account_id=account_id,
                scheduled=scheduled,
            )
        ])
        self.assertEqual(len(verified_transfers), 1)
        self.assertIsNotNone(verified_transfers[0].id)


if __name__ == '__main__':
    main()
