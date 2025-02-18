import starkbank
from datetime import datetime, timedelta
from unittest import TestCase, main
from tests.utils.date import randomPastDate
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestDepositQuery(TestCase):

    def test_success_after_before(self):
        after = randomPastDate(days=10)
        before = datetime.today()
        deposits = starkbank.deposit.query(after=after.date(), before=before.date())
        i = 0
        for i, deposit in enumerate(deposits):
            self.assertTrue(after.date() <= deposit.created.date() <= (before + timedelta(hours=3)).date())
            if i >= 200:
                break
        print("Number of deposits:", i)


class TestDepositPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            deposits, cursor = starkbank.deposit.page(limit=2, cursor=cursor)
            for deposit in deposits:
                print(deposit)
                self.assertFalse(deposit.id in ids)
                ids.append(deposit.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestDepositInfoGet(TestCase):

    def test_success(self):
        deposits = starkbank.deposit.query(limit=1)
        deposit_id = next(deposits).id
        deposit = starkbank.deposit.get(deposit_id)
        print(deposit)


class TestDepositInfoPatch(TestCase):

    def test_success_amount(self):
        deposits = starkbank.deposit.query(status="created", limit=20)
        deposit_amount = 0
        for deposit in deposits:
            if deposit.type != "ted":
                self.assertIsNotNone(deposit.id)
                updated_deposit = starkbank.deposit.update(
                    deposit.id,
                    amount=deposit_amount,
                )
                print(updated_deposit)
                self.assertEqual(updated_deposit.amount, deposit_amount)
                break


if __name__ == '__main__':
    main()

