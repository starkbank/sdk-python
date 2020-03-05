from ellipticcurve.privateKey import PrivateKey


class Credentials:
    def __init__(self, access_id, private_key):
        if private_key and not isinstance(private_key, PrivateKey):
            private_key = PrivateKey.fromPem(private_key)

        private_key_pem, public_key_pem = None, None
        if private_key:
            private_key_pem = private_key.toPem()
            public_key_pem = private_key.publicKey().toPem()

        self.access_id = access_id
        self.private_key = private_key
        self.private_key_pem = private_key_pem
        self.public_key_pem = public_key_pem
