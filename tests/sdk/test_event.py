import starkbank
from random import choice
from json import loads, dumps
from unittest import TestCase, main
from starkcore.error import InvalidSignatureError
from tests.utils.user import exampleProject

starkbank.user = exampleProject


class TestEventQuery(TestCase):

    def test_success(self):
        events = list(starkbank.event.query(limit=5))
        for event in events:
            print(event.id)
            for attempt in starkbank.event.attempt.query(event_ids=event.id, limit=1):
                print(starkbank.event.attempt.get(attempt.id).id)
                break


class TestEventPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            events, cursor = starkbank.event.page(limit=2, cursor=cursor)
            for event in events:
                print(event)
                self.assertFalse(event.id in ids)
                ids.append(event.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 4)


class TestEventInfoGet(TestCase):
    def test_success(self):
        events = starkbank.event.query(user=exampleProject)
        event_id = next(events).id
        event = starkbank.event.get(user=exampleProject, id=event_id)
        self.assertIsNotNone(event.id)
        self.assertEqual(event_id, event.id)


class TesteEventProcess(TestCase):
    content = '{"event": {"created": "2021-04-26T20:16:51.866857+00:00", "id": "5415223380934656", "log": {"created": "2021-04-26T20:16:50.927706+00:00", "errors": [], "id": "4687457496858624", "invoice": {"amount": 256, "brcode": "00020101021226890014br.gov.bcb.pix2567invoice-h.sandbox.starkbank.com/v2/afdf94b770b0458a8440a335daf77c4c5204000053039865802BR5915Stark Bank S.A.6009Sao Paulo62070503***6304CC32", "created": "2021-04-26T20:16:50.886319+00:00", "descriptions": [{"key": "Field1", "value": "Something"}], "discountAmount": 0, "discounts": [{"due": "2021-05-07T09:43:15+00:00", "percentage": 10.0}], "due": "2021-05-09T19:11:39+00:00", "expiration": 123456789, "fee": 0, "fine": 2.5, "fineAmount": 0, "id": "5941925571985408", "interest": 1.3, "interestAmount": 0, "link": "https://cdottori.sandbox.starkbank.com/invoicelink/afdf94b770b0458a8440a335daf77c4c", "name": "Oscar Cartwright", "nominalAmount": 256, "pdf": "https://invoice-h.sandbox.starkbank.com/pdf/afdf94b770b0458a8440a335daf77c4c", "status": "created", "tags": ["war supply", "invoice #1234"], "taxId": "337.451.076-08", "transactionIds": [], "updated": "2021-04-26T20:16:51.442989+00:00"}, "type": "created"}, "subscription": "invoice", "workspaceId": "5078376503050240"}}'
    valid_signature = "MEUCIG69+s7bcS9pvvbwN0Rx9xtsVQcIuavfdJvAi2wtyHMdAiEAh/vtDWJjI76IcJvci1BNw10iM2qV57Jb5VUOLcQAZmY="
    invalid_signature = "MEUCIQDOpo1j+V40DNZK2URL2786UQK/8mDXon9ayEd8U0/l7AIgYXtIZJBTs8zCRR3vmted6Ehz/qfw1GRut/eYyvf1yOk="
    malformed_signature = "something is definitely wrong"

    def test_success(self):
        event = starkbank.event.parse(
            content=self.content,
            signature=self.valid_signature
        )
        print(event)

    def test_normalized_success(self):
        event = starkbank.event.parse(
            content=dumps(loads(self.content), sort_keys=False, indent=4),
            signature=self.valid_signature
        )
        print(event)

    def test_invalid_signature(self):
        with self.assertRaises(InvalidSignatureError):
            starkbank.event.parse(
                content=self.content,
                signature=self.invalid_signature,
            )

    def test_malformed_signature(self):
        with self.assertRaises(InvalidSignatureError):
            starkbank.event.parse(
                content=self.content,
                signature=self.malformed_signature,
            )


class TestEventDelete(TestCase):

    def test_success(self):
        event = choice(list(starkbank.event.query(limit=100, is_delivered=True)))
        event = starkbank.event.delete(event.id)
        print(event)


class TestEventSetDelivered(TestCase):

    def test_success(self):
        event = choice(list(starkbank.event.query(limit=100, is_delivered=False)))
        assert event.is_delivered is False
        event = starkbank.event.update(id=event.id, is_delivered=True)
        event = starkbank.event.get(event.id)
        assert event.is_delivered is True
        print(event)


if __name__ == '__main__':
    main()
