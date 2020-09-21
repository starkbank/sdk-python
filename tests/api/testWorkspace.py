import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestWorkspace(TestCase):

    def test_success(self):
        workspaces = starkbank.workspace.query(limit=1)
        for workspace in workspaces:
            print(workspace)


class TestWebhookInfoGet(TestCase):

    def test_success(self):
        workspaces = starkbank.workspace.query(limit=1)
        workspace = starkbank.workspace.get(id=next(workspaces).id)
        print(workspace)


if __name__ == '__main__':
    main()
