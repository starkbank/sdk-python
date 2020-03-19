from .case import snake_to_camel


def urlencode(params):
    params = {k: v for k, v in params.items() if v is not None} if params else {}
    params = {snake_to_camel(k): ",".join(v) if isinstance(v, (tuple, list, set)) else v for k, v in params.items()}
    return "&".join("{k}={v}".format(k=k, v=v) for k, v in params.items())