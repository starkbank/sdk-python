import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject

starkbank.debug = True


class TestBoletoLogGet(TestCase):

    def testSuccess(self):
        logs = list(starkbank.boleto.log.query(limit=10))
        print("Number of logs:", len(logs))


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


if __name__ == '__main__':
    main()
