import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBalanceGet(TestCase):

    def test_success(self):

        # debug
        print("--- project ---")
        print(exampleProject)
        print("--- end project ---")

        balance = starkbank.balance.get(user=exampleProject)
        print(balance)
        self.assertIsInstance(balance.amount, int)


if __name__ == '__main__':
    main()
