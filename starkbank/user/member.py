from starkbank.user.base import User
from starkbank.user.credentials import Credentials


class Member(User):
    def __init__(self, private_key, workspace_id, email):
        access_id = "workspace/{workspace_id}/email/{email}".format(workspace_id=workspace_id, email=email)
        self.workspace_id = workspace_id
        self.email = email

        User.__init__(
            self,
            id=None,
            credentials=Credentials(
                access_id=access_id,
                private_key_pem=private_key,
            )
        )
