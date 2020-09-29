import starkbank
from unittest import TestCase, main
from tests.utils.boleto import generateExampleBoletosJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBoletoHolmesPost(TestCase):

    def test_success(self):
        boleto_samples = starkbank.boleto.create(generateExampleBoletosJson(n=5))

        holmes = starkbank.boletoholmes.create([
            starkbank.BoletoHolmes(boleto_id=boleto.id, tags=["elementary", "watson"])
            for boleto in boleto_samples
        ])
        for holmes in holmes:
            print(holmes)


class TestBoletoHolmesGet(TestCase):

    def test_success(self):
        holmes = list(starkbank.boletoholmes.query(limit=5))
        for sherlock in holmes:
            print(sherlock)
        self.assertEqual(5, len(holmes))


class TestBoletoHolmesInfoGet(TestCase):

    def test_success(self):
        holmes = starkbank.boletoholmes.query()
        sherlock_id = next(holmes).id
        sherlock = starkbank.boletoholmes.get(id=sherlock_id)
        print(sherlock)


if __name__ == '__main__':
    main()
