import starkbank
from unittest import TestCase, main

from tests.utils.webhook import generateExampleWebhook
from tests.utils.user import exampleMember


class TestWebhookPost(TestCase):
    def testSuccess(self):
        webhook = generateExampleWebhook()
        webhooks, errors = starkbank.webhook.create(user=exampleMember, webhook=webhook)
        self.assertEqual(0, len(errors))
    pass


class TestWebhookGet(TestCase):
    def testSuccess(self):
        webhooks, cursor, errors = starkbank.webhook.list(user=exampleMember)
        self.assertEqual(0, len(errors))
        print("Number of webhooks:", len(webhooks))
        self.assertIsInstance(webhooks, list)

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     webhooks, cursor, errors = starkbank.webhook.list(user=exampleMember, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     for webhook in webhooks:
    #         self.assertTrue(set(webhook.keys()).issubset(fields))


class TestWebhookInfoGet(TestCase):
    def testSuccess(self):
        webhooks, cursor, errors = starkbank.webhook.list(user=exampleMember)
        webhookId = webhooks[0].id
        webhook, errors = starkbank.webhook.retrieve(user=exampleMember, id=webhookId)
        self.assertEqual(0, len(errors))

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     webhooks, cursor, errors = starkbank.webhook.list(user=exampleMember)
    #     webhookId = webhooks[0].id
    #     webhooks, errors = starkbank.webhook.retrieve(user=exampleMember, webhookId=webhookId, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     self.assertTrue(set(webhook.keys()).issubset(fields))


class TestWebhookPostAndDelete(TestCase):
    def testSuccess(self):
        webhook = generateExampleWebhook()
        webhook, errors = starkbank.webhook.create(user=exampleMember, webhook=webhook)
        self.assertEqual(0, len(errors))
        webhookId = webhook.id
        webhooks, errors = starkbank.webhook.delete(user=exampleMember, id=webhookId)
        self.assertEqual(0, len(errors))


if __name__ == '__main__':
    main()
