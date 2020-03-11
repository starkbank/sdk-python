from ellipticcurve.privateKey import PrivateKey
from starkbank.utils.environment import Environment
from starkbank.utils.base import Base


class Credentials(Base):
    def __init__(self, environment, access_id, private_key_pem, public_key_pem=None):
        Base.__init__(self, access_id)
        if environment not in Environment.values():
            raise ValueError("environment {} is not in {}".format(environment, Environment.values()))

        private_key = None
        if private_key_pem and not isinstance(private_key_pem, PrivateKey):
            private_key = PrivateKey.fromPem(private_key_pem)

        if private_key:
            private_key_pem = private_key.toPem()
            public_key_pem = private_key.publicKey().toPem()

        self.environment = environment
        self.private_key_object = private_key
        self.private_key = private_key_pem
        self.public_key = public_key_pem
