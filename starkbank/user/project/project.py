from ..base import User
from ..credentials import Credentials
from ...utils.checks import check_id, check_string, check_list_of_strings


class Project(User):
    def __init__(self, private_key, project_id, name="", allowed_ips=[]):
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
