import starkbank
from uuid import uuid4


def generateExampleWorkspace():
    id = uuid4()
    return starkbank.Workspace(
        username="starkv2-{id}".format(id=id),
        name="Stark V2: {id}".format(id=id),
    )
