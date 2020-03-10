import starkbank
from unittest import TestCase, main

from tests.utils.user import exampleProject


class TestProjectGet(TestCase):
    def testSuccess(self):
        projects = starkbank.project.query()
        for project in projects:
            print(project.id)


class TestProjectGetInfo(TestCase):
    def testSuccess(self):
        projects = starkbank.project.query()
        project1 = next(projects)
        project2 = starkbank.project.get(project1.id)
        self.assertEqual(project1.id, project2.id)


if __name__ == '__main__':
    main()
