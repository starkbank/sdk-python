from ..utils import rest
from ..transfer.rule.__rule import Rule
from ..transfer.rule.__rule import _sub_resource as _rule_resource
from starkcore.utils.api import from_api_json
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_datetime_or_date


class VerifiedTransfer(Resource):
    """# VerifiedTransfer object
    When you initialize a VerifiedTransfer, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    ## Parameters (required):
    - amount [integer]: amount in cents to be transferred. ex: 1234 (= R$ 12.34)
    - account_id [string]: receiver's VerifiedAccount ID. ex: "5656565656565656"
    ## Parameters (optional):
    - external_id [string, default None]: url safe string that must be unique among all your transfers. Duplicated external_ids will cause failures. ex: "my-internal-id-123456"
    - scheduled [datetime.date, datetime.datetime or string, default now]: date or datetime when the transfer will be processed. May be pushed to next business day if necessary. ex: datetime.datetime(2020, 11, 12, 0, 14, 22)
    - description [string, default None]: optional description to override default description to be shown in the bank statement. ex: "Payment for service #1234"
    - display_description [string, default None]: optional description to be shown in the receiver bank interface. ex: "Payment for service #1234"
    - tags [list of strings, default []]: list of strings for reference when searching for verified transfers. ex: ["employees", "monthly"]
    - rules [list of Transfer.Rules, default []]: list of Transfer.Rule objects for modifying transfer behavior. ex: [Transfer.Rule(key="resendingLimit", value=5)]
    ## Attributes (return-only):
    - id [string]: unique id returned when the VerifiedTransfer is created. ex: "5656565656565656"
    - fee [integer]: fee charged when the transfer is created. ex: 200 (= R$ 2.00)
    - status [string]: current verified transfer status. ex: "created", "processing", "success" or "failed"
    - transaction_ids [list of strings]: ledger transaction IDs linked to this transfer (if there are two, the second is the chargeback). ex: ["19827356981273"]
    - metadata [dictionary]: dictionary object used to store additional information about the VerifiedTransfer object.
    - created [datetime.datetime]: creation datetime for the verified transfer. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the verified transfer. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, amount, account_id, external_id=None, scheduled=None,
                 description=None, display_description=None, tags=None, rules=None, id=None,
                 fee=None, status=None, transaction_ids=None, metadata=None, created=None, updated=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.account_id = account_id
        self.external_id = external_id
        self.scheduled = check_datetime_or_date(scheduled)
        self.description = description
        self.display_description = display_description
        self.tags = tags
        self.rules = _parse_rules(rules)
        self.fee = fee
        self.status = status
        self.transaction_ids = transaction_ids
        self.metadata = metadata
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": VerifiedTransfer, "name": "VerifiedTransfer"}


def _parse_rules(rules):
    if rules is None:
        return None
    parsed_rules = []
    for rule in rules:
        if isinstance(rule, Rule):
            parsed_rules.append(rule)
            continue
        parsed_rules.append(from_api_json(_rule_resource, rule))
    return parsed_rules


def create(verified_transfers, user=None):
    """# Create VerifiedTransfers
    Send a list of VerifiedTransfer objects for creation in the Stark Bank API
    ## Parameters (required):
    - verified_transfers [list of VerifiedTransfer objects]: list of VerifiedTransfer objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of VerifiedTransfer objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=verified_transfers, user=user)
