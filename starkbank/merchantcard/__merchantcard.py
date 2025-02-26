from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_date, check_datetime, check_datetime_or_date

class MerchantCard(Resource):
    """# MerchantCard object
    Check out our API Documentation at https://starkbank.com/docs/api#merchant-card
    """

    def __init__(self, id=None, ending=None , funding_type=None, holder_name=None, network=None, status=None, tags=None,
                 expiration=None, created=None, updated=None):
        Resource.__init__(self, id=id)
        self.ending = ending
        self.funding_type = funding_type
        self.holder_name = holder_name
        self.network = network
        self.status = status
        self.tags = tags
        self.expiration = check_datetime_or_date(expiration)
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": MerchantCard, "name": "MerchantCard"}


def get(id, user=None):
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, status=None, tags=None, ids=None, user=None):
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        tags=tags,
        ids=ids,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, status=None, tags=None, ids=None, user=None):
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
    )
