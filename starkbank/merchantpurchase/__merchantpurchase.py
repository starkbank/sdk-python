from starkcore.utils.resource import Resource
from ..utils import rest
from starkcore.utils.checks import check_date, check_datetime


class MerchantPurchase(Resource):
    """# MerchantPurchase object
    Check out our API Documentation at https://starkbank.com/docs/api#merchant-purchase
    """

    def __init__(self, amount, card_id, funding_type, installment_count, id=None, card_expiration=None,
                 card_number=None, card_security_code=None,holder_name=None, holder_email=None, holder_phone=None,
                 billing_country_code=None, billing_city=None,billing_state_code=None, billing_street_line_1=None,
                 billing_street_line_2=None, billing_zip_code=None, metadata=None, card_ending=None,
                 challenge_mode=None, challenge_url=None, created=None, currency_code=None, end_to_end_id=None,
                 fee=None, network=None, source=None, status=None, tags=None, updated=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.installment_count = installment_count
        self.card_expiration = card_expiration
        self.card_number = card_number
        self.card_security_code = card_security_code
        self.holder_name = holder_name
        self.holder_email = holder_email
        self.holder_phone = holder_phone
        self.funding_type = funding_type
        self.billing_country_code = billing_country_code
        self.billing_city = billing_city
        self.billing_state_code = billing_state_code
        self.billing_street_line_1 = billing_street_line_1
        self.billing_street_line_2 = billing_street_line_2
        self.billing_zip_code = billing_zip_code
        self.metadata = metadata
        self.card_ending = card_ending
        self.card_id = card_id
        self.challenge_mode = challenge_mode
        self.challenge_url = challenge_url
        self.currency_code = currency_code
        self.end_to_end_id = end_to_end_id
        self.fee = fee
        self.network = network
        self.source = source
        self.status = status
        self.tags = tags
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": MerchantPurchase, "name": "MerchantPurchase"}


def create(merchant_purchase, user=None):
    return rest.post_single(resource=_resource, entity=merchant_purchase, user=user)


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


def update(id, status=None, amount=None, user=None):
    payload = {
        "status": status,
        "amount": amount
    }
    return rest.patch_id(resource=_resource, id=id, user=user, payload=payload)

