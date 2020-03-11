from .credentials import Credentials
from ..utils import rest
from ..utils.base import Base
from ..utils.checks import check_user


class User(Base):

    def __init__(self, id, access_id, private_key_pem, environment):
        Base.__init__(self, id)

        if private_key_pem is None:
            self.credentials = None
        else:
            self.credentials = Credentials(
                access_id=access_id,
                private_key_pem=private_key_pem,
                environment=environment,
            )


def get_id(resource, id, user=None):
    environment = check_user(user).credentials.environment
    entity = rest.get_id(resource=resource, id=id, user=user)
    entity.environment = environment
    return entity


def query(resource, limit=100, user=None, **kwargs):
    environment = check_user(user).credentials.environment
    query = rest.query(resource=resource, limit=limit, user=user, **kwargs)
    for entity in query:
        entity.environment = environment
        yield entity
