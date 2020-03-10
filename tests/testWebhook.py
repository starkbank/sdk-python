import starkbank
from unittest import TestCase, main

from tests.utils.webhook import generateExampleWebhook
from tests.utils.user import exampleProject


class TestWebhookPost(TestCase):
    def testSuccess(self):
        webhook = generateExampleWebhook()
        webhook = starkbank.webhook.create(webhook)
        print(webhook.id)


class TestWebhookGet(TestCase):
    def testSuccess(self):
        webhooks = list(starkbank.webhook.query(limit=10))
        print("Number of webhooks:", len(webhooks))


class TestWebhookInfoGet(TestCase):
    def testSuccess(self):
        webhooks = starkbank.webhook.query(user=exampleProject)
        webhookId = next(webhooks).id
        webhook = starkbank.webhook.get(user=exampleProject, id=webhookId)


class TestWebhookPostAndDelete(TestCase):
    def testSuccess(self):
        webhook = generateExampleWebhook()
        webhook = starkbank.webhook.create(webhook)
        webhookId = webhook.id
        webhooks = starkbank.webhook.delete([webhookId])


if __name__ == '__main__':
    main()
