from tests.utils.examples.keys.keys import sessionPublicKeyString


def generateExampleSessionData(duration=3600):
    return (
        sessionPublicKeyString,
        "api",
        duration,
    )
