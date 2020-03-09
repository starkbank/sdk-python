from ..utils.base import Base, Get, Delete, GetId


class User(Get, GetId, Delete):
    credentials = None

    def __init__(self, id, credentials):
        self.credentials = credentials
        Base.__init__(self, id)
