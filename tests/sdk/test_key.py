import starkbank
from unittest import TestCase, main


class TestKey(TestCase):

    def test_success(self):
        privateKey, publicKey = starkbank.key.create()
        print(privateKey)
        print(publicKey)

        self.assertTrue("PRIVATE KEY" in privateKey)
        self.assertTrue("PUBLIC KEY" in publicKey)

    def test_path_success(self):
        privateKey, publicKey = starkbank.key.create("temp/keys/")
        print(privateKey)
        print(publicKey)

        self.assertTrue("PRIVATE KEY" in privateKey)
        self.assertTrue("PUBLIC KEY" in publicKey)


if __name__ == '__main__':
    main()
