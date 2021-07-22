from ..utils.subresource import SubResource


class TaxPreview(SubResource):

    """# TaxPreview object
    A TaxPreview is used to get information from a Tax Payment you received to check the information before the payment.
    ## Attributes (return-only):
    - amount [int]: amount final to be paid. ex: 23456 (= R$ 234.56)
    - name [string]: beneficiary full name. ex: "Light Company"
    - description [string]: utility payment description. ex: "Tax Payment - Light Company"
    - line [string]: Number sequence that identifies the payment. ex: "34191.09008 63571.277308 71444.640008 5 81960000000062"
    - bar_code [string]: Bar code number that identifies the payment. ex: "34195819600000000621090063571277307144464000"
    """

    def __init__(self, amount, name, description, line, bar_code):
        self.amount = amount
        self.name = name
        self.description = description
        self.line = line
        self.bar_code = bar_code


_sub_resource = {"class": TaxPreview, "name": "TaxPreview"}
