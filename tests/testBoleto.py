from unittest import TestCase, main

from starkbank.old_boleto.boleto import postBoleto, deleteBoleto, getBoletoInfo, getBoleto, getBoletoPdf
from tests.utils.boleto import generateExampleBoletos
from tests.utils.user import exampleMember


class TestBoletoPost(TestCase):
    def testSuccess(self):
        boletosJson = generateExampleBoletos(n=5)
        content, status = postBoleto(exampleMember, boletosJson=boletosJson)
        print(content)
        self.assertEqual(200, status)

    def testFailInvalidArraySize(self):
        boletosJson = generateExampleBoletos(n=105)
        content, status = postBoleto(exampleMember, boletosJson=boletosJson)
        print(content)
        errors = content["errors"]
        self.assertEqual(1, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error["code"])

    def testFailInvalidJson(self):
        boletosJson = {}
        content, status = postBoleto(exampleMember, boletosJson=boletosJson)
        print(content)
        errors = content["errors"]
        self.assertEqual(1, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error["code"])

    def testFailInvalidJsonBoleto(self):
        boletosJson = generateExampleBoletos(n=16)
        boletosJson["boletos"][0].pop("amount")  # Required
        boletosJson["boletos"][1].pop("name")  # Required
        boletosJson["boletos"][2].pop("taxId")  # Required
        boletosJson["boletos"][3].pop("streetLine1")  # Required
        boletosJson["boletos"][4].pop("streetLine2")  # Required
        boletosJson["boletos"][5].pop("district")  # Required
        boletosJson["boletos"][6].pop("city")  # Required
        boletosJson["boletos"][7].pop("stateCode")  # Required
        boletosJson["boletos"][8].pop("zipCode")  # Required

        boletosJson["boletos"][9].pop("due")  # Optional
        boletosJson["boletos"][10].pop("fine")  # Optional
        boletosJson["boletos"][11].pop("interest")  # Optional
        boletosJson["boletos"][12].pop("overdueLimit")  # Optional
        boletosJson["boletos"][13].pop("tags")  # Optional
        boletosJson["boletos"][14].pop("descriptions")  # Optional

        boletosJson["boletos"][15]["invalidParameter"] = "invalidValue"

        content, status = postBoleto(exampleMember, boletosJson=boletosJson)
        print(content)
        errors = content["errors"]
        for error in errors:
            print(error)
        self.assertEqual(9, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error["code"])

    def testFailInvalidDescription(self):
        boletosJson = generateExampleBoletos(n=18)
        boletosJson["boletos"][0]["descriptions"] = [{"text": "abc"}]  # Valid (correct)
        boletosJson["boletos"][1]["descriptions"] = [{"text": "abc", "amount": 1}]  # Valid (correct)
        boletosJson["boletos"][2]["descriptions"] = None  # Valid (Null)
        boletosJson["boletos"][3]["descriptions"] = {}  # Valid (Null)
        boletosJson["boletos"][4]["descriptions"] = []  # Valid (Null)
        boletosJson["boletos"][5]["descriptions"] = ""  # Valid (Null)
        boletosJson["boletos"][6]["descriptions"] = 0  # Valid (Null)
        boletosJson["boletos"][7]["descriptions"] = [1]
        boletosJson["boletos"][8]["descriptions"] = [{}]
        boletosJson["boletos"][9]["descriptions"] = [["abc", 2]]
        boletosJson["boletos"][10]["descriptions"] = [{"a": "1"}]  # 2 errors
        boletosJson["boletos"][11]["descriptions"] = [{"amount": 1}]
        boletosJson["boletos"][12]["descriptions"] = [{"text": 1, "amount": 1}]
        boletosJson["boletos"][13]["descriptions"] = [{"text": [], "amount": 1}]
        boletosJson["boletos"][14]["descriptions"] = [{"text": "abc", "amount": []}]
        boletosJson["boletos"][15]["descriptions"] = [{"text": "abc", "amount": {}}]
        boletosJson["boletos"][16]["descriptions"] = [{"text": "abc", "amount": "abc"}]
        boletosJson["boletos"][17]["descriptions"] = [{"text": "abc", "amount": 1, "test": "abc"}]
        content, status = postBoleto(exampleMember, boletosJson=boletosJson)
        print(content)
        errors = content["errors"]
        for error in errors:
            print(error)
        self.assertEqual(12, len(errors))
        for error in errors:
            self.assertEqual('invalidDescription', error["code"])

    def testFailInvalidTaxId(self):
        boletosJson = generateExampleBoletos(n=5)
        boletosJson["boletos"][0]["taxId"] = "000.000.000-00"
        boletosJson["boletos"][1]["taxId"] = "00.000.000/0000-00"
        boletosJson["boletos"][2]["taxId"] = "abc"
        boletosJson["boletos"][3]["taxId"] = 123
        boletosJson["boletos"][4]["taxId"] = {}
        content, status = postBoleto(exampleMember, boletosJson=boletosJson)
        print(content)
        errors = content["errors"]
        for error in errors:
            print(error)
        self.assertEqual(7, len(errors))
        for error in errors:
            self.assertEqual('invalidTaxId', error["code"])

    def testFailInvalidAmount(self):
        boletosJson = generateExampleBoletos(n=5)
        boletosJson["boletos"][0]["amount"] = "123"
        boletosJson["boletos"][1]["amount"] = -5
        boletosJson["boletos"][2]["amount"] = 0
        boletosJson["boletos"][3]["amount"] = 1000000000000000
        boletosJson["boletos"][4]["amount"] = {}
        content, status = postBoleto(exampleMember, boletosJson=boletosJson)
        print(content)
        errors = content["errors"]
        for error in errors:
            print(error)
        self.assertEqual(5, len(errors))
        for error in errors:
            self.assertEqual('invalidAmount', error["code"])


class TestBoletoGet(TestCase):
    def testSuccess(self):
        content, status = getBoleto(exampleMember)
        self.assertEqual(200, status)
        boletos = content["boletos"]
        print("Number of boletos:", len(boletos))
        print(content)
        self.assertIsInstance(boletos, list)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getBoleto(exampleMember, params=fieldsParams)
        self.assertEqual(200, status)
        for boleto in content["boletos"]:
            self.assertTrue(set(boleto.keys()).issubset(fields))
        print(content)


class TestBoletoPostAndDelete(TestCase):
    def testSuccess(self):
        boletosJson = generateExampleBoletos(n=1)
        content, status = postBoleto(exampleMember, boletosJson=boletosJson)
        self.assertEqual(200, status)
        boletoId = content["boletos"][0]["id"]
        content, status = deleteBoleto(exampleMember, boletoId=boletoId)
        print(content)
        self.assertEqual(200, status)

    def testTwice(self):
        boletosJson = generateExampleBoletos(n=1)
        content, status = postBoleto(exampleMember, boletosJson=boletosJson)
        self.assertEqual(200, status)
        boletoId = content["boletos"][0]["id"]
        content, status = deleteBoleto(exampleMember, boletoId=boletoId)
        print(content)
        self.assertEqual(200, status)
        content, status = deleteBoleto(exampleMember, boletoId=boletoId)
        print(content)
        code = content["errors"][0]["code"]
        self.assertEqual('invalidBoleto', code)


class TestBoletoInfoGet(TestCase):
    def testSuccess(self):
        content, status = getBoleto(exampleMember)
        boletos = content["boletos"]
        boletoId = boletos[0]["id"]
        content, status = getBoletoInfo(exampleMember, boletoId=boletoId)
        print(content)
        self.assertEqual(200, status)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getBoleto(exampleMember)
        boletos = content["boletos"]
        boletoId = boletos[0]["id"]
        content, status = getBoletoInfo(exampleMember, boletoId=boletoId, params=fieldsParams)
        self.assertEqual(200, status)
        boleto = content["boleto"]
        print(content)
        self.assertTrue(set(boleto.keys()).issubset(fields))


class TestBoletoPdfGet(TestCase):
    def testSuccess(self):
        content, status = getBoleto(exampleMember)
        boletos = content["boletos"]
        boletoId = boletos[0]["id"]
        content, status = getBoletoPdf(exampleMember, boletoId=boletoId)
        print(content)
        self.assertEqual(200, status)


if __name__ == '__main__':
    main()
