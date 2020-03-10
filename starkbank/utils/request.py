from sys import version_info as python_version
from json import dumps
from time import time
import requests
from ellipticcurve.ecdsa import Ecdsa
from .compatibility import urlencode
from starkbank.exceptions import Houston, InputError, UnknownException
from starkbank.utils.environment import Environment
from starkbank.utils.checks import check_user
from starkbank import __version__ as starkbank_version


_version = "Python-{major}.{minor}.{micro}-SDK-{sdk_version}".format(
    major=python_version.major,
    minor=python_version.minor,
    micro=python_version.micro,
    sdk_version=starkbank_version,
)


def get(user, endpoint, url_params=None, json_response=True):
    return _request(user=user, request_method=requests.get, endpoint=endpoint, url_params=url_params, json_response=json_response)


def post(user, endpoint, body):
    return _request(user=user, request_method=requests.post, endpoint=endpoint, body=body)


def patch(user, endpoint, body):
    return _request(user=user, request_method=requests.patch, endpoint=endpoint, body=body)


def put(user, endpoint, body):
    return _request(user=user, request_method=requests.put, endpoint=endpoint, body=body)


def delete(user, endpoint, url_params=None):
    return _request(user=user, request_method=requests.delete, endpoint=endpoint, url_params=url_params)


def _request(user, request_method, endpoint, url_params=None, body=None, json_response=True):
    user = check_user(user)
    if body is not None:
        body = dumps(body)

    headers = _headers(user=user, body=body)
    url = _url(user=user, endpoint=endpoint, url_params=url_params)

    import starkbank
    if starkbank.debug:
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

    if starkbank.debug:
        print(
            "\n[{elapsed} seconds] retrieved {status}: {content}\n".format(
                elapsed=int(100 * (time() - since)) / 100,
                status=response.status_code,
                content=response.content,
            )
        )

    return _treat_request_response(response=response, json_response=json_response)


def _headers(user, body=None):
    timestamp = str(int(time()))
    message = "{access_id}:{timestamp}:{body}".format(
        access_id=user.credentials.access_id,
        timestamp=timestamp,
        body=body if body else "",
    )
    return {
        "Access-Time": timestamp,
        "Access-Signature": Ecdsa.sign(message=message, privateKey=user.credentials.private_key_object).toBase64(),
        "Access-Id": user.credentials.access_id,
        "Content-Type": "application/json",
        "User-Agent": _version,
    }


def _url(user, endpoint, url_params):
    base_url = {
        Environment.production: "https://api.starkbank.com/v2/",
        Environment.sandbox: "https://sandbox.api.starkbank.com/v2/",
        Environment.development: "https://development.api.starkbank.com/v2/",
    }[user.environment] + endpoint

    url_params = {k: v for k, v in url_params.items() if v is not None} if url_params else None
    url_params = {k: ",".join(v) if isinstance(v, (tuple, list, set)) else v for k, v in url_params.items()} if url_params else None
    query_string = "?" + urlencode(url_params) if url_params else ""

    return base_url + query_string


def _treat_request_response(response, json_response):
    status_code = response.status_code

    if status_code == 200 and json_response:
        return response.json()
    if status_code == 200:
        return response.content
    if status_code >= 500 or "Houston" in str(response.content):
        raise Houston()

    loaded_json = response.json()
    if isinstance(loaded_json, dict) and "errors" in loaded_json:
        raise InputError(loaded_json["errors"])

    raise UnknownException(response.content)