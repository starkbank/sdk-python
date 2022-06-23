from starkcore.utils.subresource import SubResource


class TaxPreview(SubResource):

    """# TaxPreview object
    A TaxPreview is used to get information from a Tax Payment you received before confirming the payment.
    ## Attributes (return-only):
    - amount [int]: final amount to be paid. ex: 23456 (= R$ 234.56)
    - name [string]: beneficiary full name. ex: "Iron Throne"
    - description [string]: tax payment description. ex: "ISS Payment - Iron Throne"
    - line [string]: Number sequence that identifies the payment. ex: "85660000006 6 67940064007 5 41190025511 7 00010601813 8"
    - bar_code [string]: Bar code number that identifies the payment. ex: "85660000006679400640074119002551100010601813"
    """

    def __init__(self, amount, name, description, line, bar_code):
        self.amount = amount
        self.name = name
        self.description = description
        self.line = line
        self.bar_code = bar_code


_sub_resource = {"class": TaxPreview, "name": "TaxPreview"}
