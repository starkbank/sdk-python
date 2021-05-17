from starkbank.utils import rest
from starkbank.utils.checks import check_datetime, check_date
from starkbank.utils.resource import Resource


class DarfPayment(Resource):
    """# DarfPayment object
    When you initialize a DarfPayment, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    ## Parameters (required):
    - description [string]: Text to be displayed in your statement (min. 10 characters). ex: "payment ABC"
    - revenue_code [string]: 4-digit tax code assigned by Federal Revenue. ex: "5948"
    - tax_id [tax_id]: tax id (formatted or unformatted) of the payer. ex: "12.345.678/0001-95"
    - competence [datetime.date or string]: competence month of the service. ex: datetime.date(2021, 4, 30)
    - nominal_amount [int]: amount due in cents without fee or interest. ex: 23456 (= R$ 234.56)
    - fine_amount [int]: fixed amount due in cents for fines. ex: 234 (= R$ 2.34)
    - interest_amount [int]: amount due in cents for interest. ex: 456 (= R$ 4.56)
    - due [datetime.date or string]: due date for payment. ex: datetime.date(2021, 5, 17)
    ## Parameters (optional):
    - reference_number [string]: number assigned to the region of the tax. ex: "08.1.17.00-4"
    - scheduled [datetime.date or string, default today]: payment scheduled date. ex: datetime.date(2021, 5, 10)
    - tags [list of strings]: list of strings for tagging
    ## Attributes (return-only):
    - id [string, default None]: unique id returned when payment is created. ex: "5656565656565656"
    - status [string, default None]: current payment status. ex: "success" or "failed"
    - amount [int, default None]: Total amount due calculated from other amounts. ex: 24146 (= R$ 241.46)
    - fee [integer, default None]: fee charged when the DarfPayment is processed. ex: 0 (= R$ 0.00)
    - updated [datetime.datetime, default None]: creation datetime for the payment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime, default None]: creation datetime for the payment. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """
    def __init__(self, description, revenue_code, tax_id, competence, nominal_amount, fine_amount, interest_amount,
                 due, reference_number=None, scheduled=None, tags=None, id=None, status=None, amount=None, fee=None,
                 updated=None, created=None):
        Resource.__init__(self, id=id)

        self.revenue_code = revenue_code
        self.tax_id = tax_id
        self.competence = check_date(competence)
        self.reference_number = reference_number
        self.fine_amount = fine_amount
        self.interest_amount = interest_amount
        self.due = check_date(due)
        self.description = description
        self.tags = tags
        self.scheduled = check_date(scheduled)
        self.status = status
        self.amount = amount
        self.nominal_amount = nominal_amount
        self.fee = fee
        self.updated = check_datetime(updated)
        self.created = check_datetime(created)


_resource = {"class": DarfPayment, "name": "DarfPayment"}


def create(payments, user=None):
    """# Create DarfPayments
    Send a list of DarfPayment objects for creation in the Stark Bank API
    ## Parameters (required):
    - payments [list of DarfPayment objects]: list of DarfPayment objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of DarfPayment objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=payments, user=user)


def get(id, user=None):
    """# Retrieve a specific DarfPayment
    Receive a single DarfPayment object previously created by the Stark Bank API by passing its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - DarfPayment object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def pdf(id, user=None):
    """# Retrieve a specific DarfPayment pdf file
    Receive a single DarfPayment pdf file generated in the Stark Bank API by passing its id.
    Only valid for darf payments with "success" status.
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - DarfPayment pdf file
    """
    return rest.get_content(resource=_resource, id=id, user=user, sub_resource_name="pdf")


def query(limit=None, after=None, before=None, tags=None, ids=None, status=None, user=None):
    """# Retrieve DarfPayments
    Receive a generator of DarfPayment objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - status [string, default None]: filter for status of retrieved objects. ex: "success"
    - user [Project object, default None]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of DarfPayment objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        tags=tags,
        ids=ids,
        status=status,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, tags=None, ids=None, status=None, user=None):
    """# Retrieve paged DarfPayments
    Receive a list of up to 100 DarfPayment objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - status [string, default None]: filter for status of retrieved objects. ex: "success"
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of DarfPayment objects with updated attributes
    - cursor to retrieve the next page of DarfPayment objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        tags=tags,
        ids=ids,
        status=status,
        user=user,
    )


def delete(id, user=None):
    """# Delete a DarfPayment entity
    Delete a DarfPayment entity previously created in the Stark Bank API
    ## Parameters (required):
    - id [string]: DarfPayment unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - deleted DarfPayment with updated attributes
    """
    return rest.delete_id(resource=_resource, id=id, user=user)
