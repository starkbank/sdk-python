import starkbank
from unittest import TestCase, main
from datetime import date, timedelta
from starkbank import CorporateInvoice
from tests.utils.user import exampleProject
from tests.utils.corporateInvoice import generateExampleInvoicesJson

starkbank.user = exampleProject


class TestCorporateInvoiceQuery(TestCase):

    def test_success(self):
        invoices = starkbank.corporateinvoice.query(
            limit=1,
            after=date.today() - timedelta(days=100),
            before=date.today(),
        )
        for invoice in invoices:
            self.assertEqual(invoice.id, str(invoice.id))


class TestCorporateInvoicePost(TestCase):

    def test_success(self):
        example_invoice = generateExampleInvoicesJson()
        invoice = starkbank.corporateinvoice.create(
            invoice=CorporateInvoice(
                amount=example_invoice.amount
            )
        )
        self.assertEqual(invoice.id, str(invoice.id))
        print(invoice)


if __name__ == '__main__':
    main()
