import starkbank
from unittest import TestCase, main
from datetime import date, timedelta
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
        utilityPayment = generateExampleUtilityPaymentsJson(n=1)[0]
        taxPayment = generateExampleTaxPaymentsJson(n=1)[0]

        types = ["brcode-payment", "boleto-payment", "utility-payment", "tax-payment"]
        previews = [
            starkbank.PaymentPreview(id=brcodePayment.brcode),
            starkbank.PaymentPreview(id=boletoPayment.bar_code or boletoPayment.line),
            starkbank.PaymentPreview(id=utilityPayment.bar_code or utilityPayment.line),
            starkbank.PaymentPreview(id=taxPayment.bar_code or taxPayment.line),
        ]

        previewedTypes = []
        for preview in starkbank.paymentpreview.create(previews=previews):
            print(preview)
            previewedTypes.append(preview.type)
        self.assertEqual(types, previewedTypes)

        for preview in previews:
            preview.scheduled = date.today() + timedelta(days=100)

        previewedTypes = []
        for preview in starkbank.paymentpreview.create(previews=previews):
            print(preview)
            previewedTypes.append(preview.type)
        self.assertEqual(types, previewedTypes)


if __name__ == '__main__':
    main()
