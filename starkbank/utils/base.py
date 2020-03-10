

class Base:

    def __init__(self, id):
        id = str(id) if id else None
        self.id = id

    def __repr__(self):
        return "{classname}[{id}]".format(
            classname=self.__class__.__name__,
            id=self.id,
        )

    def __str__(self):
        dict_ = {
            attribute: getattr(self, attribute)
            for attribute in dir(self)
            if not attribute.startswith('_') and not callable(getattr(self, attribute))
        }
        return "{classname}(\n\t{fields}\n)".format(
            classname=self.__class__.__name__,
            fields=",\n\t".join("{key}={value}".format(key=key, value=value) for key, value in dict_.items())
        )
