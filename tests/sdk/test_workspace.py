import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleOrganization
from tests.utils.workspace import generateExampleWorkspace


class TestWorkspaceCreate(TestCase):

    def test_create_and_patch(self):
        workspace = generateExampleWorkspace()

        workspace = starkbank.workspace.create(
            username=workspace.username,
            name=workspace.name,
            allowed_tax_ids=workspace.allowed_tax_ids,
            user=exampleOrganization,
        )
        print(workspace)

        update = generateExampleWorkspace()
        workspace = starkbank.workspace.update(
            id=workspace.id,
            username=update.username,
            name=update.name,
            allowed_tax_ids=update.allowed_tax_ids,
            user=exampleOrganization.replace(workspace.id),
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


class TestWorkspaceUpdatePicture(TestCase):

    def test_success(self):
        (workspaces, cursor) = starkbank.workspace.page(limit=1, user=exampleOrganization)
        file = open('tests/utils/logo.png', 'rb')
        picture = file.read()
        file.close()

        workspace = starkbank.workspace.update(
            id=workspaces[0].id,
            picture=picture,
            picture_type='image/png',
            user=starkbank.Organization.replace(exampleOrganization, workspaces[0].id)
        )

        self.assertEqual(workspace.id, workspaces[0].id)


class TestWorkspaceUpdateStatus(TestCase):

    def test_success(self):
        (workspaces, cursor) = starkbank.workspace.page(limit=1, user=exampleOrganization)

        workspace = starkbank.workspace.update(
            id=workspaces[0].id,
            status="blocked",
            user=starkbank.Organization.replace(exampleOrganization, workspaces[0].id)
        )

        self.assertEqual(workspace.id, workspaces[0].id)
        self.assertEqual(workspace.status, "blocked")

        print(workspace)

class TestWorkpsaceInfoGet(TestCase):

    def test_success(self):
        workspaces = starkbank.workspace.query(limit=1, user=exampleOrganization)
        workspace_id = next(workspaces).id
        workspace = starkbank.workspace.get(id=workspace_id, user=exampleOrganization.replace(workspace_id))
        print(workspace)


if __name__ == '__main__':
    main()
