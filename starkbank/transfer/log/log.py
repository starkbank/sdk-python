from ..transfer import Transfer
from ...utils.api import define_compatibility_fields, from_api_json
from ...utils.checks import check_datetime
from ...utils.base import Base


class TransferLog(Base):
    def __init__(self, id, created, type, errors, transfer):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.transfer = from_api_json(Transfer, transfer)


define_compatibility_fields(TransferLog)
