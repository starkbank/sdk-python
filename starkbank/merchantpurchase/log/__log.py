from starkcore.utils.resource import Resource
from ...utils import rest
from starkcore.utils.checks import check_date


class Log(Resource):
    """# MerchantPurchaseLog object
    Check out our API Documentation at https://starkbank.com/docs/api#merchant-purchase
    """

    def __init__(self, id, created, type, errors, purchase):
        Resource.__init__(self, id=id)

        self.created = check_date(created)
        self.type = type
        self.errors = errors
        self.purchase = purchase

_resource = {"class": Log, "name": "MerchantPurchaseLog"}


def get(id, user=None):
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, user=None):
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, types=None, ids=None, user=None):
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        ids=ids,
        user=user,
    )

