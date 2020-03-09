from starkbank.utils.case import camel_to_snake, camel_to_kebab, snake_to_camel


class Base:
    _known_fields = set()
    _known_camel_fields = set()
    _json_fill = {}

    def __init__(self, id):
        id = str(id) if id else None
        assert id is None or id.isdigit()
        self._id = id

    def __repr__(self):
        return "{classname}[{id}]".format(
            classname=self.__class__.__name__,
            id=self.id,
        )

    def __str__(self):
        return "{classname}({fields})".format(
            classname=self.__class__.__name__,
            fields=", ".join("{key}={value}".format(key=key, value=value) for key, value in self.json().items())
        )

    @property
    def id(self):
        return self._id

    def json(self, fields=None):
        json = {
            attribute: getattr(self, attribute)
            for attribute in dir(self)
            if not attribute.startswith('_') and not callable(getattr(self, attribute))
        }

        if fields:
            json = {k: v for k, v in json.items() if k in fields}

        return json

    @classmethod
    def from_json(cls, json):
        for fill, value in cls._json_fill.items():
            json.setdefault(fill, value)
        return cls(**{
            camel_to_snake(k): v for k, v in json.items() if k in cls._known_camel_fields
        })

    @classmethod
    def _endpoint(cls):
        return "{entity}".format(
            entity=camel_to_kebab(cls.__name__),
        )

    @classmethod
    def _id_endpoint(cls, id):
        return "{base_endpoint}/{id}".format(
            base_endpoint=cls._endpoint(),
            id=id
        )

    @classmethod
    def _last_name(cls):
        route_name = camel_to_kebab(cls.__name__)
        return route_name.split("-")[-1]

    @classmethod
    def _plural_last_name(cls):
        return "{name}s".format(name=cls._last_name())

    @classmethod
    def _define_known_fields(cls):
        cls._known_fields = set(cls.__init__.__code__.co_varnames) - {"self"}
        cls._known_camel_fields = {snake_to_camel(field) for field in cls._known_fields}
