from starkbank.user.base import User, get_id as _user_get_id, query as _user_query
from starkbank.user.credentials import Credentials


class Project(User):

    def __init__(self, environment, private_key, id, name="", allowed_ips=None):
        self.name = name
        self.allowed_ips = allowed_ips

        User.__init__(
            self,
            id=id,
            environment=environment,
            credentials=Credentials(
                access_id="project/{id}".format(id=id),
                private_key_pem=private_key,
            ),
        )


Project._define_known_fields()


def get(id, user=None):
    return _user_get_id(resource=Project, id=id, user=user)


def query(limit=100, user=None):
    return _user_query(resource=Project, limit=limit, user=user)
