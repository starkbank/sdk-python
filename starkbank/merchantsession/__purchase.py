from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime


class Purchase(Resource):
    """# Purchase object
     Check out our API Documentation at https://starkbank.com/docs/api#merchant-session
    """

    def __init__(self, amount, card_expiration, card_number, card_security_code, holder_name, funding_type, id=None,
                 holder_email=None, holder_phone=None, installment_count=None, billing_country_code=None,
                 billing_city=None, billing_state_code=None, billing_street_line_1=None, billing_street_line_2=None,
                 billing_zip_code=None, metadata=None, card_ending=None, card_id=None, challenge_mode=None,
                 challenge_url=None, created=None, currency_code=None, end_to_end_id=None, fee=None, network=None,
                 source=None, status=None, tags=None, updated=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.card_expiration = card_expiration
        self.card_number = card_number
        self.card_security_code = card_security_code
        self.holder_name = holder_name
        self.funding_type = funding_type
        self.holder_email = holder_email
        self.holder_phone = holder_phone
        self.installment_count = installment_count
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


_resource = {"class": Purchase, "name": "Purchase"}

