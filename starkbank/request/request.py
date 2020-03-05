import requests
from time import time
from json import dumps, loads
from ellipticcurve.ecdsa import Ecdsa
from starkbank.settings import Settings
from starkbank.user.base import User
from starkbank.exceptions import InputError, Houston
from starkbank.models.environment import Environment


def get(user, endpoint, url_params=None):
    credentials = _get_credentials(user)

    return _treat_request_response(
        requests.get(
            url=_get_url(endpoint) + _get_url_params_string(url_params),
            headers=_headers(credentials),
        )
    )


def post(user, endpoint, body):
    credentials = _get_credentials(user)

    body = dumps(body)

    return _treat_request_response(
        requests.post(
            url=_get_url(endpoint),
            headers=_headers(credentials=credentials, body=body),
            data=body,
        )
    )


def patch(user, endpoint, body):
    credentials = _get_credentials(user)

    body = dumps(body)

    return _treat_request_response(
        requests.patch(
            url=_get_url(endpoint),
            headers=_headers(credentials=credentials, body=body),
            data=body,
        )
    )


def put(user, endpoint, body):
    credentials = _get_credentials(user)

    body = dumps(body)

    return _treat_request_response(
        requests.put(
            url=_get_url(endpoint),
            headers=_headers(credentials=credentials, body=body),
            data=body,
        )
    )


def delete(user, endpoint):
    credentials = _get_credentials(user)

    return _treat_request_response(
        requests.delete(
            url=_get_url(endpoint),
            headers=_headers(credentials=credentials),
        )
    )


def _headers(credentials, body=""):
    timestamp = str(int(time()))
    message = "{access_id}:{timestamp}:{body}".format(
        access_id=credentials.access_id,
        timestamp=timestamp,
        body=body,
    )

    return {
        "Access-Time": timestamp,
        "Access-Signature": Ecdsa.sign(message=message, privateKey=credentials.private_key).toBase64(),
        "Access-Id": credentials.access_id,
        "Content-Type": "application/json",
        "User-Agent": "Python-SDK-2.0.0",
    }


def _get_credentials(user):
    assert isinstance(user, User), "user must be the object retrieved from one of starkbank.user methods or classes"

    return user.credentials


def _get_url(endpoint):
    return _get_base_url() + endpoint


def _get_base_url():
    env = Settings.env

    if not env:
        raise RuntimeError("please an environment with starkbank.default.env = \"env\"")

    if env == Environment.production:
        return "https://api.starkbank.com/v2/"

    if env == Environment.sandbox:
        return "https://sandbox.api.starkbank.com/v2/"

    if env == Environment.development:
        return "https://development.api.starkbank.com/v2/"

    raise ValueError("unknown env " + str(env))


def _get_url_params_string(url_params):
    if not url_params:
        return ""

    url_args = []
    for param, values in url_params.items():
        if values:
            url_args.append(
                "{param}={values}".format(
                    param=param,
                    values=",".join(values)
                )
            )

    if not url_args:
        return ""

    return "?" + "&".join(url_args)


def _treat_request_response(response):
    status_code = response.status_code
    content = response.content

    try:
        content = content.encode()
    except:
        pass

    try:
        content = loads(content)
    except:
        pass

    if status_code == 200:
        return content, []

    if status_code >= 500 or "Houston" in content:
        return None, [Houston()]

    return None, [InputError(code=error["code"], message=error["message"]) for error in content["errors"]]
