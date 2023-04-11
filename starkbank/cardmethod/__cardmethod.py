from starkcore.utils.subresource import SubResource
from starkbank.utils import rest


class CardMethod(SubResource):
    """# CardMethod object
    CardMethod's codes are used to define methods filters in CorporateRules.
    ## Parameters (required):
    - code [string]: method's code. Options: "chip", "token", "server", "manual", "magstripe", "contactless"
    ## Attributes (return-only):
    - name [string]: method's name. ex: "token"
    - number [string]: method's number. ex: "81"
    """

    def __init__(self, code, name=None, number=None):
        self.code = code
        self.name = name
        self.number = number


_resource = {"class": CardMethod, "name": "CardMethod"}


def query(search=None, user=None):
    """# Retrieve CardMethods
    Receive a generator of CardMethod objects previously created in the Stark Bank API
    ## Parameters (optional):
    - search [string, default None]: keyword to search for code, name, number or short_code
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of CardMethod objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        search=search,
        user=user,
    )
