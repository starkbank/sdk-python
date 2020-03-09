from starkbank.utils.base import Base, Post, Get, GetId, GetPdf, BaseDelete
from starkbank.utils.case import snake_to_camel


class Transfer(Post, Get, GetId, GetPdf, BaseDelete):
    _known_fields = {
        "id",
        "status",
        "tax_id",
        "amount",
        "name",
        "bank_code",
        "branch_code",
        "account_number",
        "tags",
    }
    _known_camel_fields = {snake_to_camel(field) for field in _known_fields}

    def __init__(self, amount, name, tax_id, bank_code, branch_code, account_number, tags=None, status=None, id=None):
        Base.__init__(self, id=id)

        self.tax_id = tax_id
        self.amount = amount
        self.name = name
        self.bank_code = bank_code
        self.branch_code = branch_code
        self.account_number = account_number
        self.tags = tags
        self.status = status


create = Transfer._create
list = Transfer._list
get = Transfer._get
get_pdf = Transfer.get_pdf
delete = Transfer.delete
