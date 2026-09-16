from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime


class Purchase(Resource):
    """# Purchase object
     Check out our API Documentation at https://starkbank.com/docs/api#merchant-session
    ## Parameters (required):
    - amount [integer]: Purchase value in cents. ex: 1234 (= R$ 12.34)
    - card_expiration [string]: expiration of the card used for the purchase, in the format YYYY-MM. ex: "2032-12"
    - card_number [string]: number of the card used for the purchase.
    - card_security_code [string]: security code of the card used for the purchase.
    - holder_name [string]: card holder name. ex: "Tony Stark"
    - funding_type [string]: type of funding used for the purchase. ex: "credit", "debit"
    ## Parameters (optional):
    - holder_email [string, default None]: email associated with the card holder, required if the session's challenge_mode is "enabled" and optional otherwise.
    - holder_phone [string, default None]: phone number associated with the card holder, required if the session's challenge_mode is "enabled" and optional otherwise.
    - holder_id [string, default None]: additional card holder identification data.
    - installment_count [integer, default None]: number of installments the purchase is split into. ex: 1
    - billing_country_code [string, default None]: billing country code associated with the card used for the purchase, required if the session's challenge_mode is "enabled" and optional otherwise.
    - billing_city [string, default None]: billing city associated with the card used for the purchase, required if the session's challenge_mode is "enabled" and optional otherwise.
    - billing_state_code [string, default None]: billing state code associated with the card used for the purchase, required if the session's challenge_mode is "enabled" and optional otherwise.
    - billing_street_line_1 [string, default None]: billing street address associated with the card used for the purchase, required if the session's challenge_mode is "enabled" and optional otherwise.
    - billing_street_line_2 [string, default None]: billing street address complement associated with the card used for the purchase, required if the session's challenge_mode is "enabled" and optional otherwise.
    - billing_zip_code [string, default None]: billing zip code associated with the card used for the purchase, required if the session's challenge_mode is "enabled" and optional otherwise.
    - metadata [dictionary, default None]: additional data related to the purchase. If 3DS is enabled, the following fields related to the payer's device are required: userAgent, timezoneOffset, userIp, language.
    - soft_descriptor [string, default None]: text that will be shown in the holder's bank statement. ex: "my-store"
    - tags [list of strings, default None]: list of strings for tagging
    ## Attributes (return-only):
    - id [string]: unique id returned when a Purchase is created. ex: "5656565656565656"
    - card_ending [string]: last 4 digits of the card used. ex: "1234"
    - card_id [string]: unique id of the MerchantCard used for the purchase. ex: "5656565656565656"
    - challenge_mode [string]: whether 3DS holder verification was used. ex: "enabled", "disabled"
    - challenge_url [string]: URL to the 3DS challenge, when applicable.
    - created [datetime.datetime]: creation datetime for the Purchase. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - currency_code [string]: currency of the purchase. ex: "BRL"
    - end_to_end_id [string]: unique transaction id for the acquirer network.
    - fee [integer]: fee charged when the Purchase is processed. ex: 200 (= R$ 2.00)
    - network [string]: card network flag. ex: "visa", "mastercard"
    - source [string]: locator of the entity that generated the purchase. ex: "merchant-session/{sessionId}"
    - status [string]: current Purchase status. ex: "approved", "confirmed", "canceled", "voided"
    - updated [datetime.datetime]: latest update datetime for the Purchase. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, amount, card_expiration, card_number, card_security_code, holder_name, funding_type, id=None,
                 holder_email=None, holder_phone=None, holder_id=None, installment_count=None, billing_country_code=None,
                 billing_city=None, billing_state_code=None, billing_street_line_1=None, billing_street_line_2=None,
                 billing_zip_code=None, metadata=None, card_ending=None, card_id=None, challenge_mode=None,
                 challenge_url=None, created=None, currency_code=None, end_to_end_id=None, fee=None, network=None,
                 soft_descriptor=None, source=None, status=None, tags=None, updated=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.card_expiration = card_expiration
        self.card_number = card_number
        self.card_security_code = card_security_code
        self.holder_name = holder_name
        self.funding_type = funding_type
        self.holder_email = holder_email
        self.holder_phone = holder_phone
        self.holder_id = holder_id
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
        self.soft_descriptor = soft_descriptor
        self.source = source
        self.status = status
        self.tags = tags
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": Purchase, "name": "Purchase"}

