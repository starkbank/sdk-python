import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject
from tests.utils.webhook import generateExampleWebhook


starkbank.user = exampleProject


class TestWebhookGet(TestCase):

    def test_success(self):
        webhooks = list(starkbank.webhook.query(limit=10))
        print("Number of webhooks:", len(webhooks))


class TestWebhookInfoGet(TestCase):

    def test_success(self):
        webhooks = starkbank.webhook.query(user=exampleProject)
        webhook = starkbank.webhook.get(user=exampleProject, id=next(webhooks).id)


class TestWebhookPostAndDelete(TestCase):

    def test_success(self):
        webhook = generateExampleWebhook()
        webhook = starkbank.webhook.create(url=webhook.url, subscriptions=webhook.subscriptions)
        webhook = starkbank.webhook.delete(webhook.id)


if __name__ == '__main__':
    main()
