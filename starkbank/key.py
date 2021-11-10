from ellipticcurve import PrivateKey
from os import makedirs, path as os_path


def create(path=None):
    """# Generate a new key pair
    Generates a secp256k1 ECDSA private/public key pair to be used in the API authentications
    ## Parameters (optional):
        path [string]: path to save the keys .pem files. No files will be saved if this parameter isn't provided
    ## Return:
        private and public key pems
    """

    private = PrivateKey()
    public = private.publicKey()

    private_pem = private.toPem()
    public_pem = public.toPem()

    if path is not None:
        if not os_path.exists(path):
            makedirs(path)
        with open(os_path.join(path, "private-key.pem"), "w") as file:
            file.write(private_pem)
        with open(os_path.join(path, "public-key.pem"), "w") as file:
            file.write(public_pem)

    return private_pem, public_pem
