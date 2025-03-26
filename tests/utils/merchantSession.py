# coding: utf-8
import starkbank
from copy import deepcopy
from starkbank import MerchantSession
from starkbank.merchantsession import AllowedInstallment


def generate_example_merchant_session(tags, challenge_mode):
    allowed_installments = [
        AllowedInstallment(total_amount=5000, count=1),
        AllowedInstallment(total_amount=5500, count=2),
    ]
    merchant_session = starkbank.merchantsession.create(
        MerchantSession(
            allowed_funding_types=["debit", "credit"],
            allowed_installments=allowed_installments,
            expiration=3600,
            challenge_mode=challenge_mode,
            tags=tags,
        )
    )

    return merchant_session


def json_to_merchant_session(json_data):
    return MerchantSession(
        allowed_funding_types=json_data.get("allowedFundingTypes"),
        allowed_installments=json_data.get("allowedInstallments"),
        challenge_mode=json_data.get("challengeMode"),
        expiration=json_data.get("expiration"),
        tags=json_data.get("tags"),
    )


def generate_example_merchant_session_json(challengeMode):
    merchant_session_json = {
        "allowedFundingTypes": ["debit", "credit"],
        "allowedInstallments": [
            {"totalAmount": 0, "count": 1},
            {"totalAmount": 120, "count": 2},
            {"totalAmount": 180, "count": 12},
        ],
        "expiration": 3600,
        "challengeMode": challengeMode,
        "tags": ["yourTags"],
    }
    return deepcopy(json_to_merchant_session(merchant_session_json))


def generate_example_merchant_session_purchase_challenge_mode_disabled_json():
    merchant_session_purchase_json = {
        "amount": 180,
        "installmentCount": 12,
        "cardExpiration": "2035-01",
        "cardNumber": "5277696455399733",
        "cardSecurityCode": "123",
        "holderName": "Holder Name",
        "fundingType": "credit",
    }
    return deepcopy(merchant_session_purchase_json)


def generate_example_merchant_session_purchase_challenge_mode_enabled_json():
    merchant_session_purchase_json = {
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
            "extraData": "extraData",
        },
    }
    return deepcopy(merchant_session_purchase_json)
