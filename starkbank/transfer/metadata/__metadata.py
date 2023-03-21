from starkcore.utils.subresource import SubResource


class Metadata(SubResource):
    """# Transfer.Metadata object
    The Transfer.Metadata object contains additional information about the Transfer object.
    ## Parameters (required):
    - authentication [string]: Central Bank's unique ID for Pix transactions (EndToEndID). ex: "E200181832023031715008Scr7tD63TS"
    """

    def __init__(self, authentication):
        self.authentication = authentication


_sub_resource = {"class": Metadata, "name": "Metadata"}
