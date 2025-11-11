# coding: utf-8
from datetime import timedelta, datetime
from starkbank import InvoicePullSubscription
from .names.names import get_full_name
import uuid


example_invoice_pull_subscription = InvoicePullSubscription(
    amount=0,
    amount_min_limit=5000,
    data=None,
    display_description="Dragon Travel Fare",
    external_id=str(uuid.uuid4()),
    interval="month",
    name="John Snow",
    pull_mode="manual",
    pull_retry_limit=3,
    start=datetime.today().date() + timedelta(days=5),
    end=datetime.today().date() + timedelta(days=35),
    reference_code="contract-12345",
    tags=[],
    tax_id="012.345.678-90",
    type=None
)


def generateExampleInvoicePullSubscriptionsJson(n=1, type=None):
    subscriptions = []
    for _ in range(n):
        example = example_invoice_pull_subscription
        example.name = get_full_name()
        example.external_id=str(uuid.uuid4())
        if type == "push":
            example.type = type
            example.data = {
                "accountNumber": "9123900000",
                "bankCode": "05097757",
                "branchCode": "1126",
                "taxId": "20.018.183/0001-80"
            }
        elif type == "qrcode":
            example.type = type
            example.data = None
        elif type == "qrcodeAndPayment":
            example.type = type
            example.data = {
                "amount": 400000
            }
        elif type == "paymentAndOrQrcode":
            example.type = type
            example.data = {
                "amount": 400000,
                "due": datetime.today().date() + timedelta(days=35),
                "fine": 2.5,
                "interest": 1.3
            }
        subscriptions.append(example)
    return subscriptions
