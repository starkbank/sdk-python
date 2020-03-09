from starkbank.user.base import User
from starkbank.user.credentials import Credentials
from starkbank.utils.checks import check_string, check_list_of_strings, check_user


class Project(User):

    _json_fill = ["privateKey"]

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


Project._define_known_fields()

get = Project._get_id
query = Project._query
delete = Project._delete
