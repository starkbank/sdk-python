import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject

starkbank.debug = True


class TestBoletoLogGet(TestCase):

    def testSuccess(self):
        logs = list(starkbank.boleto.log.query(limit=10))
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
        logs = starkbank.boleto.log.query()
        logId = next(logs).id
        logs = starkbank.boleto.log.get(id=logId)

    def testFailInvalidLog(self):
        logId = "0"
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            log = starkbank.boleto.log.get(id=logId)
        errors = context.exception.elements
        for error in errors:
            print(error)
            self.assertEqual('invalidBoletoLog', error.code)
        self.assertEqual(1, len(errors))

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     content, status = starkbank.boleto.log.list(user=exampleMember)
    #     logs = content["logs"]
    #     logId = logs[0]["id"]
    #     content, status = starkbank.boleto.log.get(user=exampleMember, id=logId, params=fieldsParams)
    #     self.assertEqual(200, status)
    #     log = content["log"]
    #     print(content)
    #     self.assertTrue(set(log.keys()).issubset(fields))


if __name__ == '__main__':
    main()
