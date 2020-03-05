from unittest import TestCase, main

from starkbank.auth.project import postProject, getProject, getProjectInfo, deleteProject
from tests.utils.project import generateExampleProjectData
from tests.utils.user import exampleMember


class TestProjectPost(TestCase):
    # def testSuccess(self):
    #     publicKeyString, platform, name = generateExampleProjectData()
    #     content, status = postProject(
    #         user=exampleMember,
    #         publicKeyString=publicKeyString,
    #         platform=platform,
    #         name=name,
    #     )
    #     print(content)
    #     if status != 200:
    #         code = content["errors"][0]["code"]
    #         self.assertEqual('invalidBalance', code)
    #     else:
    #         self.assertEqual(200, status)
    pass


class TestProjectGet(TestCase):
    def testSuccess(self):
        content, status = getProject(exampleMember)
        print(content)
        self.assertEqual(200, status)
        projectId = content["projects"][0]["id"]
        content, status = getProjectInfo(exampleMember, projectId=projectId)
        print(content)
        self.assertEqual(200, status)


class TestProjectGetInfo(TestCase):
    def testSuccess(self):
        content, status = getProject(exampleMember)
        print(content)
        self.assertEqual(200, status)
        projectId = content["projects"][0]["id"]
        content, status = getProjectInfo(exampleMember, projectId=projectId)
        print(content)
        self.assertEqual(200, status)


class TestProjectPostAndDelete(TestCase):
    def testSuccess(self):
        publicKeyString, platform, name = generateExampleProjectData()
        content, status = postProject(
            user=exampleMember,
            publicKeyString=publicKeyString,
            platform=platform,
            name=name,
        )
        print(content)
        self.assertEqual(200, status)
        projectId = content["project"]["id"]
        content, status = deleteProject(exampleMember, projectId=projectId)
        print(content)
        self.assertEqual(200, status)


if __name__ == '__main__':
    main()
