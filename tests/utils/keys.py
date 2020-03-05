from ellipticcurve.publicKey import PublicKey
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.utils.file import File

privateKeyString = File.read("examples/keys/member/privateKey.pem")
publicKeyString = File.read("examples/keys/member/publicKey.pem")
privateKey = PrivateKey.fromPem(privateKeyString)
publicKey = PublicKey.fromPem(publicKeyString)
