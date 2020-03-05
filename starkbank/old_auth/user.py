from time import time

from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey

from starkbank.old_auth.project import postProject
from starkbank.old_auth.session import postSession


class User:

    def __init__(self, accessId, privateKeyString, publicKeyString):
        self.signedIn = False
        self.type = None
        self.accessId = accessId
        self.privateKeyString = privateKeyString
        self.publicKeyString = publicKeyString
        self.privateKey = PrivateKey.fromPem(privateKeyString)
        self.publicKey = PublicKey.fromPem(publicKeyString)

    def getHeaders(self, message=""):
        headers = dict()
        timestamp = str(int(time()))
        message = f"{self.accessId}:{timestamp}:{message}"
        print(message)
        digitalSignature = Ecdsa.sign(message=message, privateKey=self.privateKey).toBase64()
        headers.update({
            "Access-Time": timestamp,
            "Access-Signature": digitalSignature,
            "Access-Id": self.accessId,
            'Content-Type': 'application/json',
        })
        return headers

    def newSession(self, privateKeyString, publicKeyString, platform="api", duration=3600):
        content, status = postSession(self, publicKeyString, platform=platform, duration=duration)
        if status >= 300:
            raise Exception(f"{status}: {str(content)}")
        sessionId = content["session"]["id"]
        session = Session(sessionId, privateKeyString, publicKeyString, duration=duration)
        return session

    def newProject(self, name, privateKeyString, publicKeyString, platform="api", allowedIps=None):
        content, status = postProject(
            user=self,
            name=name,
            publicKeyString=publicKeyString,
            platform=platform,
            allowedIps=allowedIps
        )
        print(content)
        if status >= 300:
            raise Exception(f"{status}: {str(content)}")
        projectId = content["project"]["id"]
        project = Project(
            projectId=projectId,
            name=name,
            publicKeyString=publicKeyString,
            privateKeyString=privateKeyString,
        )
        return project


class Member(User):
    def __init__(self, credentialsJson, privateKeyString, publicKeyString):
        memberCredentials = credentialsJson
        self.workspaceId = memberCredentials["workspaceId"]
        self.email = memberCredentials["email"]
        accessId = f"workspace/{self.workspaceId}/email/{self.email}"
        super().__init__(
            accessId=accessId,
            privateKeyString=privateKeyString,
            publicKeyString=publicKeyString,
        )


class Project(User):
    def __init__(self, projectId, name, privateKeyString, publicKeyString):
        self.projectId = projectId
        self.name = name
        accessId = f"project/{self.projectId}"
        super().__init__(
            accessId=accessId,
            privateKeyString=privateKeyString,
            publicKeyString=publicKeyString,
        )


class Session(User):
    def __init__(self, sessionId, privateKeyString, publicKeyString, duration=3600):
        self.sessionId = sessionId
        self.duration = duration
        accessId = f"session/{self.sessionId}"
        super().__init__(
            accessId=accessId,
            privateKeyString=privateKeyString,
            publicKeyString=publicKeyString,
        )
