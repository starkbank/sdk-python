import starkbank
from unittest import TestCase, main

from tests.utils.user import exampleProject


class TestBalanceGet(TestCase):
    def testSuccess(self):
        balance = starkbank.balance.get(user=exampleProject)
        self.assertIsInstance(balance.amount, int)


if __name__ == '__main__':
    main()
