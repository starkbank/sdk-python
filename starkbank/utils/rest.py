from requests import get, post, delete, patch
from ..utils.api import endpoint, last_name, last_name_plural, api_json, from_api_json, cast_json_to_api_format
from ..utils.request import fetch


def get_list(resource, limit=None, user=None, **kwargs):
    query = {"limit": min(limit, 100) if limit else limit}
    query.update(kwargs)

    while True:
        json = fetch(method=get, path=endpoint(resource), query=query, user=user).json()
        entities = json[last_name_plural(resource)]

        for entity in entities:
            yield from_api_json(resource, entity)

        if limit:
            limit -= 100
            query["limit"] = min(limit, 100)

        cursor = json.get("cursor")
        query["cursor"] = cursor
        if not cursor or (limit is not None and limit <= 0):
            break


def get_id(resource, id, user=None):
    json = fetch(method=get, path="{endpoint}/{id}".format(endpoint=endpoint(resource), id=id), user=user).json()
    entity = json[last_name(resource)]
    return from_api_json(resource, entity)


def get_pdf(resource, id, user=None, **kwargs):
    return fetch(method=get, path="{endpoint}/{id}/pdf".format(endpoint=endpoint(resource), id=id), query=kwargs, user=user).content


def get_qrcode(resource, id, user=None, **kwargs):
    return fetch(method=get, path="{endpoint}/{id}/qrcode".format(endpoint=endpoint(resource), id=id), query=kwargs, user=user).content


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
