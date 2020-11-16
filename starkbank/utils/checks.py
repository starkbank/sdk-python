from datetime import datetime, date, timedelta


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


def check_language(language):
    accepted_languages = ["en-US", "pt-BR"]
    assert language in accepted_languages, "Language must be one from {}".format(accepted_languages)
    return language


def check_datetime_or_date(data):
    if data is None:
        return None

    if type(data) == datetime:
        return data

    if isinstance(data, date):
        return data

    data, dt_type = check_datetime_string(data)

    return data.date() if dt_type == date else data


def check_datetime(data):
    if data is None:
        return None

    if type(data) == datetime:
        return data

    if isinstance(data, date):
        return datetime(data.year, data.month, data.day)

    return check_datetime_string(data)[0]


def check_date(data):
    if data is None:
        return None

    if isinstance(data, datetime):
        return data.date()

    if isinstance(data, date):
        return data

    data, type = check_datetime_string(data)

    return data.date() if type == date else data


def check_timedelta(data):
    if data is None:
        return None

    if isinstance(data, timedelta):
        return data

    try:
        return timedelta(seconds=data)
    except:
        raise TypeError(
            "invalid timedelta {data}, please use an integer in seconds or a datetime.timedelta object".format(data=data)
        )


def check_datetime_string(data):
    data = str(data)

    try:
        return datetime.strptime(data, "%Y-%m-%d"), date
    except:
        pass

    try:
        return datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f+00:00"), datetime
    except:
        pass

    try:
        return datetime.strptime(data, "%Y-%m-%dT%H:%M:%S+00:00"), datetime
    except:
        pass

    raise RuntimeError("invalid datetime string " + data)
