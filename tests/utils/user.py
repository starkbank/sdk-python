import starkbank
from tests.utils.examples.keys.keys import projectPrivateKeyString

starkbank.settings.debug = True

exampleProject = starkbank.Project(
    environment="development",
    id="4835770477051904",
    private_key=projectPrivateKeyString,
)
starkbank.user = exampleProject
starkbank.debug = True
starkbank.settings.user = exampleProject
