from ... import request
from ...utils.checks import check_string, check_list_of_strings, check_private_key, check_user
from .project import Project


def create(private_key, name, allowed_ips=None, user=None):
    response, errors = request.post(
        user=check_user(user),
        endpoint="project",
        body={
            "name": check_string(name),
            "publicKey": check_private_key(private_key).publicKey().toPem(),
            "allowedIps": check_list_of_strings(allowed_ips),
        }
    )

    if errors:
        return None, errors

    project_info = response["project"]

    return Project(
        private_key=private_key,
        project_id=project_info["id"],
        name=project_info["name"],
        allowed_ips=project_info["allowed_ips"]
    ), []


def retrieve(user, project_id):
    response, errors = request.get(
        user=user,
        endpoint="project/{project_id}".format(project_id=project_id),
    )

    if errors:
        return None, errors

    project_info = response["project"]

    return Project(
        private_key=None,
        project_id=project_info["id"],
        name=project_info["name"],
        allowed_ips=project_info["allowedIps"]
    ), []


def list(limit=100, fields=None, cursor=None, user=None):
    url_params = {
        "limit": limit,
    }
    if fields:
        url_params["fields"] = check_list_of_strings(fields)
    if cursor:
        url_params["cursor"] = check_string(cursor)

    response, errors = request.get(
        user=check_user(user),
        endpoint="project",
        url_params=url_params,
    )

    if errors:
        return None, errors

    projects = response["projects"]

    return [Project(
        private_key=None,
        project_id=project_info["id"],
        name=project_info["name"],
        allowed_ips=project_info["allowedIps"]
    ) for project_info in projects], []


def delete(project_id, user=None):
    response, errors = request.delete(
        user=check_user(user),
        endpoint="project/{project_id}".format(project_id=project_id),
    )

    if errors:
        return None, errors

    project_info = response["project"]

    return Project(
        private_key=None,
        project_id=project_info["id"],
        name=project_info["name"],
        allowed_ips=project_info["allowedIps"]
    ), []
