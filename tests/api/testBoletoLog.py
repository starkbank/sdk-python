import starkbank
from time import sleep
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.boleto import generateExampleBoletosJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBoletoLogGet(TestCase):

    def test_success(self):
        logs = list(starkbank.boleto.log.query(limit=10))
        logs = list(starkbank.boleto.log.query(limit=10, boleto_ids={log.boleto.id for log in logs}, types={log.type for log in logs}))
        print("Number of logs:", len(logs))

    def test_fail(self):
        with self.assertRaises(InputErrors) as context:
            list(starkbank.boleto.log.query(limit=10, types=["random"]))
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidBoletoLog', error.code)

    def test_success_boleto_ids(self):
        boletos = generateExampleBoletosJson(n=5)
        boletos = starkbank.boleto.create(boletos)
        boleto_ids = {boleto.id for boleto in boletos}
        logs = starkbank.boleto.log.query(boleto_ids=boleto_ids)
        log_result = {
            "created": set(),
            "registered": set(),
        }
        sleep(10)
        for log in logs:
            log_result[log.type].add(log.boleto.id)
        print(log_result)
        self.assertEqual(boleto_ids, log_result["created"])
        self.assertEqual(boleto_ids, log_result["registered"])


class TestBoletoLogInfoGet(TestCase):
    def test_success(self):
        logs = starkbank.boleto.log.query()
        log_id = next(logs).id
        logs = starkbank.boleto.log.get(id=log_id)

    def test_fail_invalid_log(self):
        log_id = "0"
        with self.assertRaises(InputErrors) as context:
            log = starkbank.boleto.log.get(id=log_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidBoletoLog', error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
