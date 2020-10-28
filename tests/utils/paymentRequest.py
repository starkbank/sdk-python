# coding: utf-8
from random import choice, random
from starkbank import PaymentRequest, Transaction
from .boletoPayment import generateExampleBoletoPaymentsJson
from .transaction import generateExampleTransactionsJson
from .transfer import generateExampleTransfersJson
from .utilityPayment import generateExampleUtilityPaymentsJson
import os

center_id = os.environ["SANDBOX_CENTER_ID"]


def generateExamplePaymentRequestsJson(n=1):
    requests = []

    types = [
        choice([
            "transfer",
            "boleto-payment",
            "utility-payment",
            "transaction",
        ])
        for _ in range(n)
    ]

    payments = []
    for type in set(types):
        payments.extend({
            "transfer": generateExampleTransfersJson,
            "boleto-payment": generateExampleBoletoPaymentsJson,
            "utility-payment": generateExampleUtilityPaymentsJson,
            "transaction": generateExampleTransactionsJson,
        }[type](n=types.count(type)))

    for payment in payments:
        attachments = []
        if random() < 0.1:
            attachments.append(
                {"name": "droids.txt", "data": "VGhlc2UgYXJlbid0IHRoZSBkcm9pZHMgeW91J3JlIGxvb2tpbmcgZm9yLg=="}
            )
        requests.append(PaymentRequest(
            center_id=center_id,
            payment=payment,
            due=None if isinstance(payment, Transaction) else payment.scheduled,
            # attachments=attachments,
        ))
        payment.scheduled = None

    return requests
