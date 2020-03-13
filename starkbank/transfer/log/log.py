from ..transfer import Transfer
from ...utils.api import from_api_json
from ...utils.checks import check_datetime
from ...utils.resource import Resource


class TransferLog(Resource):

    def __init__(self, id, created, type, errors, transfer):
        Resource.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.transfer = from_api_json(Transfer, transfer)
