from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date, check_datetime_or_date
from ..utils import rest


class CorporateInvoice(Resource):
    """# CorporateInvoice object
    The CorporateInvoice objects created in your Workspace load your Corporate balance when paid.
    When you initialize a CorporateInvoice, the entity will not be automatically
    created in the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the created object.
    ## Parameters (required):
    - amount [integer]: CorporateInvoice value in cents. ex: 1234 (= R$ 12.34)
    ## Parameters (optional):
    - tags [list of strings, default []]: list of strings for tagging. ex: ["travel", "food"]
    ## Attributes (return-only):
    - id [string]: unique id returned when CorporateInvoice is created. ex: "5656565656565656"
    - name [string, default sub-issuer name]: payer name. ex: "Iron Bank S.A."
    - tax_id [string, default sub-issuer tax ID]: payer tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
    - brcode [string]: BR Code for the Invoice payment. ex: "00020101021226930014br.gov.bcb.pix2571brcode-h.development.starkbank.com/v2/d7f6546e194d4c64a153e8f79f1c41ac5204000053039865802BR5925Stark Bank S.A. - Institu6009Sao Paulo62070503***63042109"
    - due [datetime.datetime or datetime.date or string]: Invoice due and expiration date in UTC ISO format. ex: "2020-10-28T17:59:26.249976+00:00"
    - link [string]: public Invoice webpage URL. ex: "https://starkbank-card-issuer.development.starkbank.com/invoicelink/d7f6546e194d4c64a153e8f79f1c41ac"
    - status [string]: current CorporateInvoice status. ex: "created", "expired", "overdue", "paid"
    - corporate_transaction_id [string]: ledger transaction ids linked to this CorporateInvoice. ex: "corporate-invoice/5656565656565656"
    - updated [datetime.datetime]: latest update datetime for the CorporateInvoice. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - created [datetime.datetime]: creation datetime for the CorporateInvoice. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, amount, tax_id=None, name=None, tags=None, id=None, brcode=None, due=None, link=None, status=None, 
                corporate_transaction_id=None, updated=None, created=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.tax_id = tax_id
        self.name = name
        self.tags = tags
        self.brcode = brcode
        self.due = check_datetime_or_date(due)
        self.link = link
        self.status = status
        self.corporate_transaction_id = corporate_transaction_id
        self.updated = check_datetime(updated)
        self.created = check_datetime(created)


_resource = {"class": CorporateInvoice, "name": "CorporateInvoice"}


def create(invoice, user=None):
    """# Create CorporateInvoice
    Send a CorporateInvoice object for creation at the Stark Bank API
    ## Parameters (required):
    - invoice [CorporateInvoice object]: CorporateInvoice object to be created in the API.
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - CorporateInvoice object with updated attributes
    """
    return rest.post_single(resource=_resource, entity=invoice, user=user)


def query(limit=None, after=None, before=None, status=None, tags=None, user=None):
    """# Retrieve CorporateInvoices
    Receive a generator of CorporateInvoice objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["created", "expired", "overdue", "paid"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - generator of CorporateInvoice objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        status=status,
        after=check_date(after),
        before=check_date(before),
        tags=tags,
        limit=limit,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, status=None, tags=None, user=None):
    """# Retrieve CorporateInvoices
    Receive a list of up to 100 CorporateInvoice objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. Max = 100. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [list of strings, default None]: filter for status of retrieved objects. ex: ["created", "expired", "overdue", "paid"]
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - list of CorporateInvoice objects with updated attributes
    - cursor to retrieve the next page of CorporateInvoice objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        status=status,
        after=check_date(after),
        before=check_date(before),
        tags=tags,
        limit=limit,
        user=user,
    )
