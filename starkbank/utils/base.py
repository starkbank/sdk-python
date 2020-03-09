from starkbank import request
from starkbank.utils.case import camel_to_snake, camel_to_kebab, snake_to_camel
from starkbank.utils.checks import check_user


class Base:
    _known_fields = set()
    _known_camel_fields = set()

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

    @classmethod
    def endpoint(cls):
        return "{entity}".format(
            entity=camel_to_kebab(cls.__name__),
        )

    @classmethod
    def id_endpoint(cls, id):
        return "{base_endpoint}/{id}".format(
            base_endpoint=cls.endpoint(),
            id=id
        )

    @classmethod
    def last_name(cls):
        route_name = camel_to_kebab(cls.__name__)
        return route_name.split("-")[-1]

    @classmethod
    def plural_last_name(cls):
        return "{name}s".format(name=cls.last_name())


class Post(Base):
    @classmethod
    def post_endpoint(cls):
        return cls.endpoint()

    @classmethod
    def _create(cls, entities, user=None):
        entity_list = [
            {
                snake_to_camel(k): v for k, v in entity.json().items() if v is not None
            } for entity in entities
        ]
        response = request.post(
            user=check_user(user),
            endpoint=cls.post_endpoint(),
            body={
                cls.plural_last_name(): entity_list
            }
        )
        return [
            cls.from_json(entity) for entity in response[cls.plural_last_name()]
        ]


class Get(Base):
    @classmethod
    def get_endpoint(cls):
        return cls.endpoint()

    @classmethod
    def _list(cls, limit=100, cursor=None, user=None):
        response = request.get(
            user=check_user(user),
            endpoint=cls.get_endpoint(),
            url_params={
                "limit": limit,
                "cursor": cursor,
            },
        )

        return [cls.from_json(entity) for entity in response[cls.plural_last_name()]], response["cursor"]


class GetId(Base):
    @classmethod
    def get_info_endpoint(cls, id):
        return cls.id_endpoint(id)

    @classmethod
    def _get(cls, id, user=None):
        response = request.get(
            user=check_user(user),
            endpoint=cls.get_info_endpoint(id),
        )
        return cls.from_json(response[cls.last_name()])


class GetPdf(Base):
    @classmethod
    def pdf_endpoint(cls, id):
        return "{info_endpoint}/pdf".format(
            info_endpoint=cls.id_endpoint(id),
        )

    @classmethod
    def get_pdf(cls, id, user=None):
        return request.get(
            user=check_user(user),
            endpoint=cls.pdf_endpoint(id),
        )


class BaseDelete(Base):
    @classmethod
    def delete_endpoint(cls, id):
        return cls.id_endpoint(id)

    @classmethod
    def delete(cls, ids, user=None):
        if len(ids) > 100:
            raise ValueError("ids cannot have more than 100 elements")

        entities = []
        for id in ids:
            response = request.delete(
                user=check_user(user),
                endpoint=cls.delete_endpoint(id),
            )

            entities.append(cls.from_json(response[cls.last_name()]))

        return entities
