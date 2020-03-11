import starkbank
from unittest import TestCase, main

from tests.utils.user import exampleProject

starkbank.user = exampleProject
starkbank.debug = False


class TestEventGet(TestCase):

    def test_success(self):
        events = list(starkbank.webhook.event.query(user=exampleProject, limit=10))
        print("Number of events:", len(events))


class TestEventInfoGet(TestCase):
    def test_success(self):
        events = starkbank.webhook.event.query(user=exampleProject, after="2020-03-10")
        event_id = next(events).id
        event = starkbank.webhook.event.get(user=exampleProject, id=event_id)


if __name__ == '__main__':
    main()
