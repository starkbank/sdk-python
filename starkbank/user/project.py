from starkbank import request
from starkbank.user.base import User
from starkbank.user.credentials import Credentials
from starkbank.utils.checks import check_string, check_list_of_strings, check_user, check_private_key


class Project(User):
    def __init__(self, private_key, id, name="", allowed_ips=None):
        self.name = check_string(name)
        self.allowed_ips = check_list_of_strings(allowed_ips)

        User.__init__(
            self,
            id=id,
            credentials=Credentials(
                access_id="project/{id}".format(id=id),
                private_key_pem=private_key,
            ),
        )


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
        id=project_info["id"],
        name=project_info["name"],
        allowed_ips=project_info["allowed_ips"]
    ), []


def retrieve(user, id):
    response, errors = request.get(
        user=user,
        endpoint="project/{id}".format(id=id),
    )

    if errors:
        return None, errors

    project_info = response["project"]

    return Project(
        private_key=None,
        id=project_info["id"],
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
        id=project_info["id"],
        name=project_info["name"],
        allowed_ips=project_info["allowedIps"]
    ) for project_info in projects], []


def delete(id, user=None):
    response, errors = request.delete(
        user=check_user(user),
        endpoint="project/{id}".format(id=id),
    )

    if errors:
        return None, errors

    project_info = response["project"]

    return Project(
        private_key=None,
        id=project_info["id"],
        name=project_info["name"],
        allowed_ips=project_info["allowedIps"]
    ), []
