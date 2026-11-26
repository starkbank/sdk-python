from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.api import endpoint, from_api_json
from starkcore.utils.checks import check_date, check_datetime
from .position.__position import _sub_resource as _position_sub_resource


class FixedInvestment(Resource):
    """# FixedInvestment object
    A FixedInvestment applies your account balance in a digital fixed income product indexed to the CDI.
    When you initialize a FixedInvestment, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    Investments can only be created on business days, from 10 AM to 4 PM, Brasília time (GMT-3),
    and the minimum amount to be invested is 100000 (= R$ 1,000.00).
    ## Parameters (required):
    - amount [integer]: amount available in the investment in cents. It changes with the yield, the taxes and every withdrawal. ex: 101360 (= R$ 1,013.60)
    - type [string]: investment type. Options: "deposit" (uses the account balance)
    ## Parameters (optional):
    - due [datetime.datetime or string, default None]: due datetime of the investment. If not informed, it is set by Stark Bank. ex: datetime.datetime(2027, 11, 13, 9, 30, 0, 0)
    - tags [list of strings, default []]: list of strings for reference when searching for investments. ex: ["reserve", "monthly"]
    ## Attributes (return-only):
    - id [string]: unique id returned when the FixedInvestment is created. ex: "5656565656565656"
    - nominal_amount [integer]: amount originally invested in cents. It does not change after withdrawals. ex: 100000 (= R$ 1,000.00)
    - yield_amount [integer]: gross yield of the investment in cents. ex: 1754 (= R$ 17.54)
    - tax [integer]: total amount of taxes in cents, the sum of the amounts in taxes. ex: 394 (= R$ 3.94)
    - taxes [list of dictionaries]: list of taxes with type and amount. ex: [{"type": "ir", "amount": 394}]
    - interest [float]: percentage of the index paid by the investment. ex: 100 (= 100% of the CDI)
    - interest_type [string]: index the investment yields over. ex: "cdi"
    - status [string]: current FixedInvestment status. ex: "processing", "active", "failed" or "voided"
    - transactions [list of dictionaries]: ledger transactions linked to the investment. The first one is the deposit into the investment, and each following one is a withdrawal. ex: [{"id": "5656565656565656"}]
    - created [datetime.datetime]: creation datetime for the FixedInvestment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the FixedInvestment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, amount, type, due=None, tags=None, id=None, nominal_amount=None, yield_amount=None, tax=None,
                 taxes=None, interest=None, interest_type=None, status=None, transactions=None, created=None,
                 updated=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.type = type
        self.due = check_datetime(due)
        self.tags = tags
        self.nominal_amount = nominal_amount
        self.yield_amount = yield_amount
        self.tax = tax
        self.taxes = taxes
        self.interest = interest
        self.interest_type = interest_type
        self.status = status
        self.transactions = transactions
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": FixedInvestment, "name": "FixedInvestment"}


def create(investments, user=None):
    """# Create FixedInvestments
    Send a list of FixedInvestment objects for creation in the Stark Bank API
    ## Parameters (required):
    - investments [list of FixedInvestment objects]: list of FixedInvestment objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of FixedInvestment objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=investments, user=user)


def patch(investments, user=None):
    """# Withdraw from FixedInvestments
    Withdraw from one or more FixedInvestments by setting the amount that remains in each of them.
    The difference is withdrawn. The investment stays active while the withdrawal is processed,
    and a full withdrawal makes it voided.
    ## Parameters (required):
    - investments [list of dictionaries]: list of withdrawals, each with the investment "id" and the "amount" in cents that remains in it. Send 0 to withdraw everything. For a partial withdrawal, at least 100000 (= R$ 1,000.00) must remain. ex: [{"id": "5656565656565656", "amount": 500000}]
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of FixedInvestment objects with updated attributes
    """
    return rest.patch_multi(resource=_resource, entities=investments, user=user)


def get(id, user=None):
    """# Retrieve a specific FixedInvestment
    Receive a single FixedInvestment object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - FixedInvestment object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, status=None, sort=None, user=None):
    """# Retrieve FixedInvestments
    Receive a generator of FixedInvestment objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["active", "voided"]
    - sort [string, default "-created"]: sort order considered in response. Valid options are "created" or "-created".
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of FixedInvestment objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        sort=sort,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, status=None, sort=None, user=None):
    """# Retrieve paged FixedInvestments
    Receive a list of up to 100 FixedInvestment objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None]: date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["active", "voided"]
    - sort [string, default "-created"]: sort order considered in response. Valid options are "created" or "-created".
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of FixedInvestment objects with updated attributes
    - cursor to retrieve the next page of FixedInvestment objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        sort=sort,
        user=user,
    )

def position(after, before, user=None):
    """# Retrieve the FixedInvestment position
    Receive the consolidated position of your FixedInvestments between two dates
    ## Parameters (required):
    - after [datetime.date or string]: start date of the position. ex: datetime.date(2026, 11, 26)
    - before [datetime.date or string]: end date of the position. ex: datetime.date(2027, 11, 26)
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - fixedinvestment.Position object with the consolidated amounts of the period
    """
    json = rest.get_raw(
        path=endpoint(_resource) + "/position",
        query={"after": check_date(after), "before": check_date(before)},
        user=user,
    ).json()
    return from_api_json(_position_sub_resource, json["response"])
