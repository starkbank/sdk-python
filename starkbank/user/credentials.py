from ellipticcurve.privateKey import PrivateKey


class Credentials:
    def __init__(self, access_id, private_key_pem, public_key_pem=None):
        private_key = None
        if private_key_pem and not isinstance(private_key_pem, PrivateKey):
            private_key = PrivateKey.fromPem(private_key_pem)

        if private_key:
            private_key_pem = private_key.toPem()
            public_key_pem = private_key.publicKey().toPem()

        self.access_id = access_id
        self.private_key_object = private_key
        self.private_key = private_key_pem
        self.public_key = public_key_pem

    def __str__(self):
        return "Credentials(access_id={access_id}, private_key={private_key_pem}, public_key={public_key_pem})".format(
            access_id=self.access_id,
            private_key_pem=self.private_key,
            public_key_pem=self.public_key,
        )
