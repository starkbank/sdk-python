from starkbank import request
from starkbank.utils.base import Base
from starkbank.utils.case import snake_to_camel
from starkbank.utils.checks import check_user


class Transfer(Base):
    _known_fields = {
        "id",
        "tax_id",
        "amount",
        "name",
        "bank_code",
        "branch_code",
        "account_number",
        "tags",
    }
    _known_camel_fields = {snake_to_camel(field) for field in _known_fields}

    def __init__(self, amount, name, tax_id, bank_code, branch_code, account_number, tags=None, id=None):
        Base.__init__(self, id=id)

        self.tax_id = tax_id
        self.amount = amount
        self.name = name
        self.bank_code = bank_code
        self.branch_code = branch_code
        self.account_number = account_number
        self.tags = tags


def create(transfers, user=None):
    response = request.post(
        user=check_user(user),
        endpoint="transfer",
        body={
            "transfers": [
                {snake_to_camel(k): v for k, v in transfer.json().items() if v is not None} for transfer in transfers
            ]
        }
    )

    return [
       Transfer.from_json(transfer) for transfer in response["transfers"]
    ]


def retrieve(id, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="transfer/{id}".format(id=id),
    )

    return Transfer.from_json(response["transfer"])


def retrieve_pdf(id, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="transfer/{id}/pdf".format(id=id),
        json_response=False,
    )

    return response


def list(limit=100, cursor=None, user=None):
    response = request.get(
        user=check_user(user),
        endpoint="transfer",
        url_params={
            "limit": limit,
            "cursor": cursor,
        },
    )

    return [Transfer.from_json(transfer) for transfer in response["transfers"]]


def delete(ids, user=None):
    if len(ids) > 100:
        raise ValueError("ids cannot have more than 100 elements")

    transfers = []
    for id in ids:
        response = request.delete(
            user=check_user(user),
            endpoint="transfer/{id}".format(id=id),
        )

        transfers.append(Transfer.from_json(response["transfer"]))

    return transfers
