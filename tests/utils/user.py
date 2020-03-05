from starkbank.old_auth.user import Member
from .examples.credentials.credentials import credentialsJson
from .examples.keys.keys import memberPrivateKeyString, memberPublicKeyString, sessionPublicKeyString, \
    sessionPrivateKeyString, projectPrivateKeyString, projectPublicKeyString

exampleMember = Member(
    credentialsJson=credentialsJson,
    privateKeyString=memberPrivateKeyString,
    publicKeyString=memberPublicKeyString,
)

exampleProject = exampleMember.newProject(
    name="testProject",
    privateKeyString=projectPrivateKeyString,
    publicKeyString=projectPublicKeyString,
    platform="web",
    # allowedIps=["123"]
)

exampleSession = exampleMember.newSession(
    privateKeyString=sessionPrivateKeyString,
    publicKeyString=sessionPublicKeyString,
    platform="web"
)
