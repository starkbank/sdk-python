from ellipticcurve.utils.file import File

memberPrivateKeyString = File.read("utils/examples/keys/member/privateKey.pem")
memberPublicKeyString = File.read("utils/examples/keys/member/publicKey.pem")

projectPrivateKeyString = File.read("utils/examples/keys/project/privateKey.pem")
projectPublicKeyString = File.read("utils/examples/keys/project/publicKey.pem")

sessionPrivateKeyString = File.read("utils/examples/keys/session/privateKey.pem")
sessionPublicKeyString = File.read("utils/examples/keys/session/publicKey.pem")