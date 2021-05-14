import starkbank
from uuid import uuid4


def generateExampleWebhook():
    return starkbank.Webhook(
        url="https://webhook.site/{uuid}".format(uuid=str(uuid4())),
        subscriptions=[
            "transfer",
            "boleto",
            "deposit",
            "invoice",
            "boleto-payment",
            "boleto-holmes",
            "brcode-payment",
            "utility-payment",
            "tax-payment",
        ],
    )
