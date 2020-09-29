import starkbank
from random import choice
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBoletoHolmesPost(TestCase):

    def test_success(self):
        boleto = choice(list(starkbank.boleto.query(limit=100)))
        holmes = [starkbank.BoletoHolmes(boleto_id=boleto.id, tags=["elementary", "watson"])]
        try:
            holmes = starkbank.boletoholmes.create(holmes)
        except InputErrors as e:
            for error in e.errors:
                print(error)
                self.assertTrue(error.code in ["finalHolmesStatus", "repeatedHolmes"])
        for sherlock in holmes:
            print(sherlock)

    def test_fail_invalid_array_size(self):
        holmes = [starkbank.BoletoHolmes(boleto_id="123")] * 101
        with self.assertRaises(InputErrors) as context:
            holmes = starkbank.boletoholmes.create(holmes)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json(self):
        holmes = {}
        with self.assertRaises(InputErrors) as context:
            holmes = starkbank.boletoholmes.create(holmes)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidJson', error.code)
        self.assertEqual(1, len(errors))


class TestBoletoHolmesGet(TestCase):

    def test_success(self):
        holmes = list(starkbank.boletoholmes.query(
            limit=10,
        ))
        for sherlock in holmes:
            self.assertIsNotNone(sherlock.id)
            print(sherlock)


class TestBoletoHolmesInfoGet(TestCase):

    def test_success(self):
        holmes = starkbank.boletoholmes.query()
        holmes_id = next(holmes).id
        holmes = starkbank.boletoholmes.get(id=holmes_id)
        print(holmes)

    def test_fail_invalid_holmes(self):
        holmes_id = "0"
        with self.assertRaises(InputErrors) as context:
            holmes = starkbank.boletoholmes.get(holmes_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidHolmes', error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
