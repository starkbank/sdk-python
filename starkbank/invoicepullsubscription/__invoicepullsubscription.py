from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_datetime_or_date, check_date


class InvoicePullSubscription(Resource):
    """# InvoicePullSubscription object
    When you initialize an InvoicePullSubscription, the entity will not be automatically
    sent to the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    ## Parameters (required):
    - start [datetime.date or string]: subscription start date. ex: "2022-04-01"
    - interval [string]: subscription installment interval. Options: "week", "month", "quarter", "semester", "year"
    - pull_mode [string]: subscription pull mode. Options: "manual", "automatic". Automatic mode will create the Invoice Pull Requests automatically
    - pull_retry_limit [integer]: subscription pull retry limit. Options: 0, 3
    - type [string]: subscription type. Options: "push", "qrcode", "qrcodeAndPayment", "paymentAndOrQrcode"
    ## Parameters (conditionally required):
    - amount [integer, default 0]: subscription amount in cents. Required if an amount_min_limit is not informed. Minimum = 1 (R$ 0.01). ex: 100 (= R$ 1.00)
    - amount_min_limit [integer, 0 None]: subscription minimum amount in cents. Required if an amount is not informed. Minimum = 1 (R$ 0.01). ex: 100 (= R$ 1.00)
    ## Parameters (optional):
    - display_description [string, default None]: Invoice description to be shown to the payer. ex: "Subscription payment"
    - due [datetime.timedelta or integer, default None]: subscription invoice due offset. Available only for type "push". ex: timedelta(days=7)
    - external_id [string, default None]: string that must be unique among all your InvoicePullSubscriptions. Duplicated external_ids will cause failures. ex: "my-external-id"
    - reference_code [string, default None]: reference code for reconciliation. ex: "REF123456"
    - end [datetime.date or string, default None]: subscription end date. ex: "2023-04-01"
    - data [dictionary, default None]: additional data for the subscription based on type
    - name [string, default None]: subscription debtor name. ex: "Iron Bank S.A."
    - tax_id [string, default None]: subscription debtor tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
    - tags [list of strings, default []]: list of strings for tagging
    ## Attributes (return-only):
    - id [string]: unique id returned when InvoicePullSubscription is created. ex: "5656565656565656"
    - status [string]: current InvoicePullSubscription status. ex: "active", "canceled"
    - bacen_id [string]: unique authentication id at the Central Bank. ex: "RR2001818320250616dtsPkBVaBYs"
    - brcode [string]: Brcode string for the InvoicePullSubscription. ex: "00020101021126580014br.gov.bcb.pix0114+5599999999990210starkbank.com.br520400005303986540410000000000005802BR5913Stark Bank S.A.6009SAO PAULO62070503***6304D2B1"
    - created [datetime.datetime]: creation datetime for the InvoicePullSubscription. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the InvoicePullSubscription. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, start, interval, pull_mode, pull_retry_limit, type, amount=None, amount_min_limit=None,
                 display_description=None, due=None, external_id=None, reference_code=None, end=None, data=None,
                 name=None, tax_id=None, tags=None, id=None, status=None, bacen_id=None, created=None, updated=None):
        Resource.__init__(self, id=id)

        self.start = check_datetime_or_date(start)
        self.interval = interval
        self.pull_mode = pull_mode
        self.pull_retry_limit = pull_retry_limit
        self.type = type
        self.amount = amount
        self.amount_min_limit = amount_min_limit
        self.display_description = display_description
        self.due = None if due == "" else check_datetime_or_date(due)
        self.external_id = external_id
        self.reference_code = reference_code
        self.end = None if end == "" else check_datetime_or_date(end)
        self.data = data
        self.name = name
        self.tax_id = tax_id
        self.tags = tags
        self.status = status
        self.bacen_id = bacen_id
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": InvoicePullSubscription, "name": "InvoicePullSubscription"}


def create(subscriptions, user=None):
    """# Create InvoicePullSubscriptions
    Send a list of InvoicePullSubscription objects for creation in the Stark Bank API
    ## Parameters (required):
    - subscriptions [list of InvoicePullSubscription objects]: list of InvoicePullSubscription objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of InvoicePullSubscription objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=subscriptions, user=user)


def get(id, user=None):
    """# Retrieve a specific InvoicePullSubscription
    Receive a single InvoicePullSubscription object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - InvoicePullSubscription object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, status=None, invoice_ids=None, external_ids=None, tags=None, 
          ids=None, after=None, before=None, user=None):
    """# Retrieve InvoicePullSubscriptions
    Receive a generator of InvoicePullSubscription objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["active", "canceled"]
    - invoice_ids [list of strings, default None]: list of Invoice ids linked to the subscriptions. ex: ["5656565656565656", "4545454545454545"]
    - external_ids [list of strings, default None]: list of external_ids to filter retrieved objects. ex: ["my-external-id-1", "my-external-id-2"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of InvoicePullSubscription objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        invoice_ids=invoice_ids,
        external_ids=external_ids,
        tags=tags,
        ids=ids,
        user=user,
    )


def page(cursor=None, limit=None, status=None, invoice_ids=None, external_ids=None,
         tags=None, ids=None, after=None, before=None, user=None):
    """# Retrieve paged InvoicePullSubscriptions
    Receive a list of up to 100 InvoicePullSubscription objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["active", "canceled"]
    - invoice_ids [list of strings, default None]: list of Invoice ids linked to the subscriptions. ex: ["5656565656565656", "4545454545454545"]
    - external_ids [list of strings, default None]: list of external_ids to filter retrieved objects. ex: ["my-external-id-1", "my-external-id-2"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of InvoicePullSubscription objects with updated attributes
    - cursor to retrieve the next page of InvoicePullSubscription objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        status=status,
        invoice_ids=invoice_ids,
        external_ids=external_ids,
        tags=tags,
        ids=ids,
        user=user,
    )


def cancel(id, user=None):
    """# Cancel an InvoicePullSubscription entity
    Cancel an InvoicePullSubscription entity previously created in the Stark Bank API
    ## Parameters (required):
    - id [string]: InvoicePullSubscription unique id. ex: '5656565656565656'
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - canceled InvoicePullSubscription object
    """
    return rest.delete_id(resource=_resource, id=id, user=user)
