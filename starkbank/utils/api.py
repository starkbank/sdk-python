from starkbank.utils.case import camel_to_kebab, snake_to_camel, camel_to_snake


def api_json(entity):
    json = {
        attribute: getattr(entity, attribute)
        for attribute in dir(entity)
        if not attribute.startswith('_') and not callable(getattr(entity, attribute))
    }
    json = {snake_to_camel(k): v for k, v in json.items() if v is not None}
    return json


def from_api_json(resource, json):
    snakes = {camel_to_snake(k): v for k, v in json.items()}

    params = set(resource.__init__.__code__.co_varnames) - {"self"}

    snakes = {k: v for k, v in snakes.items() if k in params}
    for param in params - set(snakes):
        snakes[param] = None

    return resource(**snakes)


def endpoint(resource):
    endpoint_ = camel_to_kebab(resource.__name__)
    split = endpoint_.split("-")
    if split[-1] == "log":
        endpoint_ = "-".join(split[:-1]) + "/log"
    return endpoint_


def id_endpoint(resource, id):
    return "{base_endpoint}/{id}".format(
        base_endpoint=endpoint(resource),
        id=id
    )


def last_name(resource):
    return camel_to_kebab(resource.__name__).split("-")[-1]


def last_name_plural(resource):
    return "{name}s".format(name=last_name(resource))
