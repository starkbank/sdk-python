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


class Post(Base):
    @classmethod
    def _post_endpoint(cls):
        return cls._endpoint()

    @classmethod
    def _post(cls, entities, user=None):
        entity_list = [
            {
                snake_to_camel(k): v for k, v in entity.json().items() if v is not None
            } for entity in entities
        ]
        response = request.post(
            user=check_user(user),
            endpoint=cls._post_endpoint(),
            body={
                cls._plural_last_name(): entity_list
            }
        )
        return [
            cls.from_json(entity) for entity in response[cls._plural_last_name()]
        ]

    @classmethod
    def _post_single(cls, entity, user=None):
        response = request.post(
            user=check_user(user),
            endpoint=cls._post_endpoint(),
            body={snake_to_camel(k): v for k, v in entity.json().items() if v is not None},
        )
        return cls.from_json(response[cls._last_name()])


class Get(Base):
    @classmethod
    def _get_endpoint(cls):
        return cls._endpoint()

    @classmethod
    def _get(cls, limit=100, cursor=None, user=None, **kwargs):
        url_params = {
            "limit": limit,
            "cursor": cursor,
        }
        url_params.update(kwargs)

        response = request.get(
            user=check_user(user),
            endpoint=cls._get_endpoint(),
            url_params=url_params,
        )

        return [cls.from_json(entity) for entity in response[cls._plural_last_name()]], response["cursor"]


class GetId(Base):
    @classmethod
    def _get_id_endpoint(cls, id):
        return cls._id_endpoint(id)

    @classmethod
    def _get_id(cls, id, user=None):
        response = request.get(
            user=check_user(user),
            endpoint=cls._get_id_endpoint(id),
        )
        return cls.from_json(response[cls._last_name()])


class GetPdf(Base):
    @classmethod
    def _pdf_endpoint(cls, id):
        return "{info_endpoint}/pdf".format(
            info_endpoint=cls._id_endpoint(id),
        )

    @classmethod
    def _get_pdf(cls, id, user=None):
        return request.get(
            user=check_user(user),
            endpoint=cls._pdf_endpoint(id),
        )


class Delete(Base):
    @classmethod
    def _delete_endpoint(cls, id):
        return cls._id_endpoint(id)

    @classmethod
    def _delete(cls, ids, user=None):
        if len(ids) > 100:
            raise ValueError("ids cannot have more than 100 elements")

        entities = []
        for id in ids:
            response = request.delete(
                user=check_user(user),
                endpoint=cls._delete_endpoint(id),
            )

            entities.append(cls.from_json(response[cls._last_name()]))

        return entities
