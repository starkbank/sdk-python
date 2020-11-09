import starkbank
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestDictKeyInfoGet(TestCase):
    
    def test_success(self):
        dict_key = starkbank.dictkey.get("tony@starkbank.com")
        self.assertIsNotNone(dict_key.id)
        print(dict_key)

    def test_fail_invalid_dict_key(self):
        dict_key_id = "0"
        with self.assertRaises(InputErrors) as context:
            dict_key = starkbank.dictkey.get(dict_key_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidDictKey', error.code)
        self.assertEqual(1, len(errors))


if __name__ == '__main__':
    main()
