from starkcore.utils.resource import Resource
from ...utils import rest
from starkcore.utils.api import from_api_json
from starkcore.utils.checks import check_date, check_datetime
from ..__merchantsession import _resource as _merchant_session_resource


class Log(Resource):
    """# merchantsession.Log object
    Check out our API Documentation at https://starkbank.com/docs/api#merchant-session
    """

    def __init__(self, id, created, type, errors, session):
        Resource.__init__(self, id=id)
        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.session = from_api_json(_merchant_session_resource, session)


_resource = {"class": Log, "name": "MerchantSessionLog"}


def get(id, user=None):
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, types=None, session_ids=None, user=None):
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        session_ids=session_ids,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, types=None, session_ids=None, user=None):
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        session_ids=session_ids,
        user=user,
    )

