from starkbank.utils import request
from starkbank.utils.case import camel_to_kebab


def get(resource, limit=100, cursor=None, user=None, **kwargs):
    url_params = {
        "limit": limit,
        "cursor": cursor,
    }
    url_params.update(kwargs)
    response = request.get(
        user=user,
        endpoint=_endpoint(resource),
        url_params=url_params,
    )
    return [resource.from_json(entity) for entity in response[_last_name_plural(resource)]], response["cursor"]


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
        endpoint=_id_endpoint(resource, id),
    )
    return resource.from_json(response[_last_name(resource)])


def get_pdf(resource, id, user=None):
    return request.get(
        user=user,
        endpoint="{info_endpoint}/pdf".format(
            info_endpoint=_id_endpoint(resource, id),
        ),
        json_response=False,
    )


def post(resource, entities, user=None):
    entity_list = [entity.json(api=True) for entity in entities]
    response = request.post(
        user=user,
        endpoint=_endpoint(resource),
        body={
            _last_name_plural(resource): entity_list
        }
    )
    return [
        resource.from_json(entity) for entity in response[_last_name_plural(resource)]
    ]


def post_single(resource, entity, user=None):
    response = request.post(
        user=user,
        endpoint=_endpoint(resource),
        body=entity.json(api=True),
    )
    return resource.from_json(response[_last_name(resource)])


def delete(resource, ids, user=None):
    if len(ids) > 100:
        raise ValueError("ids cannot have more than 100 elements")
    entities = []
    for id in ids:
        response = request.delete(
            user=user,
            endpoint=_id_endpoint(resource, id),
        )
        entities.append(resource.from_json(response[_last_name(resource)]))
    return entities


def _endpoint(resource):
    endpoint = camel_to_kebab(resource.__name__)
    split = endpoint.split("-")
    if split[-1] == "log":
        endpoint = "-".join(split[:-1]) + "/log"
    print(endpoint)
    return endpoint


def _id_endpoint(resource, id):
    return "{base_endpoint}/{id}".format(
        base_endpoint=_endpoint(resource),
        id=id
    )


def _last_name(resource):
    return camel_to_kebab(resource.__name__).split("-")[-1]


def _last_name_plural(resource):
    return "{name}s".format(name=_last_name(resource))
