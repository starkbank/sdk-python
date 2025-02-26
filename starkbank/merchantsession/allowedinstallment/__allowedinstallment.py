from starkcore.utils.subresource import SubResource


class AllowedInstallment(SubResource):
    def __init__(self, total_amount, count):
        super().__init__()
        self.total_amount = total_amount
        self.count = count


_sub_resource = {"class": AllowedInstallment, "name": "AllowedInstallment"}

