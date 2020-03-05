from hashlib import sha256
from ellipticcurve.privateKey import PrivateKey
from starkbank.user.base import User
from starkbank.user.credentials import Credentials


class Member(User):
    def __init__(self, private_key=None, passphrase=None, member_id=None, workspace_id=None, email=None):
        if member_id:
            assert not workspace_id, "if member_id is informed, workspace_id cannot be informed"
            assert not email, "if member_id is informed, email cannot be informed"
            assert private_key, "if email is not informed, private_key must be informed"
            assert not passphrase, "if private_key is informed, passphrase cannot be informed"
            access_id = "member/{member_id}".format(member_id=member_id)
        else:
            assert not member_id, "if workspace_id or email is informed, member_id cannot be informed"
            assert workspace_id, "if member_id is not informed, workspace_id must be informed"
            assert email, "if member_id is not informed, email must be informed"
            assert (private_key and not passphrase) or (not private_key and passphrase), "cannot inform both private_key and passphrase"
            access_id = "workspace/{workspace_id}/email/{email}".format(workspace_id=workspace_id, email=email)

        self.member_id = member_id
        self.workspace_id = workspace_id
        self.email = email

        if passphrase:
            secret = int(
                sha256(
                    "{email}:STARKBANK:{passphrase}".format(
                        email=email,
                        passphrase=passphrase,
                    )
                ).hexdigest(),
                16
            )

            private_key = PrivateKey(secret=secret, curve="secp256k1")

        User.__init__(
            self,
            Credentials(
                access_id=access_id.format(id=id),
                private_key_pem=private_key,
            )
        )

    def __str__(self):
        return "Member(member_id={member_id}, workspace_id={workspace_id}, email={email}, credentials={credentials})".format(
            member_id=self.member_id,
            workspace_id=self.workspace_id,
            email=self.email,
            credentials=self.credentials,
        )
