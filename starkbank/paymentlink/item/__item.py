from starkcore.utils.subresource import SubResource


class Item(SubResource):
    """# PaymentLink.Item object
    Represents a single item displayed on a PaymentLink purchase summary.
    ## Parameters (required):
    - code [string]: merchant code for the item. ex: "PREM-001"
    - description [string]: human-readable description of the item. ex: "Plano Premium Mensal"
    - quantity [integer]: quantity purchased of this item. ex: 1
    - unit_price [integer]: price per unit in cents. ex: 15000 (= R$ 150.00)
    - total_price [integer]: total price in cents for this item (quantity * unit_price minus discount). ex: 15000 (= R$ 150.00)
    ## Parameters (optional):
    - discount [integer, default None]: discount applied to the item in cents. ex: 0
    """

    def __init__(self, code, description, quantity, unit_price, total_price, discount=None):
        super().__init__()
        self.code = code
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = total_price
        self.discount = discount


_sub_resource = {"class": Item, "name": "Item"}
