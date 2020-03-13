from datetime import datetime, date


def check_environment(environment):
    from .environment import Environment
    environments = Environment.values()
    assert environment in environments, "Select one valid environment: {}".format(", ".join(environments))
    return environment


def check_user_kind(kind):
    kinds = ["project", "session", "member"]
    assert kind in kinds, "Select one valid user kind: {}".format(", ".join(kinds))
    return kind


def check_private_key(pem):
    from ellipticcurve.privateKey import PrivateKey
    try:
        PrivateKey.fromPem(pem)
    except:
        raise Exception("This private key is invalid. Try another one")
    return pem


def check_user(user):
    from ..user.user import User
    assert isinstance(user, User), "It's required to have a user to access our API. Check our docs: https://github.com/starkbank/sdk-python/"
    return user


def check_datetime(data):
    if data is None:
        return None

    if isinstance(data, datetime):
        return data

    if isinstance(data, date):
        return datetime(data.year, data.month, data.day)

    return check_datetime_string(data)


def check_date(data):
    if data is None:
        return None

    if isinstance(data, date):
        return data

    if isinstance(data, datetime):
        return data.date()

    data = check_datetime_string(data)

    return data.date()


def check_datetime_string(data):
    data = str(data)

    try:
        return datetime.strptime(data, "%Y-%m-%d")
    except:
        pass

    try:
        return datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f+00:00")
    except:
        pass

    raise RuntimeError("invalid datetime string " + data)
