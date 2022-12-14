import starkbank
from unittest import TestCase, main
from starkbank.error import InputErrors
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestDictKeyInfoGet(TestCase):
    
    def test_success(self):
        dict_key = starkbank.dictkey.get("valid@sandbox.com")
        self.assertIsNotNone(dict_key.id)
        print(dict_key)

    def test_fail_invalid_dict_key(self):
        dict_key_id = "0"
        with self.assertRaises(InputErrors) as context:
            dict_key = starkbank.dictkey.get(dict_key_id)
        errors = context.exception.errors
        for error in errors:
            print(error)
            self.assertEqual('invalidPixKey', error.code)
        self.assertEqual(1, len(errors))


class TestDictKeyGet(TestCase):

    def test_success_after_before(self):
        keys = starkbank.dictkey.query(type="evp", status="registered")
        i = 0
        for i, key in enumerate(keys):
            self.assertIsNotNone(key.id)
            if i >= 200:
                break
        print("Number of deposits:", i)


if __name__ == '__main__':
    main()
