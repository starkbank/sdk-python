from json import dumps, loads
from time import time
from ellipticcurve.ecdsa import Ecdsa
from sys import version_info as python_version
from requests import get as GET, post as POST, delete as DELETE, patch as PATCH
from .checks import check_user
from .url import urlencode
from ..exception import InternalServerError, InputErrors, UnknownException
from ..utils.environment import Environment
import starkbank


class Response(object):

    def __init__(self, status, content):
        self.status = status
        self.content = content

    def json(self):
        return loads(self.content)


def fetch(path="/", payload=None, method=GET, query=None, user=None, version="v2"):
    user = check_user(user or starkbank.user)
    url = {
        Environment.production:  "https://api.starkbank.com/{version}".format(version=version),
        Environment.sandbox:     "https://sandbox.api.starkbank.com/{version}".format(version=version),
        Environment.development: "https://development.api.starkbank.com/{version}".format(version=version),
    }.get(user.environment)
    queryString = "?{params}".format(params=urlencode(query)) if query else ""
    userAgent = "Python-{major}.{minor}.{micro}-SDK-{sdk_version}".format(
        major=python_version.major,
        minor=python_version.minor,
        micro=python_version.micro,
        sdk_version=starkbank.__version__,
    )
    return _fetch(url=url, path=path, method=method, payload=payload, query=queryString, user=user, agent=userAgent)


def _fetch(url=None, path="/", method=GET, payload=None, query=None, user=None, agent=None):
    accessTime = time()
    body = dumps(payload) if isinstance(payload, dict) else ""
    message = "{accessId}:{accessTime}:{body}".format(accessId=user.access_id(), accessTime=accessTime, body=body)
    signature = Ecdsa.sign(message=message, privateKey=user.private_key()).toBase64()
    request = method(
        url="{baseUrl}{path}{query}".format(baseUrl=url, path=path, query=query),
        data=body,
        headers={
            "Access-Id": user.access_id(),
            "Access-Time": str(accessTime),
            "Access-Signature": signature,
            "Content-Type": "application/json",
            "User-Agent": agent,
        }
    )
    response = Response(status=request.status_code, content=request.content)
    if response.status == 500:
        raise InternalServerError(response.json()["errors"][0]["message"])
    if response.status == 400:
        raise InputErrors(response.json()["errors"])
    if response.status != 200:
        raise UnknownException(response.content)
    return response
