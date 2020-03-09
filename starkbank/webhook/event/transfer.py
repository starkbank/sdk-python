from starkbank.utils.base import Base
from starkbank.utils.checks import check_datetime


class TransferMessage(Base):

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


TransferMessage._define_known_fields()
