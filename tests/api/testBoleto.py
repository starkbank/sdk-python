import starkbank
from datetime import datetime, date, timedelta
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.boleto import generateExampleBoletosJson
from tests.utils.date import randomPastDate
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBoletoPost(TestCase):

    def test_success(self):
        boletos = generateExampleBoletosJson(n=100)
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
        boletos = generateExampleBoletosJson(n=17)
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
        boletos[15].discounts = None  # Optional

        boletos[16].invalid_parameter = "invalidValue"

        with self.assertRaises(InputErrors) as context:
            boletos = starkbank.boleto.create(boletos)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual("invalidJson", error.code)
        self.assertEqual(10, len(errors))

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

    def test_fail_invalid_discounts(self):
        boletos = generateExampleBoletosJson(n=19, useRandomFutureDueDate=False)
        boletos[0].discounts = None  # Valid (correct)
        boletos[1].discounts = []  # Valid (correct)
        boletos[2].discounts = [{"percentage": 3, "date": date.today() + timedelta(days=1)},
                                {"percentage": 5, "date": date.today()}]  # Valid (correct)
        boletos[3].discounts = [{"percentage": 5, "date": date.today()},
                                {"percentage": 2.5, "date": date.today() + timedelta(days=2)}]  # Valid (correct)
        boletos[4].discounts = [{"percentage": 5, "date": date.today()},
                                {"percentage": 4, "date": date.today() + timedelta(days=1)},
                                {"percentage": 3, "date": date.today() + timedelta(days=2)},
                                {"percentage": 2, "date": date.today() + timedelta(days=3)},
                                {"percentage": 1, "date": date.today() + timedelta(days=4)},
                                {"percentage": 0.5, "date": date.today() + timedelta(days=5)}]  # too many discounts
        boletos[5].discounts = [{"percentage": 1, "date": date.today()},
                                {"percentage": 3, "date": date.today() + timedelta(days=1)}]  # ascending discount
        boletos[6].discounts = [{"percentage": 3, "date": date.today()},
                                {"percentage": 3, "date": date.today() + timedelta(days=1)}]  # repeated percentage
        boletos[7].discounts = [{"percentage": -1, "date": date.today()}]  # invalid percentage
        boletos[8].discounts = [{"percentage": 0, "date": date.today()}]  # invalid percentage
        boletos[9].discounts = [{"percentage": 110, "date": date.today()}]  # invalid percentage
        boletos[10].discounts = [{"percentage": "wrong", "date": date.today()}]  # invalid percentage
        boletos[11].discounts = [{"percentages": 5, "date": date.today()}]  # invalid argument
        boletos[12].discounts = [{"percentage": 5, "date": date.today(), "wrong": 0}]  # invalid argument
        boletos[13].discounts = [{"date": date.today()}]  # missing percentage
        boletos[14].discounts = [{}]  # missing percentage and date
        boletos[14].discounts = [{"wrong": "wrong"}]  # missing percentage and date
        boletos[15].discounts = [{"percentages": 5}]  # missing date
        boletos[16].discounts = [{"percentage": 5, "date": date.today() - timedelta(days=1)}]  # invalid date
        boletos[17].discounts = [{"percentage": 5, "date": boletos[17].due + timedelta(days=1)}]  # invalid date
        boletos[18].discounts = [{"percentage": 5, "date": "wrong"}]  # invalid date

        with self.assertRaises(InputErrors) as context:
            starkbank.boleto.create(boletos)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertTrue(error.code in ['invalidBoleto', 'invalidDiscount', 'invalidDiscountDate'])
        self.assertEqual(20, len(errors))

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
        default_pdf = starkbank.boleto.pdf(boleto_id)
        self.assertGreater(len(default_pdf), 1000)
        force_default_pdf = starkbank.boleto.pdf(boleto_id, layout="default")
        self.assertGreater(len(force_default_pdf), 1000)
        booklet_pdf = starkbank.boleto.pdf(boleto_id, layout="booklet")
        self.assertGreater(len(booklet_pdf), 1000)
        default_pdf = starkbank.boleto.pdf(boleto_id, layout="default", hidden_fields=["customerAddress"])
        self.assertGreater(len(default_pdf), 1000)
        booklet_pdf = starkbank.boleto.pdf(boleto_id, layout="booklet", hidden_fields=["customerAddress"])
        self.assertGreater(len(booklet_pdf), 1000)

    def test_fail_invalid_boleto(self):
        with self.assertRaises(InputErrors) as context:
            pdf = starkbank.boleto.pdf("123")
    
    def test_fail_invalid_hidden_fields(self):
        boletos = starkbank.boleto.query()
        boleto_id = next(boletos).id

        with self.assertRaises(InputErrors) as context:
            default_pdf = starkbank.boleto.pdf(boleto_id, layout="default", hidden_fields=["unknown"])
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual("invalidFields", error.code)
        self.assertEqual(1, len(errors))

        with self.assertRaises(InputErrors) as context:
            booklet_pdf = starkbank.boleto.pdf(boleto_id, layout="booklet", hidden_fields=["unknown"])
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual("invalidFields", error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
