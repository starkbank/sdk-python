import os
from copy import deepcopy
from uuid import uuid4
import starkbank.corporateholder
from starkbank import CorporateHolder
from tests.utils.user import exampleProject
from .names.names import get_full_name
from .rule import generateExampleRuleJson

owner_id = os.environ["SANDBOX_ID"] if "SANDBOX_ID" in os.environ else exampleProject.id

example_holder = CorporateHolder(
    name="Iron Bank S.A." + str(uuid4()),
    tags=[
        "Traveler Employee"
    ],
    permissions=[
        starkbank.corporateholder.Permission(
            owner_id=owner_id,
            owner_type="project"
        )
    ]
)

def generateExampleHoldersJson(n=1):
    holders = []
    for _ in range(n):
        example_holder.name = get_full_name()
        example_holder.rules = generateExampleRuleJson()
        holders.append(deepcopy(example_holder))
    return holders
