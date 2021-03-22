from datetime import date, datetime, timedelta
from .resource import Resource
from .case import camel_to_kebab, snake_to_camel, camel_to_snake


def api_json(entity):
    if isinstance(entity, dict):
        return cast_json_to_api_format(entity)
    json = {
        attribute: getattr(entity, attribute)
        for attribute in dir(entity)
        if not attribute.startswith('_') and not callable(getattr(entity, attribute))
    }
    return cast_json_to_api_format(json)


def cast_json_to_api_format(json):
    return {snake_to_camel(k): cast_values(v) for k, v in json.items() if v is not None}


def cast_values(value):
    if type(value) == datetime:
        return value.strftime("%Y-%m-%dT%H:%M:%S+00:00")

    if isinstance(value, date):
        return value.strftime("%Y-%m-%d")

    if isinstance(value, timedelta):
        return int(value.total_seconds())

    if isinstance(value, Resource):
        return api_json(value)

    if not isinstance(value, list):
        return value

    casted_values = []
    for v in value:
        if isinstance(v, dict):
            casted_values.append(cast_json_to_api_format(v))
            continue
        casted_values.append(v)
    return casted_values


def from_api_json(resource, json):
    snakes = {camel_to_snake(k): v for k, v in json.items()}

    params = set(resource["class"].__init__.__code__.co_varnames) - {"self"}

    snakes = {k: v for k, v in snakes.items() if k in params}
    for param in params - set(snakes):
        snakes[param] = None

    return resource["class"](**snakes)


def endpoint(resource):
    return camel_to_kebab(resource["name"]).replace("-log", "/log").replace("-attempt", "/attempt")


def last_name(resource):
    return camel_to_kebab(resource["name"]).split("-")[-1]


def last_name_plural(resource):
    base = last_name(resource)
    if base.endswith("s"):
        return base
    if base.endswith("y") and not base.endswith("ey"):
        return "{name}ies".format(name=base[:-1])
    return "{name}s".format(name=base)
