import starkbank
from unittest import TestCase, main

from tests.utils.user import exampleProject


class TestEventGet(TestCase):

    def test_success(self):
        events = list(starkbank.webhook.event.query(user=exampleProject, limit=10))
        print("Number of events:", len(events))


class TestEventInfoGet(TestCase):
    def test_success(self):
        events = starkbank.webhook.event.query(user=exampleProject)
        eventId = next(events).id
        event = starkbank.webhook.event.get(user=exampleProject, id=eventId)


if __name__ == '__main__':
    main()
