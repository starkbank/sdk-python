import starkbank
from unittest import TestCase, main
from tests.utils.verifiedAccount import generateExampleBankInfoVerifiedAccountJson
from tests.utils.verifiedTransfer import generateExampleVerifiedTransferJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestVerifiedTransferCreate(TestCase):

    def test_success(self):
        accounts = starkbank.verifiedaccount.create([generateExampleBankInfoVerifiedAccountJson()])
        account_id = accounts[0].id

        example = generateExampleVerifiedTransferJson(account_id)
        transfers = starkbank.verifiedtransfer.create([example])
        self.assertEqual(len(transfers), 1)
        transfer = transfers[0]
        self.assertIsNotNone(transfer.id)
        self.assertEqual(transfer.amount, example.amount)
        self.assertIsNotNone(transfer.status)

        self.assertTrue(len(transfer.rules) > 0)
        resending_limit_rule = None
        for rule in transfer.rules:
            if rule.key == "resendingLimit":
                resending_limit_rule = rule
        self.assertIsNotNone(resending_limit_rule)
        self.assertEqual(resending_limit_rule.value, 5)

        retrieved = starkbank.transfer.get(transfer.id)
        self.assertEqual(retrieved.id, transfer.id)


if __name__ == '__main__':
    main()
