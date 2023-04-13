import starkbank
from unittest import TestCase, main
from tests.utils.dynamicBrcode import generateExampleDynamicBrcodesJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestDynamicBrcodePost(TestCase):

    def test_success(self):
        brcodes = generateExampleDynamicBrcodesJson(n=5)
        brcodes = starkbank.dynamicbrcode.create(brcodes)
        for brcode in brcodes:
            print(brcode)


class TestDynamicBrcodeQuery(TestCase):

    def test_success(self):
        brcodes = list(starkbank.dynamicbrcode.query(limit=10))
        print(brcodes)
        self.assertEqual(10, len(brcodes))


class TestDynamicBrcodePage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            brcodes, cursor = starkbank.dynamicbrcode.page(limit=2, cursor=cursor)
            for brcode in brcodes:
                print(brcode)
                self.assertFalse(brcode.id in ids)
                ids.append(brcode.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestDynamicBrcodeInfoGet(TestCase):

    def test_success(self):
        brcodes = starkbank.dynamicbrcode.query()
        brcode_id = next(brcodes).uuid
        brcode = starkbank.dynamicbrcode.get(uuid=brcode_id)


if __name__ == '__main__':
    main()
