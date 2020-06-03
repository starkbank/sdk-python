import starkbank
from datetime import datetime, timedelta
from unittest import TestCase, main
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


class TestBoletoGet(TestCase):

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


class TestBoletoInfoGet(TestCase):

    def test_success(self):
        boletos = starkbank.boleto.query(limit=1)
        boleto_id = next(boletos).id
        boleto = starkbank.boleto.get(boleto_id)


class TestBoletoPdfGet(TestCase):

    def test_success(self):
        boletos = starkbank.boleto.query()
        boleto_id = next(boletos).id
        pdf = starkbank.boleto.pdf(boleto_id)
        self.assertGreater(len(pdf), 1000)
        default_pdf = starkbank.boleto.pdf(boleto_id, layout="default")
        self.assertGreater(len(default_pdf), 1000)
        booklet_pdf = starkbank.boleto.pdf(boleto_id, layout="booklet")
        self.assertGreater(len(booklet_pdf), 1000)


if __name__ == '__main__':
    main()
