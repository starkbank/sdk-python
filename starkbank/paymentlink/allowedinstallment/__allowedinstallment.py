from starkcore.utils.subresource import SubResource


class AllowedInstallment(SubResource):
    """# PaymentLink.AllowedInstallment object
    Represents an installment option accepted by a PaymentLink, declaring
    the number of installments and the total amount charged to the payer
    for that option.
    ## Parameters (required):
    - count [integer]: number of installments. ex: 3
    - total_amount [integer]: total amount in cents charged to the payer for this installment count. ex: 16500 (= R$ 165.00)
    """

    def __init__(self, count, total_amount):
        super().__init__()
        self.count = count
        self.total_amount = total_amount


_sub_resource = {"class": AllowedInstallment, "name": "AllowedInstallment"}
