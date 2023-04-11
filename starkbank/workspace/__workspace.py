import base64
from starkcore.utils.checks import check_datetime
from ..utils import rest
from starkcore.utils.resource import Resource


class Workspace(Resource):
    """# Workspace object
    Workspaces are bank accounts. They have independent balances, statements, operations and permissions.
    The only property that is shared between your workspaces is that they are linked to your organization,
    which carries your basic informations, such as tax ID, name, etc..
    ## Parameters (required):
    - username [string]: Simplified name to define the workspace URL. This name must be unique across all Stark Bank Workspaces. ex: "starkbankworkspace"
    - name [string]: Full name that identifies the Workspace. This name will appear when people access the Workspace on our platform, for example. ex: "Stark Bank Workspace"
    ## Parameters (optional):
    - allowed_tax_ids [list of strings, default None]: list of tax IDs that will be allowed to send Deposits to this Workspace. If empty, all are allowed. ex: ["012.345.678-90", "20.018.183/0001-80"]
    ## Attributes (return-only):
    - id [string]: unique id returned when the workspace is created. ex: "5656565656565656"
    - status [string]: current Workspace status. Options: "active", "closed", "frozen" or "blocked"
    - organization_id [string]: unique organization id returned when the organization is created. ex: "5656565656565656"
    - picture_url [string]: public workspace image (png) URL. ex: "https://storage.googleapis.com/api-ms-workspace-sbx.appspot.com/pictures/workspace/6284441752174592.png?20230208220551"
    - created [datetime.datetime]: creation datetime of the workspace. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, username, name, allowed_tax_ids=None, id=None, status=None, organization_id=None, picture_url=None,
                 created=None):
        Resource.__init__(self, id=id)

        self.username = username
        self.name = name
        self.allowed_tax_ids = allowed_tax_ids
        self.status = status
        self.organization_id = organization_id
        self.picture_url = picture_url
        self.created = check_datetime(created)


_resource = {"class": Workspace, "name": "Workspace"}


def create(username, name, allowed_tax_ids=None, user=None):
    """# Create Workspace
    Send a Workspace for creation in the Stark Bank API
    ## Parameters (required):
    - username [string]: Simplified name to define the workspace URL. This name must be unique across all Stark Bank Workspaces. ex: "starkbankworkspace"
    - name [string]: Full name that identifies the Workspace. This name will appear when people access the Workspace on our platform, for example. ex: "Stark Bank Workspace"
    ## Parameters (optional):
    - allowed_tax_ids [list of strings, default None]: list of tax IDs that will be allowed to send Deposits to this Workspace. If empty, all are allowed. ex: ["012.345.678-90", "20.018.183/0001-80"]
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
    - username [string, default None]: query by the simplified name that defines the workspace URL. This name is always unique across all Stark Bank Workspaces. ex: "starkbankworkspace"
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - generator of Workspace objects with updated attributes
    """
    return rest.get_stream(resource=_resource, limit=limit, username=username, ids=ids, user=user)


def update(id, username=None, name=None, allowed_tax_ids=None, status=None, picture=None, picture_type=None, user=None):
    """# Update Workspace entity
    Update a Workspace by passing its ID.
    ## Parameters (required):
    - id [string]: Workspace ID. ex: '5656565656565656'
    ## Parameters (conditionally required):
    - picture_type [string]: picture MIME type. This parameter will be required if the picture parameter is informed ex: "image/png" or "image/jpeg"
    ## Parameters (optional):
    - username [string, default None]: Simplified name to define the workspace URL. This name must be unique across all Stark Bank Workspaces. ex: "starkbank-workspace"
    - name [string, default None]: Full name that identifies the Workspace. This name will appear when people access the Workspace on our platform, for example. ex: "Stark Bank Workspace"
    - allowed_tax_ids [list of strings, default None]: list of tax IDs that will be allowed to send Deposits to this Workspace. If empty, all are allowed. ex: ["012.345.678-90", "20.018.183/0001-80"]
    - status [string, default None]: current Workspace status. Options: "active" or "blocked"
    - picture [bytes, default None]: Binary buffer of the picture. ex: open("/path/to/file.png", "rb").read()
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call
    ## Return:
    - target Workspace with updated attributes
    """
    payload = {
        "allowedTaxIds": allowed_tax_ids,
        "status": status
    }

    if picture:
        payload["picture"] = "data:{picture_type};base64,{picture}".format(
            picture_type=picture_type,
            picture=base64.b64encode(picture).decode('utf-8')
        )

    return rest.patch_id(resource=_resource, id=id, user=user, username=username, name=name, payload=payload)


def page(cursor=None, limit=None, username=None, ids=None, user=None):
    """# Retrieve paged Workspaces
    Receive a list of up to 100 Workspace objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - username [string, default None]: query by the simplified name that defines the workspace URL. This name is always unique across all Stark Bank Workspaces. ex: "starkbankworkspace"
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
