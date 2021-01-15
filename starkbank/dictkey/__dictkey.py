from starkbank.utils.checks import check_date
from ..utils import rest
from ..utils.checks import check_datetime
from ..utils.resource import Resource


class DictKey(Resource):

    """# DictKey object
    DictKey represents a PIX key registered in Bacen's DICT system.
    
    ## Parameters (optional):
    - id [string]: DictKey object unique id. ex: "tony@starkbank.com", "722.461.430-04", "20.018.183/0001-80", "+5511988887777", "b6295ee1-f054-47d1-9e90-ee57b74f60d9"
    
    ## Attributes (return-only):
    - type [string, default None]: DICT key type. ex: "email", "cpf", "cnpj", "phone" or "evp"
    - name [string, default None]: key owner full name. ex: "Tony Stark"
    - tax_id [string, default None]: key owner tax ID (CNPJ or masked CPF). ex: "***.345.678-**" or "20.018.183/0001-80"
    - owner_type [string, default None]: DICT key owner type. ex "naturalPerson" or "legalPerson"
    - ispb [string, default None]: bank ISPB associated with the DICT key. ex: "20018183"
    - branch_code [string, default None]: bank account branch code associated with the DICT key. ex: "9585"
    - account_number [string, default None]: bank account number associated with the DICT key. ex: "9828282578010513"
    - account_type [string, default None]: bank account type associated with the DICT key. ex: "checking", "saving" e "salary"
    - status [string, default None]: current DICT key status. ex: "created", "registered", "canceled" or "failed"
    - account_created [datetime.datetime, default None]: creation datetime of the bank account associated with the DICT key. ex: datetime.date(2020, 1, 12, 11, 14, 8)
    - owned [datetime.datetime, default None]: datetime since when the current owner holds this DICT key. ex: datetime.date(2020, 11, 16, 8, 12, 11)
    - created [datetime.datetime, default None]: creation datetime for the DICT key. ex: datetime.date(2020, 11, 16, 8, 12, 11)
    """
    
    def __init__(self, id=None, type=None, name=None, tax_id=None, owner_type=None, ispb=None, branch_code=None,
                 account_number=None, account_type=None, status=None, account_created=None, owned=None, created=None):
        Resource.__init__(self, id=id)

        self.id = id
        self.type = type
        self.name = name
        self.tax_id = tax_id
        self.owner_type = owner_type
        self.ispb = ispb
        self.branch_code = branch_code
        self.account_number = account_number
        self.account_type = account_type
        self.status = status
        self.account_created = check_datetime(account_created)
        self.owned = check_datetime(owned)
        self.created = check_datetime(created)


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
    - user [Project object, default None]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of DictKey objects with updated attributes
    """
    return rest.get_list(
        resource=_resource,
        limit=limit,
        type=type,
        after=check_date(after),
        before=check_date(before),
        ids=ids,
        status=status,
        user=user,
    )
