from datetime import datetime, date


def check_environment(environment):
    from ..environment import Environment
    environments = Environment.values()
    assert environment in environments, "Select a valid environment: {}".format(", ".join(environments))
    return environment


def check_private_key(pem):
    from ellipticcurve.privateKey import PrivateKey
    try:
        assert PrivateKey.fromPem(pem).curve.name == "secp256k1"
    except:
        raise Exception("Private-key must be valid secp256k1 ECDSA string in pem format")
    return pem


def check_user(user):
    from ..user.__user import User
    assert isinstance(user, User), "A user is required to access our API. Check our README: https://github.com/starkbank/sdk-python/"
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

    if isinstance(data, datetime):
        return data.date()

    if isinstance(data, date):
        return data

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

    try:
        return datetime.strptime(data, "%Y-%m-%dT%H:%M:%S+00:00")
    except:
        pass

    raise RuntimeError("invalid datetime string " + data)
