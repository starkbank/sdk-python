from ... import request
from ...utils.checks import check_string, check_integer, check_or_create_private_key, check_user
from .session import Session


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
