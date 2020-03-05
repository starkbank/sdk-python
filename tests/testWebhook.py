from unittest import TestCase, main

from starkbank.old_webhook.webhook import getWebhook, getWebhookInfo, postWebhook, deleteWebhook
from tests.utils.webhook import generateWebhookUrl
from tests.utils.user import exampleMemberOld


class TestWebhookPost(TestCase):
    # def testSuccess(self):
    #     webhookUrl = generateWebhookUrl()
    #     content, status = utils.postWebhook(webhookUrl=webhookUrl, subscriptions=["transfer", "boleto", "boletoPayment"])
    #     print(content)
    #     self.assertEqual(200, status)
    pass


class TestWebhookGet(TestCase):
    def testSuccess(self):
        content, status = getWebhook(exampleMemberOld)
        self.assertEqual(200, status)
        webhooks = content["webhooks"]
        print("Number of webhooks:", len(webhooks))
        print(content)
        self.assertIsInstance(webhooks, list)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getWebhook(exampleMemberOld, params=fieldsParams)
        self.assertEqual(200, status)
        for webhook in content["webhooks"]:
            self.assertTrue(set(webhook.keys()).issubset(fields))
        print(content)


class TestWebhookInfoGet(TestCase):
    def testSuccess(self):
        content, status = getWebhook(exampleMemberOld)
        webhooks = content["webhooks"]
        webhookId = webhooks[0]["id"]
        content, status = getWebhookInfo(exampleMemberOld, webhookId=webhookId)
        print(content)
        self.assertEqual(200, status)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getWebhook(exampleMemberOld)
        webhooks = content["webhooks"]
        webhookId = webhooks[0]["id"]
        content, status = getWebhookInfo(exampleMemberOld, webhookId=webhookId, params=fieldsParams)
        self.assertEqual(200, status)
        webhook = content["webhook"]
        print(content)
        self.assertTrue(set(webhook.keys()).issubset(fields))


class TestWebhookPostAndDelete(TestCase):
    def testSuccess(self):
        webhookUrl = generateWebhookUrl()
        content, status = postWebhook(exampleMemberOld, webhookUrl=webhookUrl,
                                      subscriptions=["transfer", "boleto", "boletoPayment"])
        self.assertEqual(200, status)
        webhookId = content["webhook"]["id"]
        content, status = deleteWebhook(exampleMemberOld, webhookId=webhookId)
        print(content)
        self.assertEqual(200, status)


if __name__ == '__main__':
    main()
