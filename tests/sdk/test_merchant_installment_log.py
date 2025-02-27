import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestMerchantInstallmentQueryLog(TestCase):

    def test_success(self):
        merchant_installment_logs = starkbank.merchantinstallment.log.query(limit=3)
        for log in merchant_installment_logs:
            print(log)
            self.assertIsInstance(log.id, str)


class TestMerchantInstallmentGetLog(TestCase):

    def test_success(self):
        merchant_installment_logs = starkbank.merchantinstallment.log.query(limit=3)
        for log in merchant_installment_logs:
            print(log.id)
            log = starkbank.merchantinstallment.log.get(log.id)
            self.assertIsInstance(log.id, str)


class TestMerchantInstallmentPageLog(TestCase):

    def test_success(self):
        ids = []
        cursor = None
        for _ in range(2):
            page, cursor = starkbank.merchantinstallment.log.page(limit=5, cursor=cursor)
            for entity in page:
                self.assertNotIn(entity.id, ids)
                ids.append(entity.id)
            if cursor is None:
                break
        self.assertEqual(len(ids), 10)


if __name__ == '__main__':
    main()

