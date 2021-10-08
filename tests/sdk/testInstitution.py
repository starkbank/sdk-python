import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestInstitutionQuery(TestCase):

    def test_success(self):
        institutions = starkbank.institution.query()
        for institution in institutions[:5]:
            self.assertIsInstance(institution.display_name, str)
            self.assertIsInstance(institution.name, str)
            self.assertIsInstance(institution.str_code, str)
            self.assertIsInstance(institution.spi_code, str)
            print(institution)

        self.assertEqual(len(starkbank.institution.query(search="stark")), 2)
        self.assertEqual(len(starkbank.institution.query(spi_codes="20018183")), 1)
        self.assertEqual(len(starkbank.institution.query(str_codes="341")), 1)


if __name__ == '__main__':
    main()
