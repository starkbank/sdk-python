# coding: utf-8
import starkbank
from copy import deepcopy
from starkbank import MerchantPurchase


def json_to_merchant_purchase(json_data):
    return MerchantPurchase(
        amount=json_data.get("amount"),
        installment_count=json_data.get("installmentCount"),
        card_expiration=json_data.get("cardExpiration"),
        card_number=json_data.get("cardNumber"),
        card_security_code=json_data.get("cardSecurityCode"),
        holder_name=json_data.get("holderName"),
        holder_email=json_data.get("holderEmail"),
        holder_phone=json_data.get("holderPhone"),
        funding_type=json_data.get("fundingType"),
        billing_country_code=json_data.get("billingCountryCode"),
        billing_city=json_data.get("billingCity"),
        billing_state_code=json_data.get("billingStateCode"),
        billing_street_line_1=json_data.get("billingStreetLine1"),
        billing_street_line_2=json_data.get("billingStreetLine2"),
        billing_zip_code=json_data.get("billingZipCode"),
        metadata=json_data.get("metadata"),
        card_id=json_data.get("cardId")
    )


json_data = {
    "amount": 180,
    "installmentCount": 12,
    "cardExpiration": "2035-01",
    "cardNumber": "5277696455399733",
    "cardSecurityCode": "123",
    "holderName": "Holder Name",
    "holderEmail": "holdeName@email.com",
    "holderPhone": "11111111111",
    "fundingType": "credit",
    "billingCountryCode": "BRA",
    "billingCity": "São Paulo",
    "billingStateCode": "SP",
    "billingStreetLine1": "Rua do Holder Name, 123",
    "billingStreetLine2": "",
    "billingZipCode": "11111-111",
    "metadata": {
        "userAgent": "Postman",
        "userIp": "255.255.255.255",
        "language": "pt-BR",
        "timezoneOffset": 3,
        "extraData": "extraData"
    }
}

merchant_purchase = json_to_merchant_purchase(json_data)


def generate_example_merchant_purchase_json(card_id):
    merchant_purchase_json = {
            "amount": 10000,
            "installmentCount": 5,
            "cardId": card_id,
            "fundingType": "credit",
            "challengeMode": "disabled",
            "billingCity": "Sao Paulo",
            "billingCountryCode": "BRA",
            "billingStateCode": "SP",
            "billingStreetLine1": "Rua do Holder Name, 123",
            "billingStreetLine2": "1 andar",
            "billingZipCode": "11111-111",
            "holderEmail": "holdeName@email.com",
            "holderPhone": "11111111111",
            "metadata": {
                "userAgent": "userAgent",
                "userIp": "255.255.255.255",
                "language": "pt-BR",
                "timezoneOffset": 3,
                "extraData": "extraData"
            },
            "tags": [
                "teste"
            ]
        }

    return deepcopy(json_to_merchant_purchase(merchant_purchase_json))


def generate_example_merchant_purchase_patch():
    merchant_purchase_json = {
        "status": "reversed",
        "amount": 0
    }
    return deepcopy(merchant_purchase_json)

