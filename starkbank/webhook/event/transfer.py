from starkbank.utils.base import Base
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_datetime


class TransferMessage(Base):

    _known_fields = {
        "status",
        "name",
        "created",
        "account_number",
        "tax_id",
        "branch_code",
        "amount",
        "workspace_id",
        "id",
        "tags",
        "errors",
    }
    _known_camel_fields = {snake_to_camel(field) for field in _known_fields}

    def __init__(self, status, name, created, account_number, tax_id, branch_code, amount, id, tags, errors=None, workspace_id=None):   # TODO: remove None
        Base.__init__(self, id=id)

        self.status = status
        self.errors = errors
        self.name = name
        self.created = check_datetime(created)
        self.account_number = account_number
        self.tax_id = tax_id
        self.branch_code = branch_code
        self.amount = amount
        self.workspace_id = workspace_id
        self.tags = tags
