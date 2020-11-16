import starkbank
from datetime import datetime, timedelta
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.date import randomPastDate
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestDepositGet(TestCase):

    def test_success(self):
        deposits = list(starkbank.deposit.query(limit=100))
        print("Number of deposits:", len(deposits))

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


class TestDepositInfoGet(TestCase):

    def test_success(self):
        deposits = starkbank.deposit.query()
        deposit_id = next(deposits).id
        deposit = starkbank.deposit.get(deposit_id)

    def test_fail_invalid_deposit(self):
        deposit_id = "0"
        with self.assertRaises(InputErrors) as context:
            deposit = starkbank.deposit.get(deposit_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidDeposit', error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
