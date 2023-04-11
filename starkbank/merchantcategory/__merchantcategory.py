from starkcore.utils.subresource import SubResource
from starkbank.utils import rest


class MerchantCategory(SubResource):
    """# MerchantCategory object
    MerchantCategory's codes and types are used to define categories filters in CorporateRules.
    A MerchantCategory filter must define exactly one parameter between code and type.
    A type, such as "food", "services", etc., defines an entire group of merchant codes,
    whereas a code only specifies a specific MCC.
    ## Parameters (conditionally required):
    - code [string, default None]: category's code. ex: "veterinaryServices", "fastFoodRestaurants"
    - type [string, default None]: category's type. ex: "pets", "food"
    ## Attributes (return-only):
    - name [string]: category's name. ex: "Veterinary services", "Fast food restaurants"
    - number [string]: category's number. ex: "742", "5814"
    """

    def __init__(self, code=None, type=None, name=None, number=None):
        self.code = code
        self.type = type
        self.name = name
        self.number = number


_resource = {"class": MerchantCategory, "name": "MerchantCategory"}


def query(search=None, user=None):
    """# Retrieve MerchantCategories
    Receive a generator of MerchantCategory objects previously created in the Stark Bank API
    ## Parameters (optional):
    - search [string, default None]: keyword to search for code, type, name or number
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of MerchantCategory objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        search=search,
        user=user,
    )
