from ..utils import rest


def get(path, query=None, user=None):
    """# Retrieve any StarkBank resource
    Receive a json of resources previously created in the Stark Bank API
    ## Parameters (required):
    - path [string]: StarkBank resource's route. ex: "/invoice/"
    - query [dict, default None]: Query parameters. ex: {"limit": 1, "status": paid}
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of Invoice objects with updated attributes
    """
    return rest.get_raw(
        path=path,
        query=query,
        user=user
    )


def post(path, body=None, user=None):
    return rest.post_raw(
        path=path,
        payload=body,
        user=user
    )


def patch(path, body=None, user=None):
    return rest.patch_raw(
        path=path,
        payload=body,
        user=user
    )


def put(path, body=None, user=None):
    return rest.put_raw(
        path=path,
        payload=body,
        user=user
    )


def delete(path, body=None, user=None):
    return rest.delete_raw(
        path=path,
        payload=body,
        user=user
    )