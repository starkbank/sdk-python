from starkcore.utils.resource import Resource
from ..utils import rest
from starkcore.utils.api import from_api_json
from .allowedinstallment.__allowedinstallment import AllowedInstallment
from .allowedinstallment.__allowedinstallment import _sub_resource as _allowed_installments_sub_resource
from starkcore.utils.checks import check_date, check_datetime
from .__purchase import _resource as purchase_resource


class MerchantSession(Resource):
    """# MerchantSession object
    Check out our API Documentation at https://starkbank.com/docs/api#merchant-session
    """

    def __init__(self, allowed_funding_types, allowed_installments, expiration, id=None, allowed_ips=None,
                 challenge_mode=None, created=None, status=None, tags=None, updated=None, uuid=None):
        Resource.__init__(self, id=id)

        self.allowed_funding_types = allowed_funding_types
        self.allowed_installments = _parse_allowed_installments(allowed_installments)
        self.allowed_ips = allowed_ips
        self.challenge_mode = challenge_mode
        self.expiration = expiration
        self.status = status
        self.tags = tags
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)
        self.uuid = uuid


_resource = {"class": MerchantSession, "name": "MerchantSession"}


def _parse_allowed_installments(allowed_installments):
    if allowed_installments is None:
        return []
    parsed_allowed_installments = []
    for allowed_installment in allowed_installments:
        if isinstance(allowed_installment, AllowedInstallment):
            parsed_allowed_installments.append(allowed_installment)
            continue
        parsed_allowed_installments.append(from_api_json(_allowed_installments_sub_resource, allowed_installment))
    return parsed_allowed_installments


def create(merchant_session, user=None):
    return rest.post_single(resource=_resource, entity=merchant_session, user=user)


def get(id, user=None):
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, status=None, tags=None, ids=None, after=None, before=None, user=None):
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


def page(cursor=None, limit=None, status=None, tags=None, ids=None, after=None, before=None, user=None):
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


def purchase(uuid, purchase, user=None):
    return rest.post_sub_resource(resource=_resource, id=uuid, sub_resource=purchase_resource, entity=purchase, user=user)

