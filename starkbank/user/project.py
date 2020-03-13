from .user import User


class Project(User):

    def __init__(self, id, environment, private_key, name="", allowed_ips=None):
        self.name = name
        self.allowed_ips = allowed_ips

        User.__init__(self,
            id=id,
            private_key=private_key,
            environment=environment,
            kind="project"
        )
