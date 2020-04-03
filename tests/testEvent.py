from unittest import TestCase, main

import starkbank
from starkbank.error import InvalidSignatureError
from tests.utils.user import exampleProject

starkbank.user = exampleProject


class TestEventGet(TestCase):

    def test_success(self):
        events = list(starkbank.webhook.event.query(user=exampleProject, limit=10))
        print("Number of events:", len(events))


class TestEventInfoGet(TestCase):
    def test_success(self):
        events = starkbank.webhook.event.query(user=exampleProject)
        event_id = next(events).id
        event = starkbank.webhook.event.get(user=exampleProject, id=event_id)


class TesteEventProcess(TestCase):
    content = '{"event": {"log": {"transfer": {"status": "processing", "updated": "2020-04-03T13:20:33.485644+00:00", "fee": 160, "name": "Lawrence James", "accountNumber": "10000-0", "id": "5107489032896512", "tags": [], "taxId": "91.642.017/0001-06", "created": "2020-04-03T13:20:32.530367+00:00", "amount": 2, "transactionIds": ["6547649079541760"], "bankCode": "01", "branchCode": "0001"}, "errors": [], "type": "sending", "id": "5648419829841920", "created": "2020-04-03T13:20:33.164373+00:00"}, "subscription": "transfer", "id": "6234355449987072", "created": "2020-04-03T13:20:40.784479+00:00"}}'
    valid_signature = "MEYCIQCmFCAn2Z+6qEHmf8paI08Ee5ZJ9+KvLWSS3ddp8+RF3AIhALlK7ltfRvMCXhjS7cy8SPlcSlpQtjBxmhN6ClFC0Tv6"
    invalid_signature = "MEUCIQDOpo1j+V40DNZK2URL2786UQK/8mDXon9ayEd8U0/l7AIgYXtIZJBTs8zCRR3vmted6Ehz/qfw1GRut/eYyvf1yOk="

    def test_success(self):
        event = starkbank.webhook.event.parse(
            content=self.content,
            signature=self.valid_signature
        )

        print(event)

    def test_fail(self):
        with self.assertRaises(InvalidSignatureError):
            starkbank.webhook.event.parse(
                content=self.content,
                signature=self.invalid_signature,
            )


class TestEventDelete(TestCase):

    def test_success(self):
        event = next(starkbank.webhook.event.query(limit=1))
        event = starkbank.webhook.event.delete(event.id)
        print(event)


class TestEventSetDelivered(TestCase):

    def test_success(self):
        event = next(starkbank.webhook.event.query(limit=1, is_delivered=False))
        assert event.is_delivered is False
        event = starkbank.webhook.event.update(id=event.id, is_delivered=True)
        event = starkbank.webhook.event.get(event.id)
        assert event.is_delivered is True
        print(event)


if __name__ == '__main__':
    main()
