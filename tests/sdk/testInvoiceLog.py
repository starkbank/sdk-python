import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestInvoiceLogGet(TestCase):

    def test_success(self):
        logs = list(starkbank.invoice.log.query(limit=10))
        logs = list(starkbank.invoice.log.query(limit=10, invoice_ids={log.invoice.id for log in logs}, types={log.type for log in logs}))
        print("Number of logs:", len(logs))


class TestInvoiceLogInfoGet(TestCase):
    def test_success(self):
        logs = starkbank.invoice.log.query()
        log_id = next(logs).id
        logs = starkbank.invoice.log.get(id=log_id)


if __name__ == '__main__':
    main()
