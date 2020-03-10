from ..transfer import Transfer
from ...utils.api import define_compatibility_fields
from ...utils.checks import check_datetime
from ...utils.base import Base


class TransferLog(Base):
    def __init__(self, id, created, type, errors, transfer):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.transfer = Transfer.from_json(transfer)


define_compatibility_fields(TransferLog)
