

class Base:

    def __init__(self, id):
        id = str(id)
        assert id.isdigit()
        self._id = id

    def __repr__(self):
        return self.__class__.__name__ + self.id

    def __str__(self):
        return "{classname}({fields})".format(
            classname=self.__class__.__name__,
            fields=", ".join("{key}={value}".format(key=key, value=value) for key, value in self.json().items())
        )

    def json(self, fields=None):
        json = {
            attribute: getattr(self, attribute)
            for attribute in dir(self)
            if not attribute.startswith('_') and not callable(getattr(self, attribute))
        }

        if fields:
            json = {k: v for k, v in json.items() if k in fields}

        return json

    @property
    def id(self):
        return self._id
