from .api import cast_json_to_api_format


def urlencode(params):
    params = cast_json_to_api_format(params) if params else {}
    params = {k: ",".join([str(value) for value in v]) if isinstance(v, (tuple, list, set)) else v for k, v in params.items()}
    return "?" + "&".join("{k}={v}".format(k=k, v=v) for k, v in params.items()) if params else ""
