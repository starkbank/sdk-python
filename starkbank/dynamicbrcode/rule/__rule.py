from starkcore.utils.subresource import SubResource


class Rule(SubResource):

    def __init__(self, key, value):
        self.key = key
        self.value = value


_sub_resource = {"class": Rule, "name": "Rule"}
