from starkbank.user.base import User
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

    @classmethod
    def _query(cls, limit=100, user=None):
        return super(Project, cls)._query(
            limit=limit,
            user=user,
        )


Project._define_known_fields()

get = Project._get_id
query = Project._query
