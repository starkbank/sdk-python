from unittest import TestCase, main

from starkbank.old_auth.session import postSession, getSession, getSessionInfo, deleteSession
from tests.utils.session import generateExampleSessionData
from tests.utils.user import exampleMember


class TestSession(TestCase):
    def testSessionPost(self):
        publicKeyString, platform, duration = generateExampleSessionData(duration=3600)
        content, status = postSession(
            user=exampleMember,
            publicKeyString=publicKeyString,
            platform=platform,
            duration=duration,
        )
        print(content)
        if status != 200:
            code = content["errors"][0]["code"]
            self.assertEqual('invalidBalance', code)
        else:
            self.assertEqual(200, status)

    def testSessionPostAndGet(self):
        publicKeyString, platform, duration = generateExampleSessionData(duration=3600)
        content, status = postSession(
            user=exampleMember,
            publicKeyString=publicKeyString,
            platform=platform,
            duration=duration,
        )
        print(content)
        self.assertEqual(200, status)
        content, status = getSession(exampleMember)
        sessionId = content["sessions"][0]["id"]
        content, status = getSessionInfo(exampleMember, sessionId=sessionId)
        print(content)
        self.assertEqual(200, status)

    def testSessionInfoPostAndGet(self):
        publicKeyString, platform, duration = generateExampleSessionData(duration=3600)
        content, status = postSession(
            user=exampleMember,
            publicKeyString=publicKeyString,
            platform=platform,
            duration=duration,
        )
        print(content)
        self.assertEqual(200, status)
        content, status = getSession(exampleMember)
        sessionId = content["sessions"][0]["id"]
        content, status = getSessionInfo(exampleMember, sessionId=sessionId)
        print(content)
        self.assertEqual(200, status)

    def testSessionPostAndDelete(self):
        publicKeyString, platform, duration = generateExampleSessionData(duration=3600)
        content, status = postSession(
            user=exampleMember,
            publicKeyString=publicKeyString,
            platform=platform,
            duration=duration,
        )
        print(content)
        self.assertEqual(200, status)
        sessionId = content["session"]["id"]
        content, status = deleteSession(exampleMember, sessionId=sessionId)
        print(content)
        self.assertEqual(200, status)


if __name__ == '__main__':
    main()
