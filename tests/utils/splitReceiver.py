from copy import deepcopy
from random import choice, randint
from starkbank import SplitReceiver
from tests.utils.names.names import get_full_name
from tests.utils.taxIdGenerator import TaxIdGenerator

example_receiver = SplitReceiver(
    name="João",
    tax_id="01234567890",
    bank_code=choice(["18236120", "60701190"]),
    branch_code="0001",
    account_number="10000-0",
    account_type="checking"
)


def generateExampleSplitReceiversJson(n=1):
    receivers = []
    for _ in range(n):
        receiver = deepcopy(example_receiver)
        receiver.name = get_full_name()
        receiver.branch_code = str(randint(1, 999))
        receiver.tax_id = TaxIdGenerator.taxId()
        receiver.account_type = choice(["checking", "savings", "salary", "payment"])
        receiver.account_number = "{}-{}".format(randint(10000, 100000000), randint(0, 9))
        receivers.append(receiver)
    return receivers
