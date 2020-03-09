import starkbank
from tests.utils.examples.keys.keys import projectPrivateKeyString

exampleProject = starkbank.Project(
    environment="development",
    id="4835770477051904",
    private_key=projectPrivateKeyString,
)

starkbank.settings.user = exampleProject
starkbank.settings.debug = True
