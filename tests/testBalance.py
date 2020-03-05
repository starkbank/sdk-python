from unittest import TestCase, main

from starkbank.old_ledger.balance import getBalance
from tests.utils.user import exampleMember


class TestBalanceGet(TestCase):
    def testSuccess(self):
        content, status = getBalance(exampleMember)
        print(content)
        self.assertEqual(200, status)
        self.assertIsInstance(content["balances"][0]["amount"], int)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getBalance(exampleMember, params=fieldsParams)
        self.assertEqual(200, status)
        self.assertIsInstance(content["balances"][0]["amount"], int)
        print(content)


if __name__ == '__main__':
    main()
