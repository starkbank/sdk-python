from .user import User


class Project(User):
    """Description: Project object

    The Project object is the main authentication entity for the SDK.
    Every request to the Stark Bank API must be authenticated via a project,
    which must have been previously created at the Stark Bank website
    [https://sandbox.web.starkbank.com] or [https://web.starkbank.com]
    before you can use them with this SDK Projects may be passed as a parameter on
    each request or may be defined as the default user at the start (See README).

    Parameters (required):
        id [string]: unique id required to identify project. ex: "5656565656565656"
        private_key [string]: PEM string of the private key of the project.
        environment [string]: environment where the project is being used. ex: "sandbox" or "production"
    Attributes (return-only):
        name [string, default ""]: project name. ex: "MyProject"
        allowed_ips [list of strings]: list containing the strings of the ips allowed to make requests on behalf of this project. ex: ["190.190.0.50"]
        pem [string]: processed private key string
        kind [string]: type of access. ex: "project"
    """

    def __init__(self, id, environment, private_key, name="", allowed_ips=None):
        self.name = name
        self.allowed_ips = allowed_ips

        User.__init__(
            self,
            id=id,
            private_key=private_key,
            environment=environment,
        )
