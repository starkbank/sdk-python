import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject

starkbank.user = exampleProject


class TestMerchantCategoryQuery(TestCase):

    def test_success(self):
        categories = starkbank.merchantcategory.query(
            search="food"
        )
        for category in categories:
            self.assertIsNotNone(category.type)


if __name__ == '__main__':
    main()
