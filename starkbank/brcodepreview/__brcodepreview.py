from ..utils import rest
from ..utils.resource import Resource


class BrcodePreview(Resource):

    """# BrcodePreview object
    A BrcodePreview is used to get information from a BR Code you received to check the informations before paying it.
    ## Attributes (return-only):
    - status [string]: Payment status. ex: "active", "paid", "canceled" or "unknown"
    - name [string]: Payment receiver name. ex: "Tony Stark"
    - tax_id [string]: Payment receiver tax ID. ex: "012.345.678-90"
    - bank_code [string]: Payment receiver bank code. ex: "20018183"
    - branch_code [string]: Payment receiver branch code. ex: "0001"
    - account_number [string]: Payment receiver account number. ex: "1234567"
    - account_type [string]: Payment receiver account type. ex: "checking"
    - allow_change [bool]: If True, the payment is able to receive amounts that are different from the nominal one. ex: True or False
    - amount [integer]: Value in cents that this payment is expecting to receive. If 0, any value is accepted. ex: 123 (= R$1,23)
    - reconciliation_id [string]: Reconciliation ID linked to this payment. ex: "txId", "payment-123"
    """

    def __init__(self, status, name, tax_id, bank_code, branch_code, account_number, account_type, allow_change, amount, reconciliation_id):
        self.status = status
        self.name = name
        self.tax_id = tax_id
        self.bank_code = bank_code
        self.branch_code = branch_code
        self.account_number = account_number
        self.account_type = account_type
        self.allow_change = allow_change
        self.amount = amount
        self.reconciliation_id = reconciliation_id


_resource = {"class": BrcodePreview, "name": "BrcodePreview"}


def query(brcodes, user=None):
    """# Retrieve BrcodePreviews
    Receive a generator of BrcodePreview objects previously created in the Stark Bank API
    ## Parameters (optional):
    - brcodes [list of strings]: List of brcodes to preview. ex: ["00020126580014br.gov.bcb.pix0136a629532e-7693-4846-852d-1bbff817b5a8520400005303986540510.005802BR5908T'Challa6009Sao Paulo62090505123456304B14A"]
    - user [Project object, default None]: Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of BrcodePreview objects with updated attributes
    """
    return rest.get_list(
        resource=_resource,
        brcodes=brcodes,
        limit=None,
        user=user,
    )
