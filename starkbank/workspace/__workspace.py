from ..utils import rest
from ..utils.resource import Resource


class Workspace(Resource):
    """# Workspace object
    Workspaces are bank accounts. They have independent balances, statements, operations and permissions.
    The only property that is shared between your workspaces is that they are linked to your organization,
    which carries your basic informations, such as tax ID, name, etc..
    ## Parameters (required):
    - username [string]: Simplified name to define the workspace URL. This name must be unique across all Stark Bank Workspaces. Ex: "starkbankworkspace"
    - name [string]: Full name that identifies the Workspace. This name will appear when people access the Workspace on our platform, for example. Ex: "Stark Bank Workspace"
    - allowed_tax_ids [list of strings]: list of tax IDs that will be allowed to send Deposits to this Workspace. ex: ["012.345.678-90", "20.018.183/0001-80"]
    ## Attributes:
    - id [string, default None]: unique id returned when the workspace is created. ex: "5656565656565656"
    """

    def __init__(self, username, name, allowed_tax_ids=None, id=None):
        Resource.__init__(self, id=id)

        self.username = username
        self.name = name
        self.allowed_tax_ids = allowed_tax_ids


_resource = {"class": Workspace, "name": "Workspace"}


def create(username, name, allowed_tax_ids=None, user=None):
    """# Create Workspace
    Send a Workspace for creation in the Stark Bank API
    ## Parameters (required):
    - username [string]: Simplified name to define the workspace URL. This name must be unique across all Stark Bank Workspaces. Ex: "starkbankworkspace"
    - name [string]: Full name that identifies the Workspace. This name will appear when people access the Workspace on our platform, for example. Ex: "Stark Bank Workspace"
    ## Parameters (optional):
    - allowed_tax_ids [list of strings, default []]: list of tax IDs that will be allowed to send Deposits to this Workspace. If empty, all are allowed. ex: ["012.345.678-90", "20.018.183/0001-80"]
    - user [Organization object, default None]: Organization object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Workspace object with updated attributes
    """
    workspace = Workspace(username=username, name=name, allowed_tax_ids=allowed_tax_ids)
    return rest.post_single(resource=_resource, entity=workspace, user=user)


def get(id, user=None):
    """# Retrieve a specific Workspace
    Receive a single Workspace object previously created in the Stark Bank API by passing its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Workspace object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, username=None, ids=None, user=None):
    """# Retrieve Workspaces
    Receive a generator of Workspace objects previously created in the Stark Bank API.
    If no filters are passed and the user is an Organization, all of the Organization Workspaces
    will be retrieved.
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - username [string, default None]: query by the simplified name that defines the workspace URL. This name is always unique across all Stark Bank Workspaces. Ex: "starkbankworkspace"
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of Workspace objects with updated attributes
    """
    return rest.get_stream(resource=_resource, limit=limit, username=username, ids=ids, user=user)


def update(id, username=None, name=None, allowed_tax_ids=None, user=None):
    """# Update Workspace entity
    Update a Workspace by passing its ID.
    ## Parameters (required):
    - id [string]: Workspace ID. ex: '5656565656565656'
    ## Parameters (optional):
    - username [string]: Simplified name to define the workspace URL. This name must be unique across all Stark Bank Workspaces. Ex: "starkbank-workspace"
    - name [string]: Full name that identifies the Workspace. This name will appear when people access the Workspace on our platform, for example. Ex: "Stark Bank Workspace"
    - allowed_tax_ids [list of strings, default []]: list of tax IDs that will be allowed to send Deposits to this Workspace. If empty, all are allowed. ex: ["012.345.678-90", "20.018.183/0001-80"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - target Workspace with updated attributes
    """
    return rest.patch_id(resource=_resource, id=id, user=user, username=username, name=name, allowed_tax_ids=allowed_tax_ids)


def page(cursor=None, limit=None, username=None, ids=None, user=None):
    """# Retrieve paged Workspaces
    Receive a list of up to 100 Workspace objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - username [string, default None]: query by the simplified name that defines the workspace URL. This name is always unique across all Stark Bank Workspaces. Ex: "starkbankworkspace"
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - list of Workspace objects with updated attributes
    - cursor to retrieve the next page of Workspace objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        username=username,
        ids=ids,
        user=user,
    )
