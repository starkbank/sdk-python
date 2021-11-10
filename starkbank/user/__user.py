from ellipticcurve import PrivateKey
from ..utils.checks import check_private_key, check_environment
from ..utils.resource import Resource


class User(Resource):

    def __init__(self, id=None, private_key=None, environment=None):
        Resource.__init__(self, id=id)
        self.pem = check_private_key(private_key)
        self.environment = check_environment(environment)

    def private_key(self):
        return PrivateKey.fromPem(self.pem)
