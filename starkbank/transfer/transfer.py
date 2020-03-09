from starkbank.utils.base import Base, Post, Get, GetId, GetPdf, Delete


class Transfer(Post, Get, GetId, GetPdf, Delete):

    def __init__(self, amount, name, tax_id, bank_code, branch_code, account_number, fee=None, tags=None, status=None, id=None):
        Base.__init__(self, id=id)

        self.tax_id = tax_id
        self.amount = amount
        self.fee = fee
        self.name = name
        self.bank_code = bank_code
        self.branch_code = branch_code
        self.account_number = account_number
        self.tags = tags
        self.status = status

    @classmethod
    def _query(cls, limit=100, request_id=None, transaction_ids=None, tags=None, after=None, before=None, status=None, sort=None):
        return super(Transfer, cls)._query(
            limit=limit,
            request_id=request_id,
            transaction_ids=transaction_ids,
            tags=tags,
            after=after,
            before=before,
            status=status,
            sort=sort,
        )


Transfer._define_known_fields()


create = Transfer._post
query = Transfer._query
get = Transfer._get_id
get_pdf = Transfer._get_pdf
delete = Transfer._delete
