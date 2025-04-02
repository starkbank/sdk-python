from ...utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.api import from_api_json
from starkcore.utils.checks import check_date, check_datetime
from ..__merchantpurchase import _resource as _merchant_purchase_resource


class Log(Resource):
    """# merchantpurchase.Log object
    Check out our API Documentation at https://starkbank.com/docs/api#merchant-purchase
    """

    def __init__(self, id, created, type, errors, purchase):
        Resource.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.purchase = from_api_json(_merchant_purchase_resource, purchase)


_resource = {"class": Log, "name": "MerchantPurchaseLog"}


def get(id, user=None):
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, types=None, user=None, purchase_ids=None):
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        user=user,
        purchase_ids=purchase_ids,
    )

def page(cursor=None, limit=None, after=None, before=None, types=None, user=None, purchase_ids=None):
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        user=user,
        purchase_ids=purchase_ids,
    )

