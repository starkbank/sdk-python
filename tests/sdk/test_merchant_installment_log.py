import datetime
import starkbank
from unittest import TestCase, main
from tests.utils.pooling import wait_for_query
from tests.utils.merchantSession import generate_example_merchant_session
from tests.utils.merchantPurchase import generate_example_merchant_purchase


from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestMerchantInstallmentQueryLog(TestCase):

    def setUp(self):
        self.merchant_installment_ids = []
        self.before_date = datetime.date.today()
        self.after_date = self.before_date - datetime.timedelta(days=2)
        merchant_tags = ["test_merchat_installment_query_log"]

        merchant_session = generate_example_merchant_session(
            tags=merchant_tags, challenge_mode="disabled"
        )
        self.merchant_purchase = generate_example_merchant_purchase(
            merchant_session=merchant_session
        )
        merchant_installments = wait_for_query(
            starkbank.merchantinstallment.query,
            purchase_ids=[self.merchant_purchase.id],
        )
        for merchant_installment in merchant_installments:
            self.merchant_installment_ids.append(merchant_installment.id)

    def test_query_log(self):
        merchant_installment_logs = starkbank.merchantinstallment.log.query(
            installment_ids=self.merchant_installment_ids,
            limit=1,
            after=self.after_date,
            before=self.before_date,
        )
        for log in merchant_installment_logs:
            self.assertEqual(log.installment.purchase_id, self.merchant_purchase.id)

    def test_get_log_by_id(self):
        merchant_installment_logs = starkbank.merchantinstallment.log.query(limit=3)
        for log in merchant_installment_logs:
            merchant_installment_log = starkbank.merchantinstallment.log.get(log.id)
            self.assertEqual(log.id, merchant_installment_log.id)

    def test_page_with_filters(self):
        cursor = None
        limit = 2
        while True:
            ids = []
            page, cursor = starkbank.merchantinstallment.log.page(
                limit=limit,
                cursor=cursor,
                after=self.after_date,
                before=self.before_date,
                installment_ids=self.merchant_installment_ids,
            )
            for entity in page:
                self.assertNotIn(entity.id, ids)
                self.assertIn(entity.installment.purchase_id, self.merchant_purchase.id)
                ids.append(entity.id)

            self.assertEqual(len(ids), limit)

            if cursor is None:
                break

    def test_query_by_type(self):
        type = "created"
        merchant_installment_logs = starkbank.merchantinstallment.log.query(
            types=[type],
            limit=1,
            after=self.after_date,
            before=self.before_date,
        )
        for log in merchant_installment_logs:
            self.assertEqual(log.type, type)

    def test_page_filter_by_type(self):
        type = "created"
        page, _ = starkbank.merchantinstallment.log.page(types=[type])
        for entity in page:
            self.assertEqual(entity.type, type)


if __name__ == "__main__":
    main()
