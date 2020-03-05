from starkbank import settings
from starkbank.old_auth.user import Member
from starkbank.user import member, project, session
from .examples.credentials.credentials import credentialsJson
from .examples.keys.keys import memberPrivateKeyString, memberPublicKeyString, projectPrivateKeyString, \
    projectPublicKeyString, sessionPrivateKeyString, sessionPublicKeyString

settings.env = "development"
#
# exampleMember = member.Member(
#     private_key=memberPrivateKeyString,
#     workspace_id=credentialsJson["workspace"],
#     email=credentialsJson["email"],
# )
#
# exampleProject = project.retrieve(
#     user=exampleMember,
#     id="4835770477051904"
# )
#
# exampleSession = session.create(
#     user=exampleMember,
#     private_key=None,
#     expiration=3600,
# )
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
