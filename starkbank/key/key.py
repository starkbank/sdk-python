from ellipticcurve.privateKey import PrivateKey


def create(path=None):
    private_key = PrivateKey()

    private_key_pem = private_key.toPem()

    if path:
        with open("{path}/PrivateKey.pem", "w") as file:
            file.write(private_key_pem)

    return private_key_pem
