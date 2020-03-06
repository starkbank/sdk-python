import requests
from time import time
from json import dumps, loads
from ellipticcurve.ecdsa import Ecdsa
from starkbank.settings import Settings
from starkbank.user.base import User
from starkbank.exceptions import InputError, Houston
from starkbank.models.environment import Environment
from starkbank.user.credentials import Credentials


def get(user, endpoint, url_params=None, json_response=True):
    return _make_request(user=user, request_method=requests.get, endpoint=endpoint, url_params=url_params, json_response=json_response)


def post(user, endpoint, body):
    return _make_request(user=user, request_method=requests.post, endpoint=endpoint, body=body)


def patch(user, endpoint, body):
    return _make_request(user=user, request_method=requests.patch, endpoint=endpoint, body=body)


def put(user, endpoint, body):
    return _make_request(user=user, request_method=requests.put, endpoint=endpoint, body=body)


def delete(user, endpoint):
    return _make_request(user=user, request_method=requests.delete, endpoint=endpoint)


def _make_request(user, request_method, endpoint, url_params=None, body=None, json_response=True):
    credentials = _get_credentials(user)

    if body is not None:
        body = dumps(body)

    url = _get_url(endpoint) + _get_url_params_string(url_params)
    headers = _headers(credentials=credentials, body=body)

    if Settings.logging == "debug":
        since = time()
        print(
            "\nsending /{request_method} to \"{url}\" with:\nheaders: {headers}\nbody: {body}\n".format(
                request_method=request_method.__name__.upper(),
                url=url,
                headers=headers,
                body=body,
            )
        )

    response = request_method(
        url=url,
        headers=headers,
        data=body,
    )

    if Settings.logging == "debug":
        print(
            "\n[{elapsed} seconds] retrieved {status}: {content}\n".format(
                elapsed=int(10 * (time() - since)) / 10,
                status=response.status_code,
                content=response.content,
            )
        )

    treated = _treat_request_response(response=response, json_response=json_response)

    return treated


def _headers(credentials, body=None):
    timestamp = str(int(time()))
    message = "{access_id}:{timestamp}:{body}".format(
        access_id=credentials.access_id,
        timestamp=timestamp,
        body=body if body else "",
    )

    return {
        "Access-Time": timestamp,
        "Access-Signature": Ecdsa.sign(message=message, privateKey=credentials.private_key_object).toBase64(),
        "Access-Id": credentials.access_id,
        "Content-Type": "application/json",
        "User-Agent": "Python-SDK-2.0.0",
    }


def _get_credentials(user):
    assert isinstance(user, User), "user must be the object retrieved from one of starkbank.user methods or classes"
    credentials = user.credentials
    assert isinstance(credentials, Credentials), "user private key is not loaded"
    assert credentials.private_key_object is not None, "user has no loaded credentials"

    return user.credentials


def _get_url(endpoint):
    return _get_base_url() + endpoint


def _get_base_url():
    env = Settings.env

    if not env:
        raise RuntimeError("please set an environment with starkbank.default.env = \"env\"")

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
                    values=",".join(values) if isinstance(values, list) else values
                )
            )

    if not url_args:
        return ""

    return "?" + "&".join(url_args)


def _treat_request_response(response, json_response):
    status_code = response.status_code
    content = response.content

    try:
        content = content.encode()
    except:
        pass

    if json_response:
        try:
            content = loads(content)
        except:
            pass

    if status_code == 200:
        return content, []

    if status_code >= 500 or "Houston" in content:
        return None, [Houston()]

    return None, [InputError(code=error["code"], message=error["message"]) for error in content["errors"]]
