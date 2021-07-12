from ..utils import rest
from ..utils.resource import SubResource


class Institution(SubResource):
    """# Institution object
    A Institution is used to get information on the institutions that are recognized by the Brazilian Central Bank.
    Besides the display name and full name, they also include the STR code (used for TEDs) and the SPI Code
    (used for Pix) for the institutions. Either of these codes may be empty if the institution is not registered on
    that Central Bank service.
    ## Attributes:
    - display_name [string]: short version of the institution name that should be displayed to end users. ex: "Stark Bank"
    - name [string]: full version of the institution name. ex: "Stark Bank S.A."
    - spi_code [string]: SPI code used to identify the institution on Pix transactions. ex: "20018183"
    - str_code [string]: STR code used to identify the institution on TED transactions. ex: "123"
    """

    def __init__(self, display_name, name, spi_code, str_code):
        self.display_name = display_name
        self.name = name
        self.spi_code = spi_code
        self.str_code = str_code


_resource = {"class": Institution, "name": "Institution"}


def query(limit=None, search=None, spi_codes=None, str_codes=None, user=None):
    """# Retrieve Bacen Institutions
    Receive a list of Institution objects that are recognized by the Brazilian Central bank for Pix and TED transactions
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - search [string, default None]: part of the institution name to be searched. ex: "stark"
    - spi_codes [list of strings, default None]: list of SPI (Pix) codes to be searched. ex: ["20018183"]
    - str_codes [list of strings, default None]: list of STR (TED) codes to be searched. ex: ["260"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of Institution objects with updated attributes
    """
    return rest.get_page(resource=_resource, search=search, spi_codes=spi_codes, str_codes=str_codes, limit=limit, user=user)[0]
