import starkbank
from unittest import TestCase, main
from datetime import date, timedelta
from starkbank import CorporateWithdrawal
from tests.utils.user import exampleProject
from tests.utils.withdrawal import generateExampleWithdrawalJson, payment_script
import time

starkbank.user = exampleProject


class TestCorporateResourcesChecks(TestCase):

    def test_success_corporate_balance(self):
        balance = starkbank.corporatebalance.get()
        initial_balance = balance.amount

        if balance.amount < 0:
            request = payment_script(balance.amount)
            i = 0
            while i <= 5:
                br_code = starkbank.brcodepayment.get(request[0].id)
                if br_code.status == "success" or br_code.status == "failed":
                    time.sleep(5)
                    break
                time.sleep(10)
                i += 1
        balance = starkbank.corporatebalance.get()
        if balance.amount == initial_balance:
            time.sleep(5)
        balance = starkbank.corporatebalance.get()
        print("initial_balance:" + str(initial_balance))
        print("final_balance:" + str(balance.amount))
        print("diff:" + str(initial_balance - balance.amount))


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
                amount=100,
                external_id=example_withdrawal.external_id
            )
        )
        self.assertEqual(withdrawal.id, str(withdrawal.id))


if __name__ == '__main__':
    main()
