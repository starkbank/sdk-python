import starkbank
from datetime import datetime, timedelta
from unittest import TestCase, main
from tests.utils.date import randomPastDate
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestDepositGet(TestCase):

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
        deposits = starkbank.deposit.query(limit=1)
        deposit_id = next(deposits).id
        deposit = starkbank.deposit.get(deposit_id)
        print(deposit)


if __name__ == '__main__':
    main()
