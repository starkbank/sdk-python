import starkbank
from starkcore.utils.host import StarkHost


_api_version = "v2"


def set_relay(func):
    def wrapper(*args, **kwargs):
        kwargs.update({
            "sdk_version": starkbank.version,
            "host": StarkHost.bank,
            "api_version": kwargs.get("version") or _api_version,
            "user": kwargs.get("user") or starkbank.user,
            "language": kwargs.get("language") or starkbank.language,
            "timeout": kwargs.get("timeout") or starkbank.timeout,
        })
        return func(*args, **kwargs)
    return wrapper
