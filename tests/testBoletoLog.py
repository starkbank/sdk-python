from unittest import TestCase, main

from starkbank.boleto.boletoLog import getBoletoLog, getBoletoLogInfo
from tests.utils.user import exampleMember


class TestBoletoLogGet(TestCase):

    def testSuccess(self):
        content, status = getBoletoLog(exampleMember)
        print(content)
        logs = content["logs"]
        print("Number of logs:", len(logs))
        self.assertEqual(200, status)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getBoletoLog(exampleMember, params=fieldsParams)
        self.assertEqual(200, status)
        for log in content["logs"]:
            self.assertTrue(set(log.keys()).issubset(fields))
        print(content)


class TestBoletoLogInfoGet(TestCase):
    def testSuccess(self):
        content, status = getBoletoLog(exampleMember)
        logs = content["logs"]
        logId = logs[0]["id"]
        content, status = getBoletoLogInfo(exampleMember, logId=logId)
        print(content)
        self.assertEqual(200, status)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getBoletoLog(exampleMember)
        logs = content["logs"]
        logId = logs[0]["id"]
        content, status = getBoletoLogInfo(exampleMember, logId=logId, params=fieldsParams)
        self.assertEqual(200, status)
        log = content["log"]
        print(content)
        self.assertTrue(set(log.keys()).issubset(fields))


if __name__ == '__main__':
    main()
