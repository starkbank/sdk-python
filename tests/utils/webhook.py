import starkbank


def generateExampleWebhook():
    return starkbank.Webhook(
        url=r"https://webhook.site/60e9c18e-4b5c-4369-bda1-ab5fcd8e1b29",
        subscriptions=["transfer", "boleto", "boleto-payment"],
    )
