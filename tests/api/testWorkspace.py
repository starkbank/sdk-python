import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleOrganization
from tests.utils.workspace import generateExampleWorkspace


class TestWorkspaceCreate(TestCase):

    def test_success(self):
        workspace = generateExampleWorkspace()
        workspace = starkbank.workspace.create(
            username=workspace.username,
            name=workspace.name,
            user=exampleOrganization,
        )
        print(workspace)


class TestWorkspaceQuery(TestCase):

    def test_success(self):
        workspaces = starkbank.workspace.query(limit=1, user=exampleOrganization)
        for workspace in workspaces:
            print(workspace)


class TestWebhookInfoGet(TestCase):

    def test_success(self):
        workspaces = starkbank.workspace.query(limit=1, user=exampleOrganization)
        workspace_id = next(workspaces).id
        workspace = starkbank.workspace.get(id=workspace_id, user=exampleOrganization.replace(workspace_id))
        print(workspace)


if __name__ == '__main__':
    main()
