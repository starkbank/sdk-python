from ellipticcurve.privateKey import PrivateKey
from os import path as os_path


def generate(path=None):
    private = PrivateKey()
    public = private.publicKey()

    private_pem = private.toPem()
    public_pem = public.toPem()

    if path is not None:
        with open(os_path.join(path, "private-key.pem"), "w") as file:
            file.write(private_pem)
        with open(os_path.join(path, "public-key.pem"), "w") as file:
            file.write(public_pem)

    return private_pem, public_pem
