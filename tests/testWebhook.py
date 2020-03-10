import starkbank
from unittest import TestCase, main

from tests.utils.webhook import generateExampleWebhook
from tests.utils.user import exampleProject


class TestWebhookPost(TestCase):
    def test_success(self):
        webhook = generateExampleWebhook()
        webhook = starkbank.webhook.create(url=webhook.url, subscriptions=webhook.subscriptions)
        print(webhook.id)


class TestWebhookGet(TestCase):
    def test_success(self):
        webhooks = list(starkbank.webhook.query(limit=10))
        print("Number of webhooks:", len(webhooks))


class TestWebhookInfoGet(TestCase):
    def test_success(self):
        webhooks = starkbank.webhook.query(user=exampleProject)
        webhookId = next(webhooks).id
        webhook = starkbank.webhook.get(user=exampleProject, id=webhookId)


class TestWebhookPostAndDelete(TestCase):
    def test_success(self):
        webhook = generateExampleWebhook()
        webhook = starkbank.webhook.create(url=webhook.url, subscriptions=webhook.subscriptions)
        webhookId = webhook.id
        webhooks = starkbank.webhook.delete([webhookId])


if __name__ == '__main__':
    main()
