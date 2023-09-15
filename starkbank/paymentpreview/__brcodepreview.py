from starkcore.utils.subresource import SubResource


class BrcodePreview(SubResource):

    """# BrcodePreview object
    A BrcodePreview is used to get information from a BR Code you received before confirming the payment.
    ## Attributes (return-only):
    - status [string]: Payment status. ex: "active", "paid", "canceled" or "unknown"
    - name [string]: Payment receiver name. ex: "Tony Stark"
    - tax_id [string]: Payment receiver tax ID. ex: "012.345.678-90"
    - bank_code [string]: Payment receiver bank code. ex: "20018183"
    - account_type [string]: Payment receiver account type. ex: "checking"
    - allow_change [bool]: If True, the payment is able to receive amounts that are different from the nominal one. ex: True or False
    - amount [integer]: Value in cents that this payment is expecting to receive. If 0, any value is accepted. ex: 123 (= R$1,23)
    - nominal_amount [integer]: Original value in cents that this payment was expecting to receive without the discounts, fines, etc.. If 0, any value is accepted. ex: 123 (= R$1,23)
    - interest_amount [integer]: Current interest value in cents that this payment is charging. If 0, any value is accepted. ex: 123 (= R$1,23)
    - fine_amount [integer]: Current fine value in cents that this payment is charging. ex: 123 (= R$1,23)
    - reduction_amount [integer]: Current value reduction value in cents that this payment is expecting. ex: 123 (= R$1,23)
    - discount_amount [integer]: Current discount value in cents that this payment is expecting. ex: 123 (= R$1,23)
    - reconciliation_id [string]: Reconciliation ID linked to this payment. ex: "txId", "payment-123"
    """

    def __init__(self, status, name, tax_id, bank_code, account_type, allow_change, amount, nominal_amount,
                 interest_amount, fine_amount, reduction_amount, discount_amount, reconciliation_id):
        self.status = status
        self.name = name
        self.tax_id = tax_id
        self.bank_code = bank_code
        self.account_type = account_type
        self.allow_change = allow_change
        self.amount = amount
        self.nominal_amount = nominal_amount
        self.interest_amount = interest_amount
        self.fine_amount = fine_amount
        self.reduction_amount = reduction_amount
        self.discount_amount = discount_amount
        self.reconciliation_id = reconciliation_id


_sub_resource = {"class": BrcodePreview, "name": "BrcodePreview"}
