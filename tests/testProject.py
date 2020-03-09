import starkbank
from unittest import TestCase, main

from tests.utils.user import exampleProject


# class TestProjectPost(TestCase):
#     def testSuccess(self):
#         raise NotImplementedError


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


# class TestProjectPostAndDelete(TestCase):
#     def testSuccess(self):
#         raise NotImplementedError


if __name__ == '__main__':
    main()
