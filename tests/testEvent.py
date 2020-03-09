import starkbank
from unittest import TestCase, main

from tests.utils.user import exampleProject


class TestEventGet(TestCase):

    def testSuccess(self):
        events, cursor = starkbank.webhook.event.list(user=exampleProject)
        print("Number of events:", len(events))

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
        events, cursor = starkbank.webhook.event.list(user=exampleProject)
        eventId = events[0].id
        event = starkbank.webhook.event.get(user=exampleProject, id=eventId)

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
