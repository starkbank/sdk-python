from ellipticcurve.privateKey import PrivateKey
from ..utils.checks import check_private_key, check_environment
from ..utils.resource import Resource


class User(Resource):

    def __init__(self, id=None, private_key=None, environment=None):
        Resource.__init__(self, id=id)
        self.pem = check_private_key(private_key)
        self.environment = check_environment(environment)

    def access_id(self):
        return "{kind}/{id}".format(kind=self.__class__.__name__.lower(), id=self.id)

    def private_key(self):
        return PrivateKey.fromPem(self.pem)

    @classmethod
    def null(cls, environment):
        return User(
            id="",
            private_key=PrivateKey(secret=1).toPem(),
            environment=environment
        )
