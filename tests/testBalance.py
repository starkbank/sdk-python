import starkbank
from unittest import TestCase, main

from tests.utils.user import exampleProject


class TestBalanceGet(TestCase):
    def testSuccess(self):
        balances, cursor = starkbank.balance.list(user=exampleProject)
        self.assertIsInstance(balances[0].amount, int)

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     balances, errors = starkbank.balance.get(user=exampleMember, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     self.assertIsInstance(balances[0].amount, int)
    #     print(content)


if __name__ == '__main__':
    main()
