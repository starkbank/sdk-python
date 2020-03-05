from hashlib import sha256
from ellipticcurve.curve import secp256k1
from ellipticcurve.privateKey import PrivateKey
from starkbank.user.base import User
from starkbank.user.credentials import Credentials


class Member(User):
    def __init__(self, private_key=None, passphrase=None, id=None, workspace_id=None, email=None):
        if id:
            assert not workspace_id, "if id is informed, workspace_id cannot be informed"
            assert not email, "if id is informed, email cannot be informed"
            assert private_key, "if email is not informed, private_key must be informed"
            assert not passphrase, "if private_key is informed, passphrase cannot be informed"
            access_id = "member/{id}".format(id=id)
        else:
            assert not id, "if workspace_id or email is informed, id cannot be informed"
            assert workspace_id, "if id is not informed, workspace_id must be informed"
            assert email, "if id is not informed, email must be informed"
            assert (private_key and not passphrase) or (not private_key and passphrase), "cannot inform both private_key and passphrase"
            access_id = "workspace/{workspace_id}/email/{email}".format(workspace_id=workspace_id, email=email)

        self.workspace_id = workspace_id
        self.email = email

        if passphrase:
            to_hash = "{email}:STARKBANK:{passphrase}".format(
                email=email,
                passphrase=passphrase,
            )

            try:
                to_hash = to_hash.encode()
            except:
                pass

            secret = int(sha256(to_hash).hexdigest(), 16)

            private_key = PrivateKey(secret=secret, curve=secp256k1).toPem()

        User.__init__(
            self,
            id=id,
            credentials=Credentials(
                access_id=access_id.format(id=id),
                private_key_pem=private_key,
            )
        )
