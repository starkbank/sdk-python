from starkbank import request
from .base import Base
from ..checks import check_user


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
