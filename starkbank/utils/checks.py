from builtins import str
from datetime import datetime
from ellipticcurve.privateKey import PrivateKey
from ..settings import settings
from ..user.base import User


def check_user(user):
    if not user:
        user = settings.default_user
        if not user:
            raise RuntimeError("no user passed and no default user set")
    assert isinstance(user, User)
    return user


def check_list_of_strings(list_of_strings):
    if not list_of_strings:
        return []

    assert isinstance(list_of_strings, list)
    for string in list_of_strings:
        assert isinstance(string, str)

    return list_of_strings


def check_string(string):
    assert isinstance(string, str)
    return str(string)


def check_private_key(private_key_pem):
    return PrivateKey.fromPem(private_key_pem)


def check_or_create_private_key(private_key_pem):
    if private_key_pem:
        return check_private_key(private_key_pem)
    return PrivateKey()


def check_id(id):
    id = str(id)
    assert id.isdigit()
    return id


def check_integer(integer):
    assert isinstance(integer, int)
    return integer


def check_datetime(data):
    if data is None:
        return None

    if isinstance(data, datetime):
        return data

    if not isinstance(data, str):
        raise RuntimeError("data must be a string or a datetime")

    try:
        return datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f+00:00")
    except:
        pass

    try:
        return datetime.strptime(data, "%Y-%m-%d")
    except:
        pass

    try:
        return datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
    except:
        pass

    try:
        return datetime.strptime(data, "%Y-%m-%d %H:%M:%S.%f")
    except:
        pass

    raise RuntimeError("invalid datetime string " + data)
