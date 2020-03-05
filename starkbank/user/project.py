from starkbank.user.base import User
from starkbank.user.credentials import Credentials
from starkbank import request
from starkbank.utils.checks import check_id, check_string, check_list_of_strings, check_user, check_private_key


class Project(User):
    def __init__(self, private_key, project_id, name="", allowed_ips=None):
        self.project_id = check_id(project_id)
        self.name = check_string(name)
        self.allowed_ips = check_list_of_strings(allowed_ips)

        User.__init__(
            self,
            Credentials(
                access_id="project/{project_id}".format(project_id=project_id),
                private_key_pem=private_key,
            )
        )

    def __str__(self):
        return "Project(project_id={project_id}, name={name}, allowed_ips={allowed_ips}, credentials={credentials})".format(
            project_id=self.project_id,
            name=self.name,
            allowed_ips=self.allowed_ips,
            credentials=self.credentials,
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