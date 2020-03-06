from starkbank.utils.base import Base
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_datetime


class BoletoPaymentMessage(Base):

    _known_fields = {
        "status",
        "scheduled",
        "description",
        "tags",
        "bar_code",
        "line",
        "id",
    }
    _known_camel_fields = {snake_to_camel(field) for field in _known_fields}

    def __init__(self, status, scheduled, description, tags, bar_code, line, id):
        Base.__init__(self, id=id)

        self.status = status
        self.scheduled = scheduled
        self.description = description
        self.tags = tags
        self.bar_code = bar_code
        self.line = line
