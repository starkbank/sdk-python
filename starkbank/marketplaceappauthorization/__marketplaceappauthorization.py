from ..utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime


class MarketplaceAppAuthorization(Resource):

    def __init__(
        self,
        app_id,
        created,
        permissions,
        role_id,
        status,
        updated,
        workspace_id,
        workspace_role_ids,
        workspace_username,
        id=None,
        organization_id=None,
    ):
        Resource.__init__(self, id=id)
        self.app_id = app_id
        self.created = check_datetime(created)
        self.permissions = permissions
        self.role_id = role_id
        self.status = status
        self.updated = check_datetime(updated)
        self.workspace_id = workspace_id
        self.workspace_role_ids = workspace_role_ids
        self.workspace_username = workspace_username
        self.organization_id = organization_id


_resource = {
    "class": MarketplaceAppAuthorization,
    "name": "MarketplaceAppAuthorization",
}


def query(user=None):
    return rest.get_stream(resource=_resource, user=user)
