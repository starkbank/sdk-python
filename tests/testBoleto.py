import starkbank
from unittest import TestCase, main
from tests.utils.boleto import generateExampleBoletosJson
from tests.utils.user import exampleMember

starkbank.settings.logging = "debug"

class TestBoletoPost(TestCase):
    def testSuccess(self):
        boletos = generateExampleBoletosJson(n=5)
        boletos, errors = starkbank.boleto.create(user=exampleMember, boletos=boletos)
        for error in errors:
            print(error)
        print(boletos)
        self.assertEqual(0, len(errors))

    def testFailInvalidArraySize(self):
        boletos = generateExampleBoletosJson(n=105)
        boletos, errors = starkbank.boleto.create(user=exampleMember, boletos=boletos)
        for error in errors:
            print(error)
        self.assertEqual(1, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error.code)

    def testFailInvalidJson(self):
        boletos = {}
        boletos, errors = starkbank.boleto.create(user=exampleMember, boletos=boletos)
        for error in errors:
            print(error)
        self.assertEqual(1, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error.code)

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

        boletos, errors = starkbank.boleto.create(user=exampleMember, boletos=boletos)
        for error in errors:
            print(error)
        self.assertEqual(9, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error.code)

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
        boletos, errors = starkbank.boleto.create(user=exampleMember, boletos=boletos)
        for error in errors:
            print(error)
        self.assertEqual(12, len(errors))
        for error in errors:
            self.assertEqual('invalidDescription', error.code)

    def testFailInvalidTaxId(self):
        boletos = generateExampleBoletosJson(n=5)
        boletos[0].tax_id = "000.000.000-00"
        boletos[1].tax_id = "00.000.000/0000-00"
        boletos[2].tax_id = "abc"
        boletos[3].tax_id = 123
        boletos[4].tax_id = {}
        boletos, errors = starkbank.boleto.create(user=exampleMember, boletos=boletos)
        for error in errors:
            print(error)
        self.assertEqual(7, len(errors))
        for error in errors:
            self.assertEqual('invalidTaxId', error.code)

    def testFailInvalidAmount(self):
        boletos = generateExampleBoletosJson(n=5)
        boletos[0].amount = "123"
        boletos[1].amount = -5
        boletos[2].amount = 0
        boletos[3].amount = 1000000000000000
        boletos[4].amount = {}
        boletos, errors = starkbank.boleto.create(user=exampleMember, boletos=boletos)
        for error in errors:
            print(error)
        self.assertEqual(5, len(errors))
        for error in errors:
            self.assertEqual('invalidAmount', error.code)


class TestBoletoGet(TestCase):
    def testSuccess(self):
        boletos, errors = starkbank.boleto.list(user=exampleMember)
        for error in errors:
            print(error)
        self.assertEqual(0, len(errors))
        print("Number of boletos:", len(boletos))
        self.assertIsInstance(boletos, list)

    # def testFields(self):
    #     return NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     boletos, errors = starkbank.boleto.list(user=exampleMember, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     for boleto in content["boletos"]:
    #         self.assertTrue(set(boleto.keys()).issubset(fields))
    #     print(content)


class TestBoletoPostAndDelete(TestCase):
    def testSuccess(self):
        boletos = generateExampleBoletosJson(n=1)
        boletos, errors = starkbank.boleto.create(user=exampleMember, boletos=boletos)
        for error in errors:
            print(error)
        self.assertEqual(0, len(errors))
        boletoId = boletos[0].id
        boletos, errors = starkbank.boleto.delete(user=exampleMember, id=boletoId)
        for error in errors:
            print(error)
        self.assertEqual(0, len(errors))

    def testTwice(self):
        boletos = generateExampleBoletosJson(n=1)
        boletos, errors = starkbank.boleto.create(user=exampleMember, boletos=boletos)
        for error in errors:
            print(error)
        self.assertEqual(0, len(errors))
        boletoId = boletos[0].id
        boletos, errors = starkbank.boleto.delete(user=exampleMember, id=boletoId)
        for error in errors:
            print(error)
        self.assertEqual(0, len(errors))
        boletos, errors = starkbank.boleto.delete(user=exampleMember, id=boletoId)
        for error in errors:
            print(error)
        code = errors[0].code
        self.assertEqual('invalidBoleto', code)


class TestBoletoInfoGet(TestCase):
    def testSuccess(self):
        boletos, errors = starkbank.boleto.list(user=exampleMember)
        for error in errors:
            print(error)
        boletoId = boletos[0].id
        boletos, errors = starkbank.boleto.retrieve(user=exampleMember, id=boletoId)
        for error in errors:
            print(error)
        self.assertEqual(0, len(errors))

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     boletos, errors = starkbank.boleto.list(user=exampleMember)
    #     boletos = content["boletos"]
    #     boletoId = boletos[0]["id"]
    #     boletos, errors = starkbank.boleto.retrieve(user=exampleMember, id=boletoId, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     boleto = content["boleto"]
    #     print(content)
    #     self.assertTrue(set(boleto.keys()).issubset(fields))


class TestBoletoPdfGet(TestCase):
    def testSuccess(self):
        boletos, errors = starkbank.boleto.list(user=exampleMember)
        boletoId = boletos[0].id
        pdf, errors = starkbank.boleto.retrieve_pdf(user=exampleMember, id=boletoId)
        for error in errors:
            print(error)
        print(pdf)
        self.assertEqual(0, len(errors))


if __name__ == '__main__':
    main()
