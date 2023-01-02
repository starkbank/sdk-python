from starkcore.utils.subresource import SubResource


class Rule(SubResource):
    """# BrcodePayment.Rule object
    The BrcodePayment.Rule object modifies the behavior of BrcodePayment objects when passed as an argument upon their creation.
    ## Parameters (required):
    - key [string]: Rule to be customized, describes what BrcodePayment behavior will be altered. ex: "resendingLimit"
    - value [integer]: Value of the rule. ex: 5
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value


_sub_resource = {"class": Rule, "name": "Rule"}
