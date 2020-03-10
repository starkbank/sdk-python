from starkbank.utils.api import endpoint, id_endpoint, last_name, last_name_plural, api_json, from_api_json
from starkbank.utils import request


def get(resource, limit=100, cursor=None, user=None, **kwargs):
    url_params = {
        "limit": limit,
        "cursor": cursor,
    }
    url_params.update(kwargs)
    response = request.get(
        user=user,
        endpoint=endpoint(resource),
        url_params=url_params,
    )
    return [from_api_json(resource, entity) for entity in response[last_name_plural(resource)]], response["cursor"]


def query(resource, limit=None, user=None, **kwargs):
    cursor = ""
    while True:
        entity_list, cursor = get(
            resource=resource,
            limit=min(limit, 100) if limit else None,
            cursor=cursor,
            user=user,
            **kwargs
        )

        for entity in entity_list:
            yield entity

        if limit:
            limit -= 100
        if cursor is None or (limit is not None and limit <= 0):
            break


def get_id(resource, id, user=None):
    response = request.get(
        user=user,
        endpoint=id_endpoint(resource, id),
    )
    return from_api_json(resource, response[last_name(resource)])


def get_pdf(resource, id, user=None):
    return request.get(
        user=user,
        endpoint="{info_endpoint}/pdf".format(
            info_endpoint=id_endpoint(resource, id),
        ),
        json_response=False,
    )


def post(resource, entities, user=None):
    entity_list = [api_json(entity) for entity in entities]
    response = request.post(
        user=user,
        endpoint=endpoint(resource),
        body={
            last_name_plural(resource): entity_list
        }
    )
    return [
        from_api_json(resource, entity) for entity in response[last_name_plural(resource)]
    ]


def post_single(resource, entity, user=None):
    response = request.post(
        user=user,
        endpoint=endpoint(resource),
        body=api_json(entity),
    )
    return from_api_json(resource, response[last_name(resource)])


def delete(resource, ids, user=None):
    if len(ids) > 100:
        raise ValueError("ids cannot have more than 100 elements")
    entities = []
    for id in ids:
        response = request.delete(
            user=user,
            endpoint=id_endpoint(resource, id),
        )
        entities.append(from_api_json(resource, response[last_name(resource)]))
    return entities
