from starkbank.user.base import User, get_id as _user_get_id, query as _user_query


class Project(User):

    def __init__(self, environment, private_key, id, name="", allowed_ips=None):
        self.name = name
        self.allowed_ips = allowed_ips

        User.__init__(
            self,
            id=id,
            access_id="project/{id}".format(id=id),
            private_key_pem=private_key,
            environment=environment,
        )


def get(id, user=None):
    return _user_get_id(resource=Project, id=id, user=user)


def query(limit=None, user=None):
    return _user_query(resource=Project, limit=limit, user=user)
