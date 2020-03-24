from datetime import datetime, timedelta
from unittest import TestCase, main

import starkbank
from starkbank.exception import InputErrors
from tests.utils.boleto import generateExampleBoletosJson
from tests.utils.date import randomPastDate
from tests.utils.user import exampleProject

starkbank.user = exampleProject


class TestBoletoPost(TestCase):

    def test_success(self):
        boletos = generateExampleBoletosJson(n=5)
        boletos = starkbank.boleto.create(boletos)
        for boleto in boletos:
            print(boleto)

    def test_fail_invalid_array_size(self):
        boletos = generateExampleBoletosJson(n=105)
        with self.assertRaises(InputErrors) as context:
            boletos = starkbank.boleto.create(boletos)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual("invalidJson", error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json(self):
        boletos = {}
        with self.assertRaises(InputErrors) as context:
            boletos = starkbank.boleto.create(boletos)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual("invalidJson", error.code)
        self.assertEqual(1, len(errors))

    def test_fail_invalid_json_boleto(self):
        boletos = generateExampleBoletosJson(n=16)
        boletos[0].amount = None  # Required
        boletos[1].name = None  # Required
        boletos[2].tax_id = None  # Required
        boletos[3].street_line_1 = None  # Required
        boletos[4].street_line_2 = None  # Required
        boletos[5].district = None  # Required
        boletos[6].city = None  # Required
        boletos[7].state_code = None  # Required
        boletos[8].zip_code = None  # Required

        boletos[9].due = None  # Optional
        boletos[10].fine = None  # Optional
        boletos[11].interest = None  # Optional
        boletos[12].overdue_limit = None  # Optional
        boletos[13].tags = None  # Optional
        boletos[14].descriptions = None  # Optional

        boletos[15].invalid_parameter = "invalidValue"

        with self.assertRaises(InputErrors) as context:
            boletos = starkbank.boleto.create(boletos)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual("invalidJson", error.code)
        self.assertEqual(9, len(errors))

    def test_fail_invalid_description(self):
        boletos = generateExampleBoletosJson(n=18)
        boletos[0].descriptions = [{"text": "abc"}]  # Valid (correct)
        boletos[1].descriptions = [{"text": "abc", "amount": 1}]  # Valid (correct)
        boletos[2].descriptions = None  # Valid (Null)
        boletos[3].descriptions = {}  # Valid (Null)
        boletos[4].descriptions = []  # Valid (Null)
        boletos[5].descriptions = ""  # Valid (Null)
        boletos[6].descriptions = 0  # Valid (Null)
        boletos[7].descriptions = [1]
        boletos[8].descriptions = [{}]
        boletos[9].descriptions = [["abc", 2]]
        boletos[10].descriptions = [{"a": "1"}]  # 2 errors
        boletos[11].descriptions = [{"amount": 1}]
        boletos[12].descriptions = [{"text": 1, "amount": 1}]
        boletos[13].descriptions = [{"text": [], "amount": 1}]
        boletos[14].descriptions = [{"text": "abc", "amount": []}]
        boletos[15].descriptions = [{"text": "abc", "amount": {}}]
        boletos[16].descriptions = [{"text": "abc", "amount": "abc"}]
        boletos[17].descriptions = [{"text": "abc", "amount": 1, "test": "abc"}]
        with self.assertRaises(InputErrors) as context:
            boletos = starkbank.boleto.create(boletos)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidDescription', error.code)
        self.assertEqual(12, len(errors))

    def test_fail_invalid_tax_id(self):
        boletos = generateExampleBoletosJson(n=5)
        boletos[0].tax_id = "000.000.000-00"
        boletos[1].tax_id = "00.000.000/0000-00"
        boletos[2].tax_id = "abc"
        boletos[3].tax_id = 123  # 2 errors
        boletos[4].tax_id = {}  # 2 errors
        with self.assertRaises(InputErrors) as context:
            boletos = starkbank.boleto.create(boletos)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidTaxId', error.code)
        self.assertEqual(7, len(errors))

    def test_fail_invalid_amount(self):
        boletos = generateExampleBoletosJson(n=5)
        boletos[0].amount = "123"
        boletos[1].amount = -5
        boletos[2].amount = 0
        boletos[3].amount = 1000000000000000
        boletos[4].amount = {}
        with self.assertRaises(InputErrors) as context:
            boletos = starkbank.boleto.create(boletos)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidAmount', error.code)
        self.assertEqual(5, len(errors))


class TestBoletoGet(TestCase):

    def test_success(self):
        boletos = list(starkbank.boleto.query(limit=100))
        print("Number of boletos:", len(boletos))

    def test_success_after_before(self):
        after = randomPastDate(days=10)
        before = datetime.today()
        boletos = starkbank.boleto.query(after=after.date(), before=before.date())
        i = 0
        for i, boleto in enumerate(boletos):
            self.assertTrue(after.date() <= boleto.created.date() <= (before + timedelta(hours=3)).date())
            if i >= 200:
                break
        print("Number of boletos:", i)


class TestBoletoPostAndDelete(TestCase):

    def test_success(self):
        boletos = generateExampleBoletosJson(n=1)
        boletos = starkbank.boleto.create(boletos)
        boleto_id = boletos[0].id
        boleto = starkbank.boleto.delete(id=boleto_id)
        print(boleto.id)

    def test_fail_delete_twice(self):
        boletos = generateExampleBoletosJson(n=1)
        boletos = starkbank.boleto.create(boletos)
        boleto_id = boletos[0].id
        boletos = starkbank.boleto.delete(id=boleto_id)
        with self.assertRaises(InputErrors) as context:
            boletos = starkbank.boleto.delete(id=boleto_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual("invalidBoleto", error.code)
        self.assertEqual(1, len(errors))


class TestBoletoInfoGet(TestCase):

    def test_success(self):
        boletos = starkbank.boleto.query()
        boleto_id = next(boletos).id
        boleto = starkbank.boleto.get(boleto_id)

    def test_fail_invalid_boleto(self):
        boleto_id = "0"
        with self.assertRaises(InputErrors) as context:
            boleto = starkbank.boleto.get(boleto_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidBoleto', error.code)
        self.assertEqual(1, len(errors))


class TestBoletoPdfGet(TestCase):

    def test_success(self):
        boletos = starkbank.boleto.query()
        boleto_id = next(boletos).id
        pdf = starkbank.boleto.pdf(boleto_id)
        print(pdf)

    def test_fail_invalid_boleto(self):
        with self.assertRaises(InputErrors) as context:
            pdf = starkbank.boleto.pdf("123")


if __name__ == '__main__':
    main()
