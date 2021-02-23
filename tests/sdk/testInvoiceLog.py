import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestInvoiceLogQuery(TestCase):

    def test_success(self):
        logs = list(starkbank.invoice.log.query(limit=10))
        logs = list(starkbank.invoice.log.query(limit=10, invoice_ids={log.invoice.id for log in logs}, types={log.type for log in logs}))
        print("Number of logs:", len(logs))


class TestInvoiceLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.invoice.log.page(limit=2, cursor=cursor)
            for log in logs:
                print(log)
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestInvoiceLogInfoGet(TestCase):
    def test_success(self):
        logs = starkbank.invoice.log.query()
        log_id = next(logs).id
        logs = starkbank.invoice.log.get(id=log_id)


class TestInvoiceLogPdfGet(TestCase):

    def test_success(self):
        logs = starkbank.invoice.log.query(types="reversed", limit=1)
        log_id = next(logs).id
        pdf = starkbank.invoice.log.pdf(log_id)
        self.assertGreater(len(pdf), 1000)


if __name__ == '__main__':
    main()
