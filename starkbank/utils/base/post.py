from starkbank import request
from .base import Base
from ..case import snake_to_camel


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
            user=user,
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
            user=user,
            endpoint=cls._post_endpoint(),
            body={snake_to_camel(k): v for k, v in entity.json().items() if v is not None},
        )
        return cls.from_json(response[cls._last_name()])
