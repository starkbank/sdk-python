# coding: utf-8
from random import choice, random
from starkbank import PaymentRequest, Transaction
from .boletoPayment import generateExampleBoletoPaymentsJson
from .date import randomFutureDate
from .transaction import generateExampleTransactionsJson
from .transfer import generateExampleTransfersJson
from .utilityPayment import generateExampleUtilityPaymentsJson


center_id = "5634161670881280"


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
        payment.scheduled = None
        attachments = []
        if random() < 0.1:
            attachments.append(
                {"name": "droids.txt", "data": "VGhlc2UgYXJlbid0IHRoZSBkcm9pZHMgeW91J3JlIGxvb2tpbmcgZm9yLg=="}
            )
        requests.append(PaymentRequest(
            center_id=center_id,
            payment=payment,
            due=None if isinstance(payment, Transaction) else randomFutureDate(days=7).date(),
            attachments=attachments,
        ))

    return requests
