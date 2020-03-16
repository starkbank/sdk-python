from unittest import TestCase, main

import starkbank
from tests.utils.user import exampleProject

starkbank.user = exampleProject


class TestBalanceGet(TestCase):

    def test_success(self):
        balance = starkbank.balance.get(user=exampleProject)
        self.assertIsInstance(balance.amount, int)


if __name__ == '__main__':
    main()
