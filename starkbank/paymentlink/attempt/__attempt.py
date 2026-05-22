from ...utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date


class Attempt(Resource):
    """# PaymentLink.Attempt object
    Each payment attempt against a PaymentLink generates a PaymentLink.Attempt
    record. It carries information about the payment method used, the resulting
    payment and the lifecycle status of the attempt.
    ## Attributes (return-only):
    - id [string]: unique id that identifies the payment attempt. ex: "5656565656565656"
    - payment_link_id [string]: ID of the PaymentLink that originated the attempt. ex: "5764309015642112"
    - method [string]: payment method used in the attempt. ex: "credit", "debit"
    - payment [string]: reference to the underlying payment created from this attempt. ex: "merchant-session/6543210987654321"
    - amount [integer]: amount charged in this attempt in cents. ex: 15000 (= R$ 150.00)
    - status [string]: current attempt status. ex: "created", "success", "failed" or "expired"
    - created [datetime.datetime]: datetime representing the moment when the attempt was created. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the attempt. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, id, payment_link_id, method, payment, amount, status, created, updated):
        Resource.__init__(self, id=id)

        self.payment_link_id = payment_link_id
        self.method = method
        self.payment = payment
        self.amount = amount
        self.status = status
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": Attempt, "name": "PaymentLinkAttempt"}


def get(id, user=None):
    """# Retrieve a specific paymentlink.Attempt
    Receive a single paymentlink.Attempt object previously created by the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - paymentlink.Attempt object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, status=None, payment_link_ids=None, ids=None, user=None):
    """# Retrieve paymentlink.Attempts
    Receive a generator of paymentlink.Attempt objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "success" or "failed"
    - payment_link_ids [list of strings, default None]: list of PaymentLink ids to filter attempts. ex: ["5656565656565656", "4545454545454545"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of paymentlink.Attempt objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        payment_link_ids=payment_link_ids,
        ids=ids,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, status=None, payment_link_ids=None, ids=None, user=None):
    """# Retrieve paged paymentlink.Attempts
    Receive a list of up to 100 paymentlink.Attempt objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None]: date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "success" or "failed"
    - payment_link_ids [list of strings, default None]: list of PaymentLink ids to filter attempts. ex: ["5656565656565656", "4545454545454545"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of paymentlink.Attempt objects with updated attributes
    - cursor to retrieve the next page of paymentlink.Attempt objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        payment_link_ids=payment_link_ids,
        ids=ids,
        user=user,
    )
