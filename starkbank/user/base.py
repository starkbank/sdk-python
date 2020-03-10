from ..models.environment import Environment
from ..utils.base import Base, Get, GetId
from ..utils.checks import check_user


class User(Get, GetId):

    _json_fill = {
        "environment": "production",
        "privateKey": None,
    }
    credentials = None

    def __init__(self, id, environment, credentials):
        assert environment in Environment.values(), "environment {} is not in {}".format(environment, Environment.values())
        self.environment = environment
        self.credentials = credentials
        Base.__init__(self, id)

    @classmethod
    def _get(cls, limit=100, cursor=None, user=None, **kwargs):
        environment = check_user(user).environment
        entities, cursor = super(User, cls)._get(limit=limit, cursor=cursor, user=user, **kwargs)
        for entity in entities:
            entity.environment = environment
        return entities, cursor

    @classmethod
    def _get_id(cls, id, user=None):
        environment = check_user(user).environment
        entity = super(User, cls)._get_id(id=id, user=user)
        entity.environment = environment
        return entity
