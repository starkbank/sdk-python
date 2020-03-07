import starkbank
from unittest import TestCase, main
from tests.utils.boleto import generateExampleBoletosJson
from tests.utils.user import exampleProject

starkbank.settings.logging = "debug"


class TestBoletoPost(TestCase):
    def testSuccess(self):
        boletos = generateExampleBoletosJson(n=5)
        boletos = starkbank.boleto.create(user=exampleProject, boletos=boletos)

    def testFailInvalidArraySize(self):
        boletos = generateExampleBoletosJson(n=105)
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            boletos = starkbank.boleto.create(user=exampleProject, boletos=boletos)
        errors = context.exception.elements
        for error in errors:
            self.assertTrue('invalidJson', error.code)

    def testFailInvalidJson(self):
        boletos = {}
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            boletos = starkbank.boleto.create(user=exampleProject, boletos=boletos)
        errors = context.exception.elements
        for error in errors:
            self.assertTrue('invalidJson', error.code)

    def testFailInvalidJsonBoleto(self):
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

        with self.assertRaises(starkbank.exceptions.InputError) as context:
            boletos = starkbank.boleto.create(user=exampleProject, boletos=boletos)
        errors = context.exception.elements
        for error in errors:
            self.assertTrue('invalidJson', error.code)

    def testFailInvalidDescription(self):
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
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            boletos = starkbank.boleto.create(user=exampleProject, boletos=boletos)
        for error in context.exception.elements:
            self.assertTrue('invalidDescription', error.code)

    def testFailInvalidTaxId(self):
        boletos = generateExampleBoletosJson(n=5)
        boletos[0].tax_id = "000.000.000-00"
        boletos[1].tax_id = "00.000.000/0000-00"
        boletos[2].tax_id = "abc"
        boletos[3].tax_id = 123
        boletos[4].tax_id = {}
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            boletos = starkbank.boleto.create(user=exampleProject, boletos=boletos)
        errors = context.exception.elements
        for error in errors:
            self.assertTrue('invalidTaxId', error.code)

    def testFailInvalidAmount(self):
        boletos = generateExampleBoletosJson(n=5)
        boletos[0].amount = "123"
        boletos[1].amount = -5
        boletos[2].amount = 0
        boletos[3].amount = 1000000000000000
        boletos[4].amount = {}
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            boletos = starkbank.boleto.create(user=exampleProject, boletos=boletos)
        errors = context.exception.elements
        for error in errors:
            self.assertTrue('invalidAmount', error.code)


class TestBoletoGet(TestCase):
    def testSuccess(self):
        boletos, cursor = starkbank.boleto.list(user=exampleProject)
        print("Number of boletos:", len(boletos))
        self.assertIsInstance(boletos, list)

    # def testFields(self):
    #     return NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     boletos, cursor, errors = starkbank.boleto.list(user=exampleMember, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     for boleto in content["boletos"]:
    #         self.assertTrue(set(boleto.keys()).issubset(fields))
    #     print(content)


class TestBoletoPostAndDelete(TestCase):
    def testSuccess(self):
        boletos = generateExampleBoletosJson(n=1)
        boletos = starkbank.boleto.create(user=exampleProject, boletos=boletos)
        boletoId = boletos[0].id
        boleto = starkbank.boleto.delete(user=exampleProject, ids=[boletoId])
        print(boleto.id)

    def testTwice(self):
        boletos = generateExampleBoletosJson(n=1)
        boletos = starkbank.boleto.create(user=exampleProject, boletos=boletos)
        boletoId = boletos[0].id
        boleto = starkbank.boleto.delete(user=exampleProject, ids=[boletoId])
        with self.assertRaises(starkbank.exceptions.InputError) as context:
            boleto = starkbank.boleto.delete(user=exampleProject, ids=[boletoId])
        errors = context.exception.elements
        for error in errors:
            self.assertTrue('invalidJson', error.code)


class TestBoletoInfoGet(TestCase):
    def testSuccess(self):
        boletos, cursor = starkbank.boleto.list(user=exampleProject)
        boletoId = boletos[0].id
        boleto = starkbank.boleto.retrieve(user=exampleProject, id=boletoId)

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     boletos, cursor, errors = starkbank.boleto.list(user=exampleMember)
    #     boletos = content["boletos"]
    #     boletoId = boletos[0]["id"]
    #     boletos, cursor, errors = starkbank.boleto.retrieve(user=exampleMember, id=boletoId, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     boleto = content["boleto"]
    #     print(content)
    #     self.assertTrue(set(boleto.keys()).issubset(fields))


class TestBoletoPdfGet(TestCase):
    def testSuccess(self):
        boletos, cursor = starkbank.boleto.list(user=exampleProject)
        boletoId = boletos[0].id
        pdf = starkbank.boleto.retrieve_pdf(user=exampleProject, id=boletoId)
        print(pdf)


if __name__ == '__main__':
    main()
