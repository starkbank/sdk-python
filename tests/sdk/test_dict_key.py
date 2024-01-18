import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject

starkbank.user = exampleProject


class TestDictKeyInfoGet(TestCase):
    
    def test_success(self):
        dict_key = starkbank.dictkey.get("valid@sandbox.com")
        self.assertIsNotNone(dict_key.id)
        print(dict_key)


class TestDictKeyQuery(TestCase):

    def test_success_after_before(self):
        keys = starkbank.dictkey.query(type="evp", status="registered")
        i = 0
        for i, key in enumerate(keys):
            self.assertIsNotNone(key.id)
            if i >= 200:
                break
        print("Number of deposits:", i)


class TestDictKeyPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            dictKeys, cursor = starkbank.dictkey.page(limit=2, cursor=cursor)
            for dictKey in dictKeys:
                print(dictKey)
                self.assertFalse(dictKey.id in ids)
                ids.append(dictKey.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) <= 4)


if __name__ == '__main__':
    main()
