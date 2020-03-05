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

    def testFailInvalidJson(self):
        boletosJson = {}
        content, status = postBoleto(exampleMember, boletosJson=boletosJson)
        print(content)
        errors = content["errors"]
        self.assertEqual(1, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error["code"])

    def testFailInvalidJsonBoleto(self):
        boletosJson = generateExampleBoletos(n=11)
        boletosJson["boletos"][0].pop("amount")
        boletosJson["boletos"][1].pop("zipCode")
        boletosJson["boletos"][2].pop("city")
        boletosJson["boletos"][3].pop("district")
        boletosJson["boletos"][4].pop("email")
        boletosJson["boletos"][5].pop("name")
        boletosJson["boletos"][6].pop("phone")
        boletosJson["boletos"][7].pop("stateCode")
        boletosJson["boletos"][8].pop("streetLine1")
        boletosJson["boletos"][9].pop("streetLine2")
        boletosJson["boletos"][10].pop("taxId")
        content, status = postBoleto(exampleMember, boletosJson=boletosJson)
        print(content)
        errors = content["errors"]
        self.assertEqual(11, len(errors))
        for error in errors:
            self.assertEqual('invalidJson', error["code"])

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
