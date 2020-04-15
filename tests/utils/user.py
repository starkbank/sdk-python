import starkbank

exampleProject = starkbank.Project(
    environment="sandbox",
    id="9999999999999999",
    private_key="""
    -----BEGIN EC PRIVATE KEY-----
    MHQCAQEEIBEcEJZLk/DyuXVsEjz0w4vrE7plPXhQxODvcG1Jc0WToAcGBSuBBAAK
    oUQDQgAE6t4OGx1XYktOzH/7HV6FBukxq0Xs2As6oeN6re1Ttso2fwrh5BJXDq75
    mSYHeclthCRgU8zl6H1lFQ4BKZ5RCQ==
    -----END EC PRIVATE KEY-----
    """,
)

assert exampleProject.environment != "production", "NEVER RUN THE TEST ROUTINE IN PRODUCTION"
