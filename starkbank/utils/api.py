from starkbank.utils.case import camel_to_kebab, snake_to_camel, camel_to_snake


def define_compatibility_fields(resource, json_fill=None):
    json_fill = json_fill or {}
    resource._json_fill = json_fill
    resource._known_fields = set(resource.__init__.__code__.co_varnames) - {"self"}


def api_json(entity):
    json = {
        attribute: getattr(entity, attribute)
        for attribute in dir(entity)
        if not attribute.startswith('_') and not callable(getattr(entity, attribute))
    }
    json = {snake_to_camel(k): v for k, v in json.items() if v is not None}
    return json


def from_api_json(resource, json):
    for fill, value in resource._json_fill.items():
        json.setdefault(fill, value)

    snakes = {camel_to_snake(k): v for k, v in json.items()}

    return resource(**{
        k: v for k, v in snakes.items() if k in resource._known_fields
    })


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
