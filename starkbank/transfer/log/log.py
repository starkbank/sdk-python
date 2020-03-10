from ..transfer import Transfer
from ...utils.base import Base
from ...utils.checks import check_datetime


class TransferLog(Base):
    def __init__(self, id, created, type, errors, transfer):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.transfer = Transfer.from_json(transfer)


TransferLog._define_known_fields()
