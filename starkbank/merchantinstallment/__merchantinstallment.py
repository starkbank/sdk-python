from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_date, check_datetime, check_datetime_or_date


class MerchantInstallment(Resource):
    """# MerchantInstallment object
    Represents one installment of a MerchantPurchase, generated automatically by the Stark Bank API when the purchase is split.
    ## Attributes (return-only):
    - id [string]: unique id returned when MerchantInstallment is created. ex: "5656565656565656"
    - amount [integer]: MerchantInstallment value in cents. ex: 1234 (= R$ 12.34)
    - due [datetime.date or datetime.datetime]: MerchantInstallment due date. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - fee [integer]: fee charged when the MerchantInstallment is processed. ex: 200 (= R$ 2.00)
    - funding_type [string]: installment funding type. ex: "credit"
    - network [string]: card network flag. ex: "visa", "mastercard"
    - purchase_id [string]: unique id of the MerchantPurchase to which this installment belongs. ex: "5656565656565656"
    - status [string]: current MerchantInstallment status. ex: "created", "success", "failed"
    - tags [list of strings]: list of strings for tagging
    - transaction_ids [list of strings]: ledger transaction ids linked to this MerchantInstallment
    - created [datetime.datetime]: creation datetime for the MerchantInstallment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the MerchantInstallment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, id=None, amount=None, created=None, due=None, fee=None, funding_type=None, network=None,
                 purchase_id=None, status=None, tags=None, transaction_ids=None, updated=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.due = check_datetime_or_date(due)
        self.fee = fee
        self.funding_type = funding_type
        self.network = network
        self.purchase_id = purchase_id
        self.status = status
        self.tags = tags
        self.transaction_ids = transaction_ids
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": MerchantInstallment, "name": "MerchantInstallment"}


def get(id, user=None):
    """# Retrieve a specific MerchantInstallment
    Receive a single MerchantInstallment object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - MerchantInstallment object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, status=None, tags=None, ids=None, user=None, purchase_ids=None):
    """# Retrieve MerchantInstallments
    Receive a generator of MerchantInstallment objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "success"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - purchase_ids [list of strings, default None]: list of MerchantPurchase ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of MerchantInstallment objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        tags=tags,
        ids=ids,
        user=user,
        purchase_ids=purchase_ids,
    )


def page(cursor=None, limit=None, after=None, before=None, status=None, tags=None, ids=None, user=None, purchase_ids=None):
    """# Retrieve paged MerchantInstallments
    Receive a list of up to 100 MerchantInstallment objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None]: date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "success"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - purchase_ids [list of strings, default None]: list of MerchantPurchase ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of MerchantInstallment objects with updated attributes
    - cursor to retrieve the next page of MerchantInstallment objects
    """
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
        purchase_ids=purchase_ids,
    )

