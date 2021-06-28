from sys import version_info as python_version
from ellipticcurve.ecdsa import Ecdsa
from json import dumps, loads
from time import time
from ..error import InternalServerError, InputErrors, UnknownError
from ..environment import Environment
from .checks import check_user, check_language
from .url import urlencode
import starkbank


class Response:

    def __init__(self, status, content):
        self.status = status
        self.content = content

    def json(self):
        return loads(self.content.decode("utf-8"))


def fetch(method, path, payload=None, query=None, user=None, version="v2"):
    user = check_user(user or starkbank.user)
    language = check_language(starkbank.language)

    url = {
        Environment.production:  "https://api.starkbank.com/",
        Environment.sandbox:     "https://sandbox.api.starkbank.com/",
    }[user.environment] + version

    url = "{base_url}/{path}{query}".format(base_url=url, path=path, query=urlencode(query))

    agent = "Python-{major}.{minor}.{micro}-SDK-{sdk_version}".format(
        major=python_version.major,
        minor=python_version.minor,
        micro=python_version.micro,
        sdk_version=starkbank.version,
    )

    access_time = str(time())
    body = dumps(payload) if payload else ""
    message = "{access_id}:{access_time}:{body}".format(access_id=user.access_id(), access_time=access_time, body=body)
    signature = Ecdsa.sign(message=message, privateKey=user.private_key()).toBase64()

    try:
        headers = {
            "Access-Id": user.access_id(),
            "Access-Time": access_time,
            "Access-Signature": signature,
            "Content-Type": "application/json",
            "User-Agent": agent,
            "Accept-Language": language,
        }
        response = method(
            url=url,
            data=body,
            headers=headers,
            timeout=starkbank.timeout
        )
    except Exception as exception:
        raise UnknownError("{}: {}".format(exception.__class__.__name__, str(exception)))

    debug(debug_message(method, url, headers, payload, response))
    response = Response(status=response.status_code, content=response.content)

    if response.status == 500:
        raise InternalServerError()
    if response.status == 400:
        raise InputErrors(response.json()["errors"])
    if response.status != 200:
        raise UnknownError(response.content)

    return response


def debug(message):
    if not starkbank.debug_file:
        return
    if not starkbank._debug_configuration:
        import logging
        logging.basicConfig(
            filename=starkbank.debug_file,
            filemode='a',
            format='%(asctime)s %(name)s %(levelname)s %(message)s',
            level=logging.DEBUG
        )
        starkbank._debug_configuration = True
    logging.debug(message)


def debug_message(method, url, headers, payload, response):
    from json import dumps
    debugJson = {
        "request": {
            "method": method,
            "url": url,
            "headers": headers,
            "payload": payload,
        },
        "response": {
            "status": response.status_code,
            "payload": response.content,
            "headers": response.headers,
        },
    }
    return dumps(debugJson, default=str)
