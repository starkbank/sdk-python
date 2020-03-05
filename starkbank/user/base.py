from ..utils.base import Base


class User(Base):
    credentials = None

    def __init__(self, id, credentials):
        self.credentials = credentials
        Base.__init__(self, id)
