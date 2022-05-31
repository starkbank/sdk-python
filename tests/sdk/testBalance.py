import starkbank
from datetime import datetime
from unittest import TestCase, main
from tests.utils.core import generateTestConfig, TestCore


config = generateTestConfig(
    resource=starkbank.balance,
    schema={
        "amount": int,
        "updated": datetime,
        "currency": str,
        "id": str,
    },
)


class TestBalanceGet(TestCase):

    def test_get(self):
        TestCore.get(config)


if __name__ == '__main__':
    main()
