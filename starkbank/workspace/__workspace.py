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
    ## Attributes:
    - id [string, default None]: unique id returned when the workspace is created. ex: "5656565656565656"
    """

    def __init__(self, username, name, id=None):
        Resource.__init__(self, id=id)

        self.username = username
        self.name = name


_resource = {"class": Workspace, "name": "Workspace"}


def create(username, name, user=None):
    """# Create Workspace
    Send a Workspace for creation in the Stark Bank API
    ## Parameters (required):
    - username [string]: Simplified name to define the workspace URL. This name must be unique across all Stark Bank Workspaces. Ex: "starkbankworkspace"
    - name [string]: Full name that identifies the Workspace. This name will appear when people access the Workspace on our platform, for example. Ex: "Stark Bank Workspace"
    ## Parameters (optional):
    - user [Organization object, default None]: Organization object. Not necessary if starkbank.user was set before function call
    ## Return:
    - Workspace object with updated attributes
    """
    return rest.post_single(resource=_resource, entity=Workspace(username=username, name=name), user=user)


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
    - username [string]: query by the simplified name that defines the workspace URL. This name is always unique across all Stark Bank Workspaces. Ex: "starkbankworkspace"
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of Workspace objects with updated attributes
    """
    return rest.get_list(resource=_resource, limit=limit, username=username, ids=ids, user=user)
