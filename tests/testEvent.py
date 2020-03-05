from unittest import TestCase, main

from starkbank.old_webhook.event import getEventInfo, getEvent
from tests.utils.user import exampleMember


class TestEventGet(TestCase):

    def testSuccess(self):
        content, status = getEvent(exampleMember)
        self.assertEqual(200, status)
        events = content["events"]
        print("Number of events:", len(events))
        print(content)
        self.assertIsInstance(events, list)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getEvent(exampleMember, params=fieldsParams)
        self.assertEqual(200, status)
        for log in content["events"]:
            self.assertTrue(set(log.keys()).issubset(fields))
        print(content)


class TestEventInfoGet(TestCase):
    def testSuccess(self):
        content, status = getEvent(exampleMember)
        events = content["events"]
        eventId = events[0]["id"]
        content, status = getEventInfo(exampleMember, eventId=eventId)
        print(content)
        self.assertEqual(200, status)

    def testFields(self):
        fields = {"amount", "id", "created", "invalid"}
        fieldsParams = {"fields": ",".join(fields)}
        content, status = getEvent(exampleMember)
        events = content["events"]
        eventId = events[0]["id"]
        content, status = getEventInfo(exampleMember, eventId=eventId, params=fieldsParams)
        self.assertEqual(200, status)
        event = content["event"]
        print(content)
        self.assertTrue(set(event.keys()).issubset(fields))


if __name__ == '__main__':
    main()
