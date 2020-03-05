from ..base import User
from ..credentials import Credentials


class Member(User):
    def __init__(self, private_key, member_id=None, workspace_id=None, email=None):
        if id:
            assert not workspace_id, "if member_id is informed, workspace_id cannot be informed"
            assert not email, "if member_id is informed, email cannot be informed"
            access_id = "member/{member_id}".format(member_id=member_id)
        else:
            assert not member_id, "if workspace_id or email is informed, member_id cannot be informed"
            assert workspace_id, "if member_id is not informed, workspace_id must be informed"
            assert email, "if member_id is not informed, email must be informed"
            access_id = "workspace/{workspace_id}/email/{email}".format(workspace_id=workspace_id, email=email)

        self.member_id = member_id
        self.workspace_id = workspace_id
        self.email = email

        super(User, self).__init__(
            Credentials(
                access_id=access_id.format(id=id),
                private_key=private_key,
            )
        )
