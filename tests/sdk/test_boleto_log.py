import starkbank
from unittest import TestCase, main
from starkcore.error import InputErrors
from tests.utils.boleto import generateExampleBoletosJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBoletoLogQuery(TestCase):

    def test_success(self):
        logs = list(starkbank.boleto.log.query(limit=10))
        logs = list(starkbank.boleto.log.query(limit=10, boleto_ids={log.boleto.id for log in logs}, types={log.type for log in logs}))
        print("Number of logs:", len(logs))

    def test_success_boleto_ids(self):
        boletos = generateExampleBoletosJson(n=5)
        boletos = starkbank.boleto.create(boletos)
        boleto_ids = {boleto.id for boleto in boletos}
        logs = starkbank.boleto.log.query(boleto_ids=boleto_ids)
        for log in logs:
            print(log)


class TestBoletoLogPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.boleto.log.page(limit=2, cursor=cursor)
            for log in logs:
                print(log)
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestBoletoLogInfoGet(TestCase):
    def test_success(self):
        logs = starkbank.boleto.log.query()
        log_id = next(logs).id
        logs = starkbank.boleto.log.get(id=log_id)

    def test_fail_invalid_log(self):
        log_id = "123"
        with self.assertRaises(InputErrors) as context:
            log = starkbank.boleto.log.get(id=log_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidBoletoLog', error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
