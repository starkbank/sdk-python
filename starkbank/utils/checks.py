from datetime import datetime, date


def check_user(user):
    import starkbank
    from ..user.base import User
    from ..user.credentials import Credentials

    user = user or starkbank.user

    if not user:
        raise RuntimeError("no user passed and no default user set")

    if not isinstance(user, User):
        raise TypeError("user must be an object retrieved from one of starkbank.user methods or classes")

    if (not isinstance(user.credentials, Credentials)) or user.credentials.private_key_object is None:
        raise ValueError("user private key is not loaded in credentials")

    return user


def check_datetime(data):
    if data is None:
        return None

    if isinstance(data, (datetime, date)):
        return data

    data = str(data)

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


def check_date_string(data):
    if not data or isinstance(data, str):
        return data
    if not isinstance(data, (datetime, date)):
        raise TypeError("invalid datetime or date " + str(data))
    if data:
        return data.strftime("%Y-%m-%d")
