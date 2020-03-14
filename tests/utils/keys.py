from ellipticcurve.publicKey import PublicKey
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.utils.file import File


privateKey = PrivateKey.fromPem(privateKeyString)
publicKey = PublicKey.fromPem(publicKeyString)
