from unittest import TestCase

from starkbank.utils.request import fetch
from tests.utils.user import exampleProject


class TestRequest(TestCase):

    def test_get(self):
        response = fetch(user=exampleProject, version="")
        self.assertEqual(response.status, 200)
