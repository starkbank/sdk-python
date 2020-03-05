from hashlib import sha256
from ellipticcurve.curve import secp256k1
from ellipticcurve.privateKey import PrivateKey


def pass_to_key(passphrase, email):
    to_hash = "{email}:STARKBANK:{passphrase}".format(
        email=email,
        passphrase=passphrase,
    )

    try:
        to_hash = to_hash.encode()
    except:
        pass

    secret = int(sha256(to_hash).hexdigest(), 16)

    return PrivateKey(secret=secret, curve=secp256k1).toPem()
