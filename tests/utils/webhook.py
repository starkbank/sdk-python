import starkbank
from uuid import uuid4


def generateExampleWebhook():
    return starkbank.Webhook(
        url=r"https://webhook.site/{uuid}".format(uuid=str(uuid4())),
        subscriptions=["transfer", "boleto", "boleto-payment", "boleto-holmes"],
    )
