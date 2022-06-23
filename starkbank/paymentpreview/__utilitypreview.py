from starkcore.utils.subresource import SubResource


class UtilityPreview(SubResource):

    """# UtilityPreview object
    A UtilityPreview is used to get information from a Utility Payment you received before confirming the payment.
    ## Attributes (return-only):
    - amount [int]: final amount to be paid. ex: 23456 (= R$ 234.56)
    - name [string]: beneficiary full name. ex: "Light Company"
    - description [string]: utility payment description. ex: "Utility Payment - Light Company"
    - line [string]: Number sequence that identifies the payment. ex: "82660000002 8 44361143007 7 41190025511 7 00010601813 8"
    - bar_code [string]: Bar code number that identifies the payment. ex: "82660000002443611430074119002551100010601813"
    """

    def __init__(self, amount, name, description, line, bar_code):
        self.amount = amount
        self.name = name
        self.description = description
        self.line = line
        self.bar_code = bar_code


_sub_resource = {"class": UtilityPreview, "name": "UtilityPreview"}
