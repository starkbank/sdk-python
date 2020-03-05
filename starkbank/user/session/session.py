from ...utils.checks import check_id, check_datetime
from ..credentials import Credentials
from ..base import User


class Session(User):
    def __init__(self, private_key, session_id, expiration=None):
        self.session_id = check_id(session_id)
        if expiration:
            expiration = check_datetime(expiration)
        self.expiration = expiration

        User.__init__(
            self,
            Credentials(
                access_id="session/{session_id}".format(session_id=session_id),
                private_key_pem=private_key,
            )
        )

    def __str__(self):
        return "Session(session_id={session_id}, expiration={expiration}, credentials={credentials})".format(
            session_id=self.session_id,
            expiration=self.expiration,
            credentials=self.credentials,
        )
