from starkbank.utils.case import camel_to_snake


class Base:
    _known_fields = set()
    _known_camel_fields = set()

    def __init__(self, id):
        id = str(id) if id else None
        assert id is None or id.isdigit()
        self._id = id

    def __repr__(self):
        return "{classname}[id]".format(
            classname=self.__class__.__name__,
            id=self.id,
        )

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

    @classmethod
    def from_json(cls, json):
        return cls(**{
            camel_to_snake(k): v for k, v in json.items() if k in cls._known_camel_fields
        })
