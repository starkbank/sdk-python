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


class Response:

    def __init__(self, status, content):
        print(content)
        self.status = status
        self.content = content

    def json(self):
        return loads(self.content)


def fetch(path="/", payload=None, method=GET, query=None, user=None, version="v2"):
    user = check_user(user or starkbank.user)
    url = {
        Environment.production:  "https://api.starkbank.com/" + version,
        Environment.sandbox:     "https://sandbox.api.starkbank.com/" + version,
        Environment.development: "https://development.api.starkbank.com/" + version,
    }[user.environment]

    query_string = "?" + urlencode(query) if query else ""
    url = "{baseUrl}{path}{query}".format(baseUrl=url, path=path, query=query_string)

    print(url)

    agent = "Python-{major}.{minor}.{micro}-SDK-{sdk_version}".format(
        major=python_version.major,
        minor=python_version.minor,
        micro=python_version.micro,
        sdk_version=starkbank.__version__,
    )

    access_time = str(time())
    body = dumps(payload) if payload else ""
    message = "{access_id}:{access_time}:{body}".format(access_id=user.access_id(), access_time=access_time, body=body)
    signature = Ecdsa.sign(message=message, privateKey=user.private_key()).toBase64()

    print(body)

    try:
        request = method(
            url=url,
            data=body,
            headers={
                "Access-Id": user.access_id(),
                "Access-Time": access_time,
                "Access-Signature": signature,
                "Content-Type": "application/json",
                "User-Agent": agent,
            }
        )
    except Exception as exception:
        raise UnknownException("{}: {}".format(exception.__class__.__name__, str(exception)))

    response = Response(status=request.status_code, content=request.content)

    if response.status == 500:
        raise InternalServerError()
    if response.status == 400:
        raise InputErrors(response.json()["errors"])
    if response.status != 200:
        raise UnknownException(response.content)

    return response
