import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestInstitutionQuery(TestCase):

    def test_success(self):
        institutions = starkbank.institution.query()
        for institution in institutions[:5]:
            self.assertIsNotNone(institution.display_name)
            self.assertIsNotNone(institution.name)
            self.assertIsNotNone(institution.str_code)
            self.assertIsNotNone(institution.spi_code)
            print(institution)

        self.assertEqual(len(starkbank.institution.query(search="stark")), 2)
        self.assertEqual(len(starkbank.institution.query(spi_codes="20018183")), 1)
        self.assertEqual(len(starkbank.institution.query(str_codes="341")), 1)


if __name__ == '__main__':
    main()
