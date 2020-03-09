from starkbank import Transfer
from starkbank.utils.base import Base
from starkbank.utils.checks import check_datetime


class TransferLog(Base):
    def __init__(self, id, created, type, errors, transfer):
        Base.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.transfer = Transfer.from_json(transfer)

    @classmethod
    def _endpoint(cls):
        return "transfer/log"


TransferLog._define_known_fields()
