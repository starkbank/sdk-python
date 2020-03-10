from starkbank.utils import request


def get(resource, limit=100, cursor=None, user=None, **kwargs):
    url_params = {
        "limit": limit,
        "cursor": cursor,
    }
    url_params.update(kwargs)
    response = request.get(
        user=user,
        endpoint=resource._endpoint(),
        url_params=url_params,
    )
    return [resource.from_json(entity) for entity in response[resource._last_name_plural()]], response["cursor"]


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
        endpoint=resource._id_endpoint(id),
    )
    return resource.from_json(response[resource._last_name()])


def get_pdf(resource, id, user=None):
    return request.get(
        user=user,
        endpoint="{info_endpoint}/pdf".format(
            info_endpoint=resource._id_endpoint(id),
        ),
        json_response=False,
    )


def post(resource, entities, user=None):
    entity_list = [entity.json(api=True) for entity in entities]
    response = request.post(
        user=user,
        endpoint=resource._endpoint(),
        body={
            resource._last_name_plural(): entity_list
        }
    )
    return [
        resource.from_json(entity) for entity in response[resource._last_name_plural()]
    ]


def post_single(resource, entity, user=None):
    response = request.post(
        user=user,
        endpoint=resource._endpoint(),
        body=entity.json(api=True),
    )
    return resource.from_json(response[resource._last_name()])


def delete(resource, ids, user=None):
    if len(ids) > 100:
        raise ValueError("ids cannot have more than 100 elements")
    entities = []
    for id in ids:
        response = request.delete(
            user=user,
            endpoint=resource._id_endpoint(id),
        )
        entities.append(resource.from_json(response[resource._last_name()]))
    return entities
