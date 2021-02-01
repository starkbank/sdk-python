from starkbank.utils.subresource import SubResource


class Resource(SubResource):

    def __init__(self, id):
        id = str(id) if id else None
        self.id = id

    def __repr__(self):
        return "{classname}[{id}]".format(
            classname=self.__class__.__name__,
            id=self.id,
        )
