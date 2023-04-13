from ..utils import rest
from starkcore.utils.api import from_api_json
from starkcore.utils.checks import check_date
from starkcore.utils.resource import Resource
from .__taxpreview import _sub_resource as _tax_preview_sub_resource
from .__brcodepreview import _sub_resource as _brcode_preview_sub_resource
from .__boletopreview import _sub_resource as _boleto_preview_sub_resource
from .__utilitypreview import _sub_resource as _utility_preview_sub_resource


_sub_resource_by_type = {
    "brcode-payment": _brcode_preview_sub_resource,
    "boleto-payment": _boleto_preview_sub_resource,
    "utility-payment": _utility_preview_sub_resource,
    "tax-payment": _tax_preview_sub_resource,
}


class PaymentPreview(Resource):

    """# PaymentPreview object
    A PaymentPreview is used to get information from a payment code before confirming the payment.
    This resource can be used to preview BR Codes and bar codes of boleto, tax and utility payments
    ## Parameters (required):
    - id [string]: Main identification of the payment. This should be the BR Code for Pix payments and lines or bar codes for payment slips. ex: "34191.09008 63571.277308 71444.640008 5 81960000000062", "00020126580014br.gov.bcb.pix0136a629532e-7693-4846-852d-1bbff817b5a8520400005303986540510.005802BR5908T'Challa6009Sao Paulo62090505123456304B14A"
    ## Parameters (optional):
    - scheduled [datetime.date or string, default today]: intended payment date. Right now, this parameter only has effect on BrcodePreviews. ex: datetime.date(2020, 3, 10)
    ## Attributes (return-only):
    - type [string]: Payment type. ex: "brcode-payment", "boleto-payment", "utility-payment" or "tax-payment"
    - payment [BrcodePreview, BoletoPreview, UtilityPreview or TaxPreview]: Information preview of the informed payment.
    """

    def __init__(self, id, scheduled=None, type=None, payment=None):
        Resource.__init__(self, id=id)
        self.scheduled = check_date(scheduled)
        self.type = type
        self.payment = payment
        if type in _sub_resource_by_type:
            self.payment = from_api_json(resource=_sub_resource_by_type[type], json=payment)


_resource = {"class": PaymentPreview, "name": "PaymentPreview"}


def create(previews, user=None):
    """# Create PaymentPreviews
    Send a list of PaymentPreviews objects for processing in the Stark Bank API
    ## Parameters (required):
    - previews [list of PaymentPreviews objects]: list of PaymentPreviews objects to be created in the API
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of PaymentPreviews objects with updated attributes
    """
    return rest.post_multi(resource=_resource, entities=previews, user=user)
