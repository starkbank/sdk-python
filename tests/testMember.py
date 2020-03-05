from unittest import TestCase, main
from starkbank.old_auth.session import getSessionInfo, getSession, postSession, deleteSession
from starkbank.old_auth.project import getProjectInfo, getProject, postProject, deleteProject
from tests.utils.project import generateExampleProjectData
from tests.utils.session import generateExampleSessionData
from tests.utils.user import exampleMemberOld


class TestMember(TestCase):
    pass


if __name__ == '__main__':
    main()
