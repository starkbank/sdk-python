import requests
from time import time
from json import dumps, loads
from ellipticcurve.ecdsa import Ecdsa
from starkbank.exceptions import Houston, InputError, UnknownException
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

    from starkbank import settings

    if settings.debug:
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

    if settings.debug:
        print(
            "\n[{elapsed} seconds] retrieved {status}: {content}\n".format(
                elapsed=int(100 * (time() - since)) / 100,
                status=response.status_code,
                content=response.content,
            )
        )

    return _treat_request_response(response=response, json_response=json_response)


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
    from starkbank.user.base import User
    assert isinstance(user, User), "user must be an object retrieved from one of starkbank.user methods or classes"
    credentials = user.credentials
    assert isinstance(credentials, Credentials), "user private key is not loaded in credentials"
    assert credentials.private_key_object is not None, "user private key is not loaded in credentials"

    return user.credentials


def _get_url(endpoint):
    return _get_base_url() + endpoint


def _get_base_url():
    from starkbank import settings
    env = settings.environment

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

    if status_code == 200:
        if json_response:
            return _load_json_string(content)
        return content

    if status_code >= 500 or "Houston" in str(content):
        raise Houston()

    loaded_json = _load_json_string(content)

    if isinstance(loaded_json, dict) and "errors" in loaded_json:
        raise InputError(loaded_json["errors"])

    raise UnknownException(content)


def _load_json_string(json):
    try:
        return loads(json)
    except:
        pass
    return json
