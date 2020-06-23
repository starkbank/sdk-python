from sys import version_info as python_version
from ellipticcurve.ecdsa import Ecdsa
from json import dumps, loads
from time import time
from ..error import InternalServerError, InputErrors, UnknownError
from ..environment import Environment
from .checks import check_user, check_language, check_environment
from .url import urlencode
import starkbank


class Response:

    def __init__(self, status, content):
        self.status = status
        self.content = content

    def json(self):
        return loads(self.content.decode("utf-8"))


def fetch(method, path, payload=None, query=None, user=None, environment=None, version="v2"):
    language = check_language(starkbank.language)

    if not environment:
        user = check_user(user or starkbank.user)
        environment = user.environment

    url = {
        Environment.production:  "https://api.starkbank.com/",
        Environment.sandbox:     "https://sandbox.api.starkbank.com/",
    }[check_environment(environment)] + version

    url = "{base_url}/{path}{query}".format(base_url=url, path=path, query=urlencode(query))

    agent = "Python-{major}.{minor}.{micro}-SDK-{sdk_version}".format(
        major=python_version.major,
        minor=python_version.minor,
        micro=python_version.micro,
        sdk_version=starkbank.version,
    )

    headers = {
        "Content-Type": "application/json",
        "Accept-Language": language,
        "User-Agent": agent,
    }

    body = dumps(payload) if payload else ""

    if user:
        access_time = str(time())
        message = "{access_id}:{access_time}:{body}".format(access_id=user.access_id(), access_time=access_time, body=body)
        signature = Ecdsa.sign(message=message, privateKey=user.private_key()).toBase64()
        headers.update({
            "Access-Id": user.access_id(),
            "Access-Time": access_time,
            "Access-Signature": signature,
        })

    try:
        request = method(
            url=url,
            data=body,
            headers=headers,
        )
    except Exception as exception:
        raise UnknownError("{}: {}".format(exception.__class__.__name__, str(exception)))

    response = Response(status=request.status_code, content=request.content)

    if response.status == 500:
        raise InternalServerError()
    if response.status == 400:
        raise InputErrors(response.json()["errors"])
    if response.status != 200:
        raise UnknownError(response.content)

    return response
