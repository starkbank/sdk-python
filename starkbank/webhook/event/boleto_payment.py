from starkbank.utils.base import Base


class BoletoPaymentMessage(Base):

    def __init__(self, status, scheduled, description, tags, bar_code, line, id):
        Base.__init__(self, id=id)

        self.status = status
        self.scheduled = scheduled
        self.description = description
        self.tags = tags
        self.bar_code = bar_code
        self.line = line


BoletoPaymentMessage._define_known_fields()
