from starkcore.utils.subresource import SubResource


class Rule(SubResource):
     """# DynamicBrcode.Rule object
    The DynamicBrcode.Rule object modifies the behavior of DynamicBrcode objects when passed as an argument upon their creation.
    ## Parameters (required):
    - key [string]: Rule to be customized, describes what DynamicBrcode behavior will be altered. ex: "allowedTaxIds"
    - value [list of string]: Value of the rule. ex: ["012.345.678-90", "45.059.493/0001-73"]
    """
    
    def __init__(self, key, value):
        self.key = key
        self.value = value


_sub_resource = {"class": Rule, "name": "Rule"}
