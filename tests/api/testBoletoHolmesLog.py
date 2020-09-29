import starkbank
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBoletoHolmesLogGet(TestCase):

    def test_success(self):
        logs = list(starkbank.boletoholmes.log.query(
            limit=5,
        ))
        for log in logs:
            self.assertIsNotNone(log.id)
            print(log)

    def test_fail(self):
        with self.assertRaises(InputErrors) as context:
            list(starkbank.boletoholmes.log.query(limit=10, types=["random"]))
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidType', error.code)


class TestBoletoHolmesLogInfoGet(TestCase):

    def test_success(self):
        logs = starkbank.boletoholmes.log.query()
        log_id = next(logs).id
        log = starkbank.boletoholmes.log.get(log_id)
        print(log)

    def test_fail_invalid_log(self):
        log_id = "0"
        with self.assertRaises(InputErrors) as context:
            log = starkbank.boletoholmes.log.get(log_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidLog', error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
