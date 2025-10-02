# coding: utf-8
from datetime import timedelta, datetime


def generateExampleInvoicePullRequestJson(invoice_id=None, subscription_id=None):
    request = {
        "attemptType": "default",
        "due": datetime.today().date() + timedelta(days=5),
        "invoiceId": invoice_id,
        "subscriptionId": subscription_id,
        "tags": []
    }
    return request
