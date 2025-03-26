from ...utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.api import from_api_json
from starkcore.utils.checks import check_date, check_datetime
from ..__merchantinstallment import _resource as _merchant_installment_resource


class Log(Resource):
    """# merchantinstallment.Log object
    Check out our API Documentation at https://starkbank.com/docs/api#merchant-installment
    """

    def __init__(self, id, created, updated, type, errors, installment):
        Resource.__init__(self, id=id)
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)
        self.type = type
        self.errors = errors
        self.installment = from_api_json(_merchant_installment_resource, installment)


_resource = {"class": Log, "name": "MerchantInstallmentLog"}


def get(id, user=None):
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, types=None, user=None, installment_ids=None):
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        user=user,
        installment_ids=installment_ids,
    )


def page(cursor=None, limit=None, after=None, before=None, types=None, user=None, installment_ids=None):
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        user=user,
        installment_ids=installment_ids,
    )

