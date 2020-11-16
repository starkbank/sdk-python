import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject

starkbank.user = exampleProject


class TestDictKeyInfoGet(TestCase):
    
    def test_success(self):
        dict_key = starkbank.dictkey.get("tony@starkbank.com")
        self.assertIsNotNone(dict_key.id)
        print(dict_key)


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
