from datetime import date, datetime
from .case import camel_to_kebab, snake_to_camel, camel_to_snake


def api_json(entity):
    json = {
        attribute: getattr(entity, attribute)
        for attribute in dir(entity)
        if not attribute.startswith('_') and not callable(getattr(entity, attribute))
    }
    return cast_json_to_api_format(json)


def cast_json_to_api_format(json):
    return {snake_to_camel(k): _date_to_string(v) for k, v in json.items() if v is not None}


def _date_to_string(data):
    return data.strftime("%Y-%m-%d") if isinstance(data, (date, datetime)) else data


def from_api_json(resource, json):
    snakes = {camel_to_snake(k): v for k, v in json.items()}

    params = set(resource.__init__.__code__.co_varnames) - {"self"}

    snakes = {k: v for k, v in snakes.items() if k in params}
    for param in params - set(snakes):
        snakes[param] = None

    return resource(**snakes)


def endpoint(resource):
    return camel_to_kebab(resource.__name__).replace("-log", "/log")


def last_name(resource):
    return camel_to_kebab(resource.__name__).split("-")[-1]


def last_name_plural(resource):
    return "{name}s".format(name=last_name(resource))
