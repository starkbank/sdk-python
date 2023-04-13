import starkbank
from unittest import TestCase, main
from datetime import date, timedelta
from starkbank.paymentpreview import BrcodePreview, BoletoPreview, UtilityPreview, TaxPreview
from tests.utils.user import exampleProject
from tests.utils.taxPayment import generateExampleTaxPaymentsJson
from tests.utils.boletoPayment import generateExampleBoletoPaymentsJson
from tests.utils.brcodePayment import generateExampleBrcodePaymentsJson
from tests.utils.utilityPayment import generateExampleUtilityPaymentsJson


starkbank.user = exampleProject


class TestPaymentPreviewCreate(TestCase):

    def test_success(self):
        brcodePayment = generateExampleBrcodePaymentsJson(n=1)[0]
        boletoPayment = generateExampleBoletoPaymentsJson(n=1)[0]
        taxPayment = generateExampleTaxPaymentsJson(n=1)[0]
        utilityPayment = generateExampleUtilityPaymentsJson(n=1)[0]

        previews = [
            starkbank.PaymentPreview(id=brcodePayment.brcode, scheduled=date.today() + timedelta(days=2)),
            starkbank.PaymentPreview(id=boletoPayment.bar_code or boletoPayment.line, scheduled=date.today() + timedelta(days=2)),
            starkbank.PaymentPreview(id=taxPayment.bar_code or taxPayment.line, scheduled=date.today() + timedelta(days=2)),
            starkbank.PaymentPreview(id=utilityPayment.bar_code or utilityPayment.line, scheduled=date.today() + timedelta(days=2)),
        ]

        for preview in starkbank.paymentpreview.create(previews=previews):
            print(preview)
            paymentClass = {
                "brcode-payment": BrcodePreview,
                "boleto-payment": BoletoPreview,
                "utility-payment": UtilityPreview,
                "tax-payment": TaxPreview,
            }[preview.type]
            self.assertIsInstance(preview.payment, paymentClass)


if __name__ == '__main__':
    main()
