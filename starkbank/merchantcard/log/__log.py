from ...utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.api import from_api_json
from starkcore.utils.checks import check_date, check_datetime
from ..__merchantcard import _resource as _merchant_card_resource


class Log(Resource):
    """# merchantcard.Log object
    Check out our API Documentation at https://starkbank.com/docs/api#merchant-card
    """

    def __init__(self, id, created, updated, type, errors, card):
        Resource.__init__(self, id=id)
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)
        self.type = type
        self.errors = errors
        self.card = from_api_json(_merchant_card_resource, card)


_resource = {"class": Log, "name": "MerchantCardLog"}


def get(id, user=None):
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, card_ids=None, after=None, before=None, user=None, types=None):
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        card_ids=card_ids,
        user=user,
        types=types,
    )


def page(cursor=None, limit=None, card_ids=None, after=None, before=None, user=None, types=None):
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        card_ids=card_ids,
        user=user,
    )

