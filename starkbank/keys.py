from ellipticcurve.privateKey import PrivateKey
from pathlib import Path


def generate(path=None):
    private = PrivateKey()
    public = private.publicKey()

    private_pem = private.toPem()
    public_pem = public.toPem()

    if path is not None:
        path = Path(path)
        with open(path / "private-key.pem", "w") as file:
            file.write(private_pem)
        with open(path / "public-key.pem", "w") as file:
            file.write(public_pem)

    return private_pem, public_pem
