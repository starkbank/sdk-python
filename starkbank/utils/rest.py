from requests import get, post, delete, patch
from ..utils.api import endpoint, last_name, last_name_plural, api_json, from_api_json, cast_json_to_api_format
from ..utils.request import fetch


def get_page(resource, user=None, **kwargs):
    json = fetch(method=get, path=endpoint(resource), query=kwargs, user=user).json()
    entities = [from_api_json(resource, entity) for entity in json[last_name_plural(resource)]]
    cursor = json.get("cursor")
    return entities, cursor


def get_stream(resource, limit=None, user=None, **kwargs):
    query = {"limit": min(limit, 100) if limit else limit}
    query.update(kwargs)

    while True:
        entities, cursor = get_page(resource=resource, user=user, **query)
        for entity in entities:
            yield entity

        if limit:
            limit -= 100
            query["limit"] = min(limit, 100)

        query["cursor"] = cursor
        if not cursor or (limit is not None and limit <= 0):
            break


def get_id(resource, id, user=None):
    json = fetch(method=get, path="{endpoint}/{id}".format(endpoint=endpoint(resource), id=id), user=user).json()
    entity = json[last_name(resource)]
    return from_api_json(resource, entity)


def get_content(resource, id, sub_resource_name, user=None, **kwargs):
    path = "{endpoint}/{id}/{sub_resource_name}".format(endpoint=endpoint(resource), id=id, sub_resource_name=sub_resource_name)
    return fetch(method=get, path=path, query=kwargs, user=user).content


def get_sub_resource(resource, id, sub_resource, user=None, **kwargs):
    path = "{endpoint}/{id}/{sub_resource}".format(endpoint=endpoint(resource), id=id, sub_resource=endpoint(sub_resource))
    entity = fetch(method=get, path=path, query=kwargs, user=user).json()[last_name(sub_resource)]
    return from_api_json(sub_resource, entity)


def get_sub_resources(resource, id, sub_resource, user=None, **kwargs):
    path = "{endpoint}/{id}/{sub_resource}".format(endpoint=endpoint(resource), id=id, sub_resource=endpoint(sub_resource))
    entities = fetch(method=get, path=path, query=kwargs, user=user).json()[last_name_plural(sub_resource)]
    return [from_api_json(sub_resource, entity) for entity in entities]


def post_multi(resource, entities, user=None):
    json = fetch(method=post, path=endpoint(resource), user=user, payload={
        last_name_plural(resource): [api_json(entity) for entity in entities]
    }).json()
    entities = json[last_name_plural(resource)]
    return [from_api_json(resource, entity) for entity in entities]


def post_single(resource, entity, user=None):
    payload = api_json(entity)
    json = fetch(method=post, path=endpoint(resource), user=user, payload=payload).json()
    entity_json = json[last_name(resource)]
    return from_api_json(resource, entity_json)


def delete_id(resource, id, user=None):
    json = fetch(method=delete, path="{endpoint}/{id}".format(endpoint=endpoint(resource), id=id), user=user).json()
    entity = json[last_name(resource)]
    return from_api_json(resource, entity)


def patch_id(resource, id, user=None, **payload):
    payload = cast_json_to_api_format(payload)
    json = fetch(method=patch, path="{endpoint}/{id}".format(endpoint=endpoint(resource), id=id), payload=payload, user=user).json()
    entity = json[last_name(resource)]
    return from_api_json(resource, entity)
