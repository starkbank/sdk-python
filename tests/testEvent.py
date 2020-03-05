from unittest import TestCase, main

from starkbank.old_webhook.event import getEventInfo, getEvent
from tests.utils.user import exampleMemberOld


class TestEventGet(TestCase):

    def testSuccess(self):
        content, status = getEvent(exampleMemberOld)
        self.assertEqual(200, status)
        events = content["events"]
        print("Number of events:", len(events))
        print(content)
        self.assertIsInstance(events, list)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getEvent(exampleMemberOld, params=fieldsParams)
        self.assertEqual(200, status)
        for log in content["events"]:
            self.assertTrue(set(log.keys()).issubset(fields))
        print(content)


class TestEventInfoGet(TestCase):
    def testSuccess(self):
        content, status = getEvent(exampleMemberOld)
        events = content["events"]
        eventId = events[0]["id"]
        content, status = getEventInfo(exampleMemberOld, eventId=eventId)
        print(content)
        self.assertEqual(200, status)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getEvent(exampleMemberOld)
        events = content["events"]
        eventId = events[0]["id"]
        content, status = getEventInfo(exampleMemberOld, eventId=eventId, params=fieldsParams)
        self.assertEqual(200, status)
        event = content["event"]
        print(content)
        self.assertTrue(set(event.keys()).issubset(fields))


if __name__ == '__main__':
    main()
