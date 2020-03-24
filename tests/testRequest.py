from unittest import TestCase

from starkbank.utils.request import fetch, GET
from tests.utils.user import exampleProject


class TestRequest(TestCase):

    def test_get(self):
        response = fetch(method=GET, path="/", user=exampleProject, version="")
        self.assertEqual(response.status, 200)
