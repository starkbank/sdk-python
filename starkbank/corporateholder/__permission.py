from starkcore.utils.api import from_api_json
from starkcore.utils.checks import check_datetime
from starkcore.utils.subresource import SubResource


class Permission(SubResource):
    """# corporateholder.Permission object
    Permission object represents access granted to an user for a particular cardholder
    ## Parameters (optional):
    - owner_id [string, default None]: owner unique id. ex: "5656565656565656"
    - owner_type [string, default None]: owner type. ex: "project"
    ## Attributes (return only):
    - owner_email [string]: email address of the owner. ex: "tony@starkbank.com
    - owner_name [string]: name of the owner. ex: "Tony Stark"
    - owner_picture_url [string]: Profile picture Url of the owner. ex: "https://storage.googleapis.com/api-ms-workspace-sbx.appspot.com/pictures/member/6227829385592832?20230404164942"
    - owner_status [string]: current owner status. ex: "active", "blocked", "canceled"
    - created [datetime.datetime]: creation datetime for the Permission. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, owner_email=None, owner_id=None, owner_name=None, owner_picture_url=None, owner_status=None,
                 owner_type=None, created=None):
        self.owner_email = owner_email
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.owner_picture_url = owner_picture_url
        self.owner_status = owner_status
        self.owner_type = owner_type
        self.created = check_datetime(created)


_resource = {"class": Permission, "name": "Permission"}


def parse_permissions(permissions):
    parsed_permissions = []
    if permissions is None:
        return permissions
    for permission in permissions:
        if isinstance(permission, Permission):
            parsed_permissions.append(permission)
            continue
        parsed_permissions.append(from_api_json(_resource, permission))
    return parsed_permissions
