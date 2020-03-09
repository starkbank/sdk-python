from starkbank.models.environment import Environment
from starkbank.user.base import User


class Settings:
    _environment = None
    _debug = False
    _user = None

    @property
    def environment(self):
        return self._environment

    @environment.setter
    def environment(self, env):
        assert env in Environment.values(), "env must be one from {}".format(Environment.values())
        self._environment = env

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, debug):
        self._debug = debug

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        assert isinstance(user, User), "user must be an object retrieved from one of starkbank.user methods or classes"
        self._user = user


settings = Settings()
