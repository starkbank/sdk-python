from unittest import TestCase, main

import starkbank
from starkbank.exception import InvalidSignatureException
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
    def test_success(self):
        event = starkbank.webhook.event.parse(
            content='{"event": {"log": {"transfer": {"status": "failed", "updated": "2020-03-13T14:49:10.189611+00:00", "fee": 200, "name": "Richard Jenkins", "accountNumber": "10000-0", "id": "5599003076984832", "tags": ["19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7"], "taxId": "81.680.513/0001-92", "created": "2020-03-13T14:49:09.943811+00:00", "amount": 295136516, "transactionIds": ["invalidBalance"], "bankCode": "01", "branchCode": "0001"}, "errors": ["invalidbalance"], "type": "failed", "id": "6046244933730304", "created": "2020-03-13T14:49:10.189586+00:00"}, "delivered": null, "subscription": "transfer", "id": "6270003208781824", "created": "2020-03-13T14:49:11.236120+00:00"}}',
            signature="MEQCIGVKEnnhLFHjxKM+nDggweTsFEQOIsmnZkep2Ni5o8FeAiAVm//jnu3vmh9lxq1HRQcRW7SsMlqSGNERaa1CvnVnNA=="
        )

        print(event)

    def test_fail(self):
        with self.assertRaises(InvalidSignatureException) as context:
            event = starkbank.webhook.event.parse(
                content='{"event": {"log": {"transfer": {"status": "failed", "updated": "2020-03-13T14:49:10.189611+00:00", "fee": 200, "name": "Richard Jenkins", "accountNumber": "10000-0", "id": "5599003076984832", "tags": ["19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7"], "taxId": "81.680.513/0001-92", "created": "2020-03-13T14:49:09.943811+00:00", "amount": 295136516, "transactionIds": ["invalidBalance"], "bankCode": "01", "branchCode": "0001"}, "errors": ["invalidbalance"], "type": "failed", "id": "6046244933730304", "created": "2020-03-13T14:49:10.189586+00:00"}, "delivered": null, "subscription": "transfer", "id": "6270003208781824", "created": "2020-03-13T14:49:11.236120+00:00"}}',
                signature="MEYCIQC+0fzgh+WX6Af0hm9FsnWmsRaeQbTHI9vITB0d+lg9QwIhAMpz2xBRLm8dO+E4NQZXVxtxLJylkS1rqdlB06PQGIub"
            )


class TestEventDelete(TestCase):

    def test_success(self):
        event = next(starkbank.webhook.event.query(limit=1))
        event = starkbank.webhook.event.delete(event.id)
        print(event)


class TestEventSetDelivered(TestCase):

    def test_success(self):
        event = next(starkbank.webhook.event.query(limit=1))
        event = starkbank.webhook.event.set_delivered(event.id)
        print(event)


if __name__ == '__main__':
    main()
