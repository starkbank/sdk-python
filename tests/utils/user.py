import starkbank
import os

exampleProject = starkbank.Project(
    environment="sandbox",
    id=os.environ["SANDBOX_ID"],  # "9999999999999999"
    private_key=os.environ["SANDBOX_PRIVATE_KEY"],  # "-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIBEcEJZLk/DyuXVsEjz0w4vrE7plPXhQxODvcG1Jc0WToAcGBSuBBAAK\noUQDQgAE6t4OGx1XYktOzH/7HV6FBukxq0Xs2As6oeN6re1Ttso2fwrh5BJXDq75\nmSYHeclthCRgU8zl6H1lFQ4BKZ5RCQ==\n-----END EC PRIVATE KEY-----"
)

exampleOrganization = starkbank.Organization(
    environment="sandbox",
    id=os.environ["SANDBOX_ORGANIZATION_ID"],  # "8888888888888888"
    private_key=os.environ["SANDBOX_ORGANIZATION_PRIVATE_KEY"],  # "-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIBEcEJZLk/DyuXVsEjz0w4vrE7plPXhQxODvcG1Jc0WToAcGBSuBBAAK\noUQDQgAE6t4OGx1XYktOzH/7HV6FBukxq0Xs2As6oeN6re1Ttso2fwrh5BJXDq75\nmSYHeclthCRgU8zl6H1lFQ4BKZ5RCQ==\n-----END EC PRIVATE KEY-----"
)

assert exampleProject.environment != "production", "NEVER RUN THE TEST ROUTINE IN PRODUCTION"
