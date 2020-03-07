import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject

starkbank.settings.logging = "debug"


class TestBoletoLogGet(TestCase):

    def testSuccess(self):
        logs, cursor = starkbank.boleto.log.list(user=exampleProject)
        print("Number of logs:", len(logs))

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     content, status = starkbank.boleto.log.list(user=exampleMember, params=fieldsParams)
    #     self.assertEqual(200, status)
    #     for log in content["logs"]:
    #         self.assertTrue(set(log.keys()).issubset(fields))
    #     print(content)


class TestBoletoLogInfoGet(TestCase):
    def testSuccess(self):
        logs, cursor = starkbank.boleto.log.list(user=exampleProject)
        logId = logs[0].id
        logs = starkbank.boleto.log.retrieve(user=exampleProject, id=logId)

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     content, status = starkbank.boleto.log.list(user=exampleMember)
    #     logs = content["logs"]
    #     logId = logs[0]["id"]
    #     content, status = starkbank.boleto.log.retrieve(user=exampleMember, id=logId, params=fieldsParams)
    #     self.assertEqual(200, status)
    #     log = content["log"]
    #     print(content)
    #     self.assertTrue(set(log.keys()).issubset(fields))


if __name__ == '__main__':
    main()
