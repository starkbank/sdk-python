import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestCorporateBalanceQuery(TestCase):

    def test_success(self):
        balance = starkbank.corporatebalance.get()
        self.assertIsInstance(balance.amount, int)


if __name__ == '__main__':
    main()
