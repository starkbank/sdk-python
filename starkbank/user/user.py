from ellipticcurve.privateKey import PrivateKey
from ..utils.checks import check_private_key, check_user_kind, check_environment


class User:

    def __init__(self, id=None, private_key=None, kind=None, environment=None):
        self.id = id
        self.pem = check_private_key(private_key)
        self.kind = check_user_kind(kind)
        self.environment = check_environment(environment)

    def access_id(self):
        return "{kind}/{id}".format(kind=self.kind, id=self.id)

    def private_key(self):
        return PrivateKey.fromPem(self.pem)
