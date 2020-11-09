import starkbank
from time import sleep
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.invoice import generateExampleInvoicesJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestInvoiceLogGet(TestCase):

    def test_success(self):
        logs = list(starkbank.invoice.log.query(limit=10))
        logs = list(starkbank.invoice.log.query(limit=10, invoice_ids={log.invoice.id for log in logs}, types={log.type for log in logs}))
        print("Number of logs:", len(logs))

    def test_success_invoice_ids(self):
        invoices = generateExampleInvoicesJson(n=5)
        invoices = starkbank.invoice.create(invoices)
        invoice_ids = {invoice.id for invoice in invoices}
        logs = starkbank.invoice.log.query(invoice_ids=invoice_ids)
        for log in logs:
            print(log)


class TestInvoiceLogInfoGet(TestCase):
    def test_success(self):
        logs = starkbank.invoice.log.query()
        log_id = next(logs).id
        logs = starkbank.invoice.log.get(id=log_id)

    def test_fail_invalid_log(self):
        log_id = "123"
        with self.assertRaises(InputErrors) as context:
            log = starkbank.invoice.log.get(id=log_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidInvoiceLog', error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
