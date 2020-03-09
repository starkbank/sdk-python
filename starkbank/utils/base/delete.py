from starkbank import request
from starkbank.utils.case import camel_to_snake, camel_to_kebab, snake_to_camel
from starkbank.utils.checks import check_user
from .base import Base
from ..case import snake_to_camel
from ..checks import check_user


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
