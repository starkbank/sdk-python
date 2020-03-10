from starkbank import request
from .base import Base


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
                user=user,
                endpoint=cls._delete_endpoint(id),
            )

            entities.append(cls.from_json(response[cls._last_name()]))

        return entities
