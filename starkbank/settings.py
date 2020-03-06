from starkbank.models.environment import Environment
from starkbank.models.logging import Logging
from starkbank.user.base import User


class Settings:
    _env = None
    _logging = Logging.none
    _default_user = None

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, env):
        assert env in Environment.values(), "env must be one from {}".format(Environment.values())
        self._env = env

    @property
    def logging(self):
        return self._logging

    @logging.setter
    def logging(self, logging):
        assert logging in Logging.values(), "logging must be one from {}".format(Logging.values())
        self._logging = logging

    @property
    def default_user(self):
        return self._default_user

    @default_user.setter
    def default_user(self, default_user):
        assert isinstance(default_user, User), "default_user must be an object retrieved from one of starkbank.user methods or classes"
        self._default_user = default_user


settings = Settings()
