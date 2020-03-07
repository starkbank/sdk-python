from starkbank import request
from starkbank.user.base import User
from starkbank.user.credentials import Credentials
from starkbank.utils.checks import check_string, check_list_of_strings, check_user


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


def retrieve(user, id):
    response = request.get(
        user=user,
        endpoint="project/{id}".format(id=id),
    )

    project_info = response["project"]

    return Project(
        private_key=None,
        id=project_info["id"],
        name=project_info["name"],
        allowed_ips=project_info["allowedIps"]
    )


def list(limit=100, cursor=None, user=None):
    url_params = {
        "limit": limit,
    }
    if cursor:
        url_params["cursor"] = check_string(cursor)

    response = request.get(
        user=check_user(user),
        endpoint="project",
        url_params=url_params,
    )

    projects = response["projects"]

    return [Project(
        private_key=None,
        id=project_info["id"],
        name=project_info["name"],
        allowed_ips=project_info["allowedIps"]
    ) for project_info in projects]


def delete(id, user=None):
    response = request.delete(
        user=check_user(user),
        endpoint="project/{id}".format(id=id),
    )

    project_info = response["project"]

    return Project(
        private_key=None,
        id=project_info["id"],
        name=project_info["name"],
        allowed_ips=project_info["allowedIps"]
    )
