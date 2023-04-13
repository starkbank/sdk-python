import starkbank
from unittest import TestCase, main
from datetime import date, timedelta
from starkbank import CorporateWithdrawal
from tests.utils.user import exampleProject
from tests.utils.withdrawal import generateExampleWithdrawalJson

starkbank.user = exampleProject


class TestCorporateWithdrawalQuery(TestCase):

    def test_success(self):
        withdrawals = starkbank.corporatewithdrawal.query(
            limit=10,
            after=date.today() - timedelta(days=100),
            before=date.today(),
        )
        for withdrawal in withdrawals:
            self.assertEqual(withdrawal.id, str(withdrawal.id))


class TestCorporateWithdrawalPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            withdrawals, cursor = starkbank.corporatewithdrawal.page(limit=2, cursor=cursor)
            for withdrawal in withdrawals:
                print(withdrawal)
                self.assertFalse(withdrawal.id in ids)
                ids.append(withdrawal.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestCorporateWithdrawalGet(TestCase):

    def test_success(self):
        withdrawals = starkbank.corporatewithdrawal.query(limit=1)
        withdrawal = starkbank.corporatewithdrawal.get(id=next(withdrawals).id)
        self.assertEqual(withdrawal.id, str(withdrawal.id))


class TestCorporateWithdrawalPost(TestCase):

    def test_success(self):
        example_withdrawal = generateExampleWithdrawalJson()
        withdrawal = starkbank.corporatewithdrawal.create(
            withdrawal=CorporateWithdrawal(
                amount=example_withdrawal.amount,
                external_id=example_withdrawal.external_id
            )
        )
        self.assertEqual(withdrawal.id, str(withdrawal.id))


if __name__ == '__main__':
    main()
