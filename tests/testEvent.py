import starkbank
from unittest import TestCase, main

from tests.utils.user import exampleProject


class TestEventGet(TestCase):

    def testSuccess(self):
        events, cursor, errors = starkbank.webhook.event.list(user=exampleProject)
        self.assertEqual(0, len(errors))
        print("Number of events:", len(events))
        self.assertIsInstance(events, list)

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     events, errors = starkbank.webhook.event.list(user=exampleMember, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     for log in content["events"]:
    #         self.assertTrue(set(log.keys()).issubset(fields))
    #     print(content)


class TestEventInfoGet(TestCase):
    def testSuccess(self):
        events, cursor, errors = starkbank.webhook.event.list(user=exampleProject)
        eventId = events[0].id
        event, errors = starkbank.webhook.event.retrieve(user=exampleProject, id=eventId)
        self.assertEqual(0, len(errors))

    # def testFields(self):
    #     raise NotImplementedError
    #     fields = {"amount", "id", "created", "invalid"}
    #     fieldsParams = {"fields": ",".join(fields)}
    #     events, errors = starkbank.webhook.event.list(user=exampleMember)
    #     events = content["events"]
    #     eventId = events[0]["id"]
    #     events, errors = starkbank.webhook.event.retrieve(user=exampleMember, eventId=eventId, params=fieldsParams)
    #     self.assertEqual(0, len(errors))
    #     event = content["event"]
    #     print(content)
    #     self.assertTrue(set(event.keys()).issubset(fields))


if __name__ == '__main__':
    main()
