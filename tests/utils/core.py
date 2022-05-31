import starkbank
from tests.utils.user import exampleProject


starkbank.user = exampleProject


def generateTestConfig(resource, schema, sample_builder=None):
    return {
        "resource": resource,
        "schema": schema,
        "sample_builder": sample_builder,
    }


class TestCore:

    @classmethod
    def get(cls, config):
        entity = config["resource"].get(user=exampleProject)
        print(entity)
        _assert_schema(entity=entity, schema=config["schema"])

    @classmethod
    def create(cls, config, n=5):
        samples = config["sample_builder"](n=n)
        entities = config["resource"].create(samples)
        for entity in entities:
            print(entity)
            _assert_schema(entity=entity, schema=config["schema"])


def _assert_schema(entity, schema):
    unknownFields = set(schema) - set(_to_dict(entity))
    if unknownFields:
        raise ValueError("Unknown fields detected in entity: {unknownFields}".format(unknownFields=unknownFields))

    for field, value in schema.items():
        if isinstance(value, dict):
            _assert_schema(entity=value, schema=schema)
            continue
        _assert_is_instance(getattr(entity, field), value)


def _to_dict(entity):
    return {
        a: getattr(entity, a) for a in dir(entity) if not a.startswith('_') and not callable(getattr(entity, a))
    }


def _assert_is_instance(value, type):
    if not isinstance(value, type):
        raise TypeError("value {value} is of type {valueType}, but should be {type}".format(
            value=value,
            valueType=type(value),
            type=type,
        ))
