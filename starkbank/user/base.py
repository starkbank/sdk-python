from starkbank.utils.environment import Environment
from ..utils import rest
from ..utils.base import Base
from ..utils.checks import check_user


class User(Base):

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


def get_id(resource, id, user=None):
    environment = check_user(user).environment
    entity = rest.get_id(resource=resource, id=id, user=user)
    entity.environment = environment
    return entity


def query(resource, limit=100, user=None, **kwargs):
    environment = check_user(user).environment
    query = rest.query(resource=resource, limit=limit, user=user, **kwargs)
    for entity in query:
        entity.environment = environment
        yield entity
