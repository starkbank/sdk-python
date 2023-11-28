from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.api import from_api_json
from starkcore.utils.checks import check_date, check_datetime, check_timedelta, check_datetime_or_date
from .__payment import _sub_resource as _payment_sub_resource
from .rule.__rule import Rule
from .rule.__rule import _sub_resource as _rule_resource
from ..split.__split import _resource as _split_resource, Split


class Invoice(Resource):
    """# Invoice object
    When you initialize an Invoice, the entity will not be automatically
    sent to the Stark Bank API. The 'create' function sends the objects
    to the Stark Bank API and returns the list of created objects.
    To create scheduled Invoices, which will display the discount, interest, etc. on the final users banking interface,
    use dates instead of datetimes on the "due" and "discounts" fields.
    ## Parameters (required):
    - amount [integer]: Invoice value in cents. Minimum = 0 (any value will be accepted). ex: 1234 (= R$ 12.34)
    - tax_id [string]: payer tax ID (CPF or CNPJ) with or without formatting. ex: "01234567890" or "20.018.183/0001-80"
    - name [string]: payer name. ex: "Iron Bank S.A."
    ## Parameters (optional):
    - due [datetime.datetime or datetime.date or string, default now + 2 days]: Invoice due date in UTC ISO format. ex: "2020-10-28T17:59:26.249976+00:00" for immediate invoices and "2020-10-28" for scheduled invoices
    - expiration [integer or datetime.timedelta, default 5097600 (59 days)]: time interval in seconds between due date and expiration date. ex 123456789
    - fine [float, default 2.0]: Invoice fine for overdue payment in %. ex: 2.5
    - interest [float, default 1.0]: Invoice monthly interest for overdue payment in %. ex: 5.2
    - discounts [list of dictionaries, default []]: list of dictionaries with "percentage":float and "due":datetime.datetime or string pairs
    - rules [list of Invoice.Rules, default []]: list of Invoice.Rule objects for modifying invoice behavior. ex: [Invoice.Rule(key="allowedTaxIds", value=[ "012.345.678-90", "45.059.493/0001-73" ])]
    - splits [list of Split.Splits, default []]: list of Split.Splits objects to indicate payment receivers. ex: [Invoice.Split(amount=141, receiverId="5706627130851328")]
    - tags [list of strings, default []]: list of strings for tagging
    - descriptions [list of dictionaries, default []]: list of dictionaries with "key":string and (optional) "value":string pairs
    ## Attributes (return-only):
    - pdf [string]: public Invoice PDF URL. ex: "https://invoice.starkbank.com/pdf/d454fa4e524441c1b0c1a729457ed9d8"
    - link [string]: public Invoice webpage URL. ex: "https://my-workspace.sandbox.starkbank.com/invoicelink/d454fa4e524441c1b0c1a729457ed9d8"
    - nominal_amount [integer]: Invoice emission value in cents (will change if invoice is updated, but not if it's paid). ex: 400000
    - fine_amount [integer]: Invoice fine value calculated over nominal_amount. ex: 20000
    - interest_amount [integer]: Invoice interest value calculated over nominal_amount. ex: 10000
    - discount_amount [integer]: Invoice discount value calculated over nominal_amount. ex: 3000
    - id [string]: unique id returned when Invoice is created. ex: "5656565656565656"
    - brcode [string]: BR Code for the Invoice payment. ex: "00020101021226800014br.gov.bcb.pix2558invoice.starkbank.com/f5333103-3279-4db2-8389-5efe335ba93d5204000053039865802BR5913Arya Stark6009Sao Paulo6220051656565656565656566304A9A0"
    - status [string]: current Invoice status. ex: "registered" or "paid"
    - fee [integer]: fee charged by this Invoice. ex: 200 (= R$ 2.00)
    - transaction_ids [list of strings]: ledger transaction ids linked to this Invoice (if there are more than one, all but the first are reversals or failed reversal chargebacks). ex: ["19827356981273"]
    - created [datetime.datetime]: creation datetime for the Invoice. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    - updated [datetime.datetime]: latest update datetime for the Invoice. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, amount, tax_id, name, due=None, expiration=None, fine=None, interest=None, discounts=None,
                 rules=None, tags=None, descriptions=None, pdf=None, link=None, nominal_amount=None, fine_amount=None,
                 interest_amount=None, discount_amount=None, id=None, brcode=None, status=None, fee=None, splits=None,
                 transaction_ids=None, created=None, updated=None):
        Resource.__init__(self, id=id)

        self.amount = amount
        self.nominal_amount = nominal_amount
        self.fine_amount = fine_amount
        self.interest_amount = interest_amount
        self.discount_amount = discount_amount
        self.due = check_datetime_or_date(due)
        self.tax_id = tax_id
        self.name = name
        self.expiration = check_timedelta(expiration)
        self.fine = fine
        self.interest = interest
        self.discounts = discounts
        self.rules = _parse_rules(rules)
        self.splits = _parse_splits(splits)
        self.tags = tags
        self.pdf = pdf
        self.link = link
        self.descriptions = descriptions
        self.brcode = brcode
        self.status = status
        self.fee = fee
        self.transaction_ids = transaction_ids
        self.created = check_datetime(created)
        self.updated = check_datetime(updated)


_resource = {"class": Invoice, "name": "Invoice"}


def _parse_rules(rules):
    if rules is None:
        return None
    parsed_rules = []
    for rule in rules:
        if isinstance(rule, Rule):
            parsed_rules.append(rule)
            continue
        parsed_rules.append(from_api_json(_rule_resource, rule))
    return parsed_rules


def _parse_splits(splits):
    if splits is None:
        return None
    parsed_splits = []
    for split in splits:
        if isinstance(split, Split):
            parsed_splits.append(split)
            continue
        parsed_splits.append(from_api_json(_split_resource, split))
    return parsed_splits


def create(invoices, user=None):
    """# Create Invoices
    Send a list of Invoice objects for creation in the Stark Bank API
    ## Parameters (required):
    - invoices [list of Invoice objects]: list of Invoice objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of Invoice objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=invoices, user=user)


def get(id, user=None):
    """# Retrieve a specific Invoice
    Receive a single Invoice object previously created in the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Invoice object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, status=None, tags=None, ids=None, after=None, before=None, user=None):
    """# Retrieve Invoices
    Receive a generator of Invoice objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "paid" or "registered"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of Invoice objects with updated attributes
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
    )


def page(cursor=None, limit=None, status=None, tags=None, ids=None, after=None, before=None, user=None):
    """# Retrieve paged Invoices
    Receive a list of up to 100 Invoice objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - status [string, default None]: filter for status of retrieved objects. ex: "paid" or "registered"
    - tags [list of strings, default None]: tags to filter retrieved objects. ex: ["tony", "stark"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of Invoice objects with updated attributes
    - cursor to retrieve the next page of Invoice objects
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
    )


def update(id, status=None, amount=None, due=None, expiration=None, user=None):
    """# Update Invoice entity
    Update an Invoice by passing id, if it hasn't been paid yet.
    ## Parameters (required):
    - id [string]: Invoice id. ex: '5656565656565656'
    ## Parameters (optional):
    - status [string]: You may cancel the invoice by passing 'canceled' in the status
    - amount [string]: Nominal amount charged by the invoice. ex: 100 (R$1.00)
    - due [datetime.datetime or string, default now + 2 days]: Invoice due date in UTC ISO format. ex: "2020-10-28T17:59:26.249976+00:00"
    - expiration [integer or datetime.timedelta, default None]: time interval in seconds between the due date and the expiration date. ex 123456789
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - target Invoice with updated attributes
    """
    payload = {
        "status": status,
        "amount": amount,
        "due": check_datetime(due),
        "expiration": check_timedelta(expiration),
    }
    return rest.patch_id(resource=_resource, id=id, user=user, payload=payload)


def qrcode(id, size=7, user=None):
    """# Retrieve a specific Invoice QR Code png
    Receive a single Invoice QR Code in png format generated in the Stark Bank API by the invoice ID.
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - size [integer, default 7]: number of pixels in each "box" of the QR code. Minimum = 1, maximum = 50. ex: 12
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Invoice png blob
    """
    return rest.get_content(resource=_resource, id=id, size=size, user=user, sub_resource_name="qrcode")


def pdf(id, user=None):
    """# Retrieve a specific Invoice pdf file
    Receive a single Invoice pdf receipt file generated in the Stark Bank API by its id.
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Invoice pdf file
    """
    return rest.get_content(resource=_resource, id=id, user=user, sub_resource_name="pdf")


def payment(id, user=None):
    """# Retrieve a specific Invoice payment information
    Receive the Invoice.Payment sub-resource associated with a paid Invoice.
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Invoice.Payment sub-resource
    """
    return rest.get_sub_resource(resource=_resource, id=id, user=user, sub_resource=_payment_sub_resource)
