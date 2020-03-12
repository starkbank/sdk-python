from starkbank.utils import rest
from starkbank.utils.checks import check_datetime, check_date
from starkbank.utils.base import Base


class Transfer(Base):
    """Description: Transfer object

    When you initialize a Transfer, the entity will not necessarily be
    created in the Stark Bank API. The create function sends the object
    to the Stark Bank API and returns the list of validated and created
    objects.

    Parameters (required):
        amount [integer]: amount in cents to be transferred. ex: 1234 (= R$ 12.34)
        name [string]: receiver full name. ex: "Anthony Edward Stark"
        tax_id [string]: receiver tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
        bank_code [string]: receiver 1 to 3 digits of the bank institution in Brazil. ex: "200" or "341"
        branch_code [string]: receiver bank account branch. Use '-' in case there is a verifier digit. ex: "1357-9"
        account_number [string]: Receiver Bank Account number. Use '-' before the verifier digit. ex: "876543-2"
        tags [list of strings]: list of strings for reference when searching transactions (may be empty). ex: ["abc", "transfer"]
    Attrtibutes (return-only):
        id [string, default None]: unique id returned when Boleto is created. ex: "5656565656565656"
        fee [integer, default None]: fee charged when transfer is created. ex: 200 (= R$ 2.00)
        status [string, default None]: current boleto status. ex: "registered" or "paid"
        created [datetime.datetime, default None]: creation datetime for the boleto. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, amount, name, tax_id, bank_code, branch_code, account_number, fee=None, tags=None, status=None, id=None, created=None):
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
        self.created = check_datetime(created)


def create(transfers, user=None):
    return rest.post(resource=Transfer, entities=transfers, user=user)


def get(id, user=None):
    return rest.get_id(resource=Transfer, id=id, user=user)


def get_pdf(id, user=None):
    return rest.get_pdf(resource=Transfer, id=id, user=user)


def query(limit=None, request_id=None, transaction_ids=None, tags=None, after=None, before=None, status=None, sort=None, user=None):
    return rest.query(resource=Transfer, limit=limit, user=user, status=status, tags=tags, after=check_date(after), before=check_date(before), request_id=request_id, transaction_ids=transaction_ids, sort=sort)


def delete(ids, user=None):
    return rest.delete(resource=Transfer, ids=ids, user=user)
