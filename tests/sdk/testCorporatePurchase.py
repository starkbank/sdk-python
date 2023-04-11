import starkbank
from json import dumps, loads
from unittest import TestCase, main
from datetime import date, timedelta
from tests.utils.user import exampleProject
from starkcore.error import InvalidSignatureError

starkbank.user = exampleProject


class TestCorporatePurchaseQuery(TestCase):

    def test_success(self):
        purchases = starkbank.corporatepurchase.query(
            limit=10,
            after=date.today() - timedelta(days=100),
            before=date.today(),
        )
        for purchase in purchases:
            self.assertEqual(purchase.id, str(purchase.id))


class TestCorporatePurchaseGet(TestCase):

    def test_success(self):
        purchases = starkbank.corporatepurchase.query(limit=1)
        purchase = starkbank.corporatepurchase.get(id=next(purchases).id)
        self.assertEqual(purchase.id, str(purchase.id))


class TestCorporatePurchaseParseRight(TestCase):
    content = '{"acquirerId": "236090", "amount": 100, "cardId": "5671893688385536", "cardTags": [], "endToEndId": "2fa7ef9f-b889-4bae-ac02-16749c04a3b6", "holderId": "5917814565109760", "holderTags": [], "isPartialAllowed": false, "issuerAmount": 100, "issuerCurrencyCode": "BRL", "merchantAmount": 100, "merchantCategoryCode": "bookStores", "merchantCountryCode": "BRA", "merchantCurrencyCode": "BRL", "merchantFee": 0, "merchantId": "204933612653639", "merchantName": "COMPANY 123", "methodCode": "token", "purpose": "purchase", "score": null, "tax": 0, "walletId": ""}'
    valid_signature = "MEUCIBxymWEpit50lDqFKFHYOgyyqvE5kiHERi0ZM6cJpcvmAiEA2wwIkxcsuexh9BjcyAbZxprpRUyjcZJ2vBAjdd7o28Q="
    invalid_signature = "MEUCIQDOpo1j+V40DNZK2URL2786UQK/8mDXon9ayEd8U0/l7AIgYXtIZJBTs8zCRR3vmted6Ehz/qfw1GRut/eYyvf1yOk="

    def test_success(self):
        event = starkbank.corporatepurchase.parse(
            content=self.content,
            signature=self.valid_signature
        )
        print(event)

    def test_normalized_success(self):
        event = starkbank.corporatepurchase.parse(
            content=dumps(loads(self.content), sort_keys=False, indent=4),
            signature=self.valid_signature
        )
        print(event)

    def test_invalid_signature(self):
        with self.assertRaises(InvalidSignatureError):
            starkbank.corporatepurchase.parse(
                content=self.content,
                signature=self.invalid_signature,
            )


class TestCorporatePurchaseResponse(TestCase):

    def test_approved(self):
        response = starkbank.corporatepurchase.response(
            status="approved",
            amount=1000,
            tags=["tony", "stark"]
        )
        print(response)

    def test_denied(self):
        response = starkbank.corporatepurchase.response(
            status="denied",
            reason="other",
            tags=["tony", "stark"]
        )
        print(response)


if __name__ == '__main__':
    main()
