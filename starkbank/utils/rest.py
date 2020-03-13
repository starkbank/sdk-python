from ..utils.api import endpoint, last_name, last_name_plural, api_json, from_api_json
from ..utils.request import fetch, GET, POST, DELETE


def get_list(resource, cursor=None, limit=100, user=None, **kwargs):
    while True:
        query = {"limit": limit, "cursor": cursor}
        query.update(kwargs)

        json = fetch(path="/{endpoint}".format(endpoint=endpoint(resource)), method=GET, query=query, user=user).json()
        entities = json[last_name_plural(resource)]

        for entity in entities:
            yield from_api_json(resource, entity)

        if limit:
            limit -= 100

        cursor = json["cursor"]
        if cursor is None or (limit is not None and limit <= 0):
            break


def get_id(resource, id, user=None):
    json = fetch(path="/{endpoint}/{id}".format(endpoint=endpoint(resource), id=id), method=GET, user=user).json()
    entity = json[last_name(resource)]
    return from_api_json(resource, entity)


def get_pdf(resource, id, user=None):
    return fetch(path="/{endpoint}/{id}/pdf".format(endpoint=endpoint(resource), id=id), method=GET, user=user).content


def post(resource, entities, user=None):
    json = fetch(path="/{endpoint}".format(endpoint=endpoint(resource)), method=POST, user=user, payload={
        last_name_plural(resource): [api_json(entity) for entity in entities]
    }).json()
    entities = json[last_name_plural(resource)]
    return [from_api_json(resource, entity) for entity in entities]


def post_single(resource, entity, user=None):
    payload = api_json(entity)
    json = fetch(path="/{endpoint}".format(endpoint=endpoint(resource)), method=POST, user=user, payload=payload).json()
    entity_json = json[last_name(resource)]
    return from_api_json(resource, entity_json)


def delete_list(resource, ids, user=None):
    if len(ids) > 100:
        raise ValueError("ids cannot have more than 100 elements")
    entities = []
    for id in ids:
        entity = delete_id(resource, id, user)
        entities.append(entity)
    return entities


def delete_id(resource, id, user=None):
    json = fetch(path="/{endpoint}/{id}".format(endpoint=endpoint(resource), id=id), method=DELETE, user=user).json()
    entity = json[last_name(resource)]
    return from_api_json(resource, entity)


def get_public_key(service_id, user=None):
    return fetch(path="/public-key",  method=GET, query={"service_id": service_id}, user=user).json()["publicKey"]
