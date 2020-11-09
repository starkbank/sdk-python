import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject

starkbank.user = exampleProject


class TestDictKey(TestCase):
    
    def test_success(self):
        dict_key = starkbank.dictkey.get("tony@starkbank.com")
        self.assertIsNotNone(dict_key.id)
        print(dict_key)


if __name__ == '__main__':
    main()
