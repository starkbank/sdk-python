from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_date
from starkcore.utils.checks import check_datetime


class DictKey(Resource):

    """# DictKey object
    DictKey represents a PIX key registered in Bacen's DICT system.
    ## Parameters (optional):
    - id [string]: DictKey object unique id. ex: "tony@starkbank.com", "722.461.430-04", "20.018.183/0001-80", "+5511988887777", "b6295ee1-f054-47d1-9e90-ee57b74f60d9"
    ## Attributes (return-only):
    - type [string]: DICT key type. ex: "email", "cpf", "cnpj", "phone" or "evp"
    - name [string]: key owner full name. ex: "Tony Stark"
    - tax_id [string]: key owner tax ID (CNPJ or masked CPF). ex: "***.345.678-**" or "20.018.183/0001-80"
    - owner_type [string]: DICT key owner type. ex "naturalPerson" or "legalPerson"
    - bank_name [string]: bank name associated with the DICT key. ex: "Stark Bank"
    - ispb [string]: bank ISPB associated with the DICT key. ex: "20018183"
    - branch_code [string]: encrypted bank account branch code associated with the DICT key. ex: "ZW5jcnlwdGVkLWJyYW5jaC1jb2Rl"
    - account_number [string]: encrypted bank account number associated with the DICT key. ex: "ZW5jcnlwdGVkLWFjY291bnQtbnVtYmVy"
    - account_type [string]: bank account type associated with the DICT key. ex: "checking", "savings", "salary" or "payment"
    - status [string]: current DICT key status. ex: "created", "registered", "canceled" or "failed"
    """
    
    def __init__(self, id=None, type=None, name=None, tax_id=None, owner_type=None, bank_name=None, 
                   ispb=None, branch_code=None, account_number=None, account_type=None, status=None):
        Resource.__init__(self, id=id)

        self.type = type
        self.name = name
        self.tax_id = tax_id
        self.owner_type = owner_type
        self.bank_name = bank_name
        self.ispb = ispb
        self.branch_code = branch_code
        self.account_number = account_number
        self.account_type = account_type
        self.status = status


_resource = {"class": DictKey, "name": "DictKey"}


def get(id, user=None):
    """# Retrieve a specific DictKey
    Receive a single DictKey object by its id
    ## Parameters (required):
    - id [string]: DictKey object unique id and PIX key itself. ex: "tony@starkbank.com", "722.461.430-04", "20.018.183/0001-80", "+5511988887777", "b6295ee1-f054-47d1-9e90-ee57b74f60d9"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - DictKey object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, type=None, after=None, before=None, ids=None, status=None, user=None):
    """# Retrieve DictKeys
    Receive a generator of DictKey objects associated with your Stark Bank Workspace
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - type [string, default None]: DictKey type. ex: "cpf", "cnpj", "phone", "email" or "evp"
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - status [string, default None]: filter for status of retrieved objects. ex: "success"
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of DictKey objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        type=type,
        after=check_date(after),
        before=check_date(before),
        ids=ids,
        status=status,
        user=user,
    )


def page(cursor=None, limit=None, type=None, after=None, before=None, ids=None, status=None, user=None):
    """# Retrieve paged DictKeys
    Receive a list of up to 100 DictKey objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - type [string, default None]: DictKey type. ex: "cpf", "cnpj", "phone", "email" or "evp"
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - status [string, default None]: filter for status of retrieved objects. ex: "success"
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of DictKey objects with updated attributes
    - cursor to retrieve the next page of DictKey objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        type=type,
        after=check_date(after),
        before=check_date(before),
        ids=ids,
        status=status,
        user=user,
    )
