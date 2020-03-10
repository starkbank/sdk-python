from starkbank.utils.case import camel_to_snake, camel_to_kebab, snake_to_camel


class Base:
    _known_fields = set()
    _json_fill = {}

    def __init__(self, id):
        id = str(id) if id else None
        assert id is None or id.isdigit()
        self.id = id

    def __repr__(self):
        return "{classname}[{id}]".format(
            classname=self.__class__.__name__,
            id=self.id,
        )

    def __str__(self):
        return "{classname}(\n\t{fields}\n)".format(
            classname=self.__class__.__name__,
            fields=",\n\t".join("{key}={value}".format(key=key, value=value) for key, value in self.json().items())
        )

    def json(self, fields=None, api=False):
        json = {
            attribute: getattr(self, attribute)
            for attribute in dir(self)
            if not attribute.startswith('_') and not callable(getattr(self, attribute))
        }
        if fields:
            json = {k: v for k, v in json.items() if k in fields}
        if api:
            json = {snake_to_camel(k): v for k, v in json.items() if v is not None}

        return json

    @classmethod
    def from_json(cls, json):
        for fill, value in cls._json_fill.items():
            json.setdefault(fill, value)

        snakes = {camel_to_snake(k): v for k, v in json.items()}

        return cls(**{
            k: v for k, v in snakes.items() if k in cls._known_fields
        })

    @classmethod
    def _define_known_fields(cls):
        cls._known_fields = set(cls.__init__.__code__.co_varnames) - {"self"}

    @classmethod
    def _last_name(cls):
        return camel_to_kebab(cls.__name__).split("-")[-1]

    @classmethod
    def _last_name_plural(cls):
        return "{name}s".format(name=cls._last_name())
