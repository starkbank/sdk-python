from starkbank import request
from starkbank.utils.checks import check_id, check_datetime, check_or_create_private_key, check_user, check_integer, \
    check_string
from starkbank.user.credentials import Credentials
from starkbank.user.base import User


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


def create(private_key=None, expiration=3600, user=None):
    private_key = check_or_create_private_key(private_key)

    response, errors = request.post(
        user=check_user(user),
        endpoint="session",
        body={
            "publicKey": private_key.publicKey().toPem(),
            "expiration": check_integer(expiration),
            "platform": "api",
        }
    )

    if errors:
        return None, errors

    session_info = response["session"]

    return Session(
        private_key=private_key.toPem(),
        session_id=session_info["id"],
        expiration=session_info["expiration"],
    ), []


def retrieve(session_id, user=None):
    response, errors = request.get(
        user=check_user(user),
        endpoint="session/{session_id}".format(session_id=session_id),
    )

    if errors:
        return None, errors

    session_info = response["session"]

    return Session(
        private_key=None,
        session_id=session_info["id"],
        expiration=session_info["expiration"],
    ), []


def list(limit=100, cursor=None, user=None):
    url_params = {
        "limit": limit,
    }
    if cursor:
        url_params["cursor"] = check_string(cursor)

    response, errors = request.get(
        user=check_user(user),
        endpoint="session",
        url_params=url_params,
    )

    if errors:
        return None, errors

    sessions = response["sessions"]

    return [Session(
        private_key=None,
        session_id=session_info["id"],
        expiration=session_info["expiration"],
    ) for session_info in sessions], []


def delete(session_id, user=None):
    response, errors = request.delete(
        user=check_user(user),
        endpoint="session/{session_id}".format(session_id=session_id),
    )

    if errors:
        return None, errors

    session_info = response["session"]

    return Session(
        private_key=None,
        session_id=session_info["id"],
        expiration=session_info["expiration"],
    ), []