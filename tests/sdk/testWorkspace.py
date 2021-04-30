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
            allowed_tax_ids=workspace.allowed_tax_ids,
            user=exampleOrganization,
        )
        print(workspace)


class TestWorkspaceQuery(TestCase):

    def test_success(self):
        workspaces = starkbank.workspace.query(limit=1, user=exampleOrganization)
        for workspace in workspaces:
            print(workspace)


class TestWorkspacePage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            workspaces, cursor = starkbank.workspace.page(limit=2, cursor=cursor, user=exampleOrganization)
            for workspace in workspaces:
                print(workspace)
                self.assertFalse(workspace.id in ids)
                ids.append(workspace.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestWebhookInfoGet(TestCase):

    def test_success(self):
        workspaces = starkbank.workspace.query(limit=1, user=exampleOrganization)
        workspace_id = next(workspaces).id
        workspace = starkbank.workspace.get(id=workspace_id, user=exampleOrganization.replace(workspace_id))
        print(workspace)


if __name__ == '__main__':
    main()
