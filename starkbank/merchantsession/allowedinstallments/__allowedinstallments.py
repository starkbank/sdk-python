from starkcore.utils.subresource import SubResource


class AllowedInstallments(SubResource):
    def __init__(self, total_amount, count):
        super().__init__()
        self.total_amount = total_amount
        self.count = count


_sub_resource = {"class": AllowedInstallments, "name": "AllowedInstallments"}

