from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_date, check_datetime, check_datetime_or_date


class MerchantInstallment(Resource):
    """# MerchantInstallment object
    Check out our API Documentation at https://starkbank.com/docs/api#merchant-installment
    """

    def __init__(self, id=None, amount=None, created=None, due=None, fee=None, funding_type=None, network=None,
                 purchase_id=None, status=None, tags=None, transaction_ids=None, updated=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.due = check_datetime_or_date(due)
        self.fee = fee
        self.funding_type = funding_type
        self.network = network
        self.purchase_id = purchase_id
        self.status = status
        self.tags = tags
        self.transaction_ids = transaction_ids
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": MerchantInstallment, "name": "MerchantInstallment"}


def get(id, user=None):
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, status=None, tags=None, ids=None, user=None, purchase_ids=None):
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        tags=tags,
        ids=ids,
        user=user,
        purchase_ids=purchase_ids,
    )


def page(cursor=None, limit=None, after=None, before=None, status=None, tags=None, ids=None, user=None, purchase_ids=None):
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        tags=tags,
        ids=ids,
        user=user,
        purchase_ids=purchase_ids,
    )

