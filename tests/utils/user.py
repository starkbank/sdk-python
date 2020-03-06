import starkbank
from starkbank.old_auth.user import Member
from starkbank.user import member, project, session
from tests.utils.examples.credentials.credentials import credentialsJson
from tests.utils.examples.keys.keys import memberPrivateKeyString, memberPublicKeyString, projectPrivateKeyString, \
    projectPublicKeyString, sessionPrivateKeyString, sessionPublicKeyString

starkbank.settings.env = "development"

exampleMember = member.Member(
    private_key=memberPrivateKeyString,
    workspace_id=credentialsJson["workspaceId"],
    email=credentialsJson["email"],
)

exampleProject = project.retrieve(
    user=exampleMember,
    id="4835770477051904"
)

exampleSession = session.create(
    user=exampleMember,
    private_key=None,
    expiration=3600,
)

exampleMemberOld = Member(
    credentialsJson=credentialsJson,
    privateKeyString=memberPrivateKeyString,
    publicKeyString=memberPublicKeyString,
)

exampleProjectOld = exampleMemberOld.newProject(
    name="testProject",
    privateKeyString=projectPrivateKeyString,
    publicKeyString=projectPublicKeyString,
    platform="web",
    # allowedIps=["123"]
)

exampleSessionOld = exampleMemberOld.newSession(
    privateKeyString=sessionPrivateKeyString,
    publicKeyString=sessionPublicKeyString,
    platform="web"
)

starkbank.settings.default_user = exampleMember
