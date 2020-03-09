from starkbank import request
from .base import Base
from ..checks import check_user


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
