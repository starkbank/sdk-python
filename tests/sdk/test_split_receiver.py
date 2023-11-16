import starkbank
from datetime import timedelta, date
from unittest import TestCase, main
from tests.utils.splitReceiver import generateExampleSplitReceiversJson
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestSplitReceiverPost(TestCase):

    def test_success(self):
        splitreceivers = generateExampleSplitReceiversJson(n=2)
        splitreceivers = starkbank.splitreceiver.create(splitreceivers)
        self.assertEqual(len(splitreceivers), 2)
        for splitreceiver in splitreceivers:
            self.assertIsNotNone(splitreceiver.id)


class TestSplitReceiverQuery(TestCase):

    def test_success(self):
        splitreceivers = list(starkbank.splitreceiver.query(limit=2))
        for receiver in splitreceivers:
            print(receiver)
        assert len(splitreceivers) == 2

    def test_success_with_params(self):
        splitreceivers = starkbank.splitreceiver.query(
            limit=2,
            after=date.today() - timedelta(days=100),
            before=date.today(),
            status="created",
            tags=["test"],
        )
        for receiver in splitreceivers:
            print(receiver)
        self.assertEqual(len(list(splitreceivers)), 0)


class TestSplitReceiverPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            splitreceivers, cursor = starkbank.splitreceiver.page(limit=1, cursor=cursor)
            for splitreceiver in splitreceivers:
                print(splitreceiver)
                self.assertFalse(splitreceiver.id in ids)
                ids.append(splitreceiver.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 2)


class TestSplitReceiverInfoGet(TestCase):

    def test_success(self):
        splitreceivers = starkbank.splitreceiver.query()
        splitreceiver_id = next(splitreceivers).id
        splitreceiver = starkbank.splitreceiver.get(id=splitreceiver_id)
        self.assertIsNotNone(splitreceiver.id)
        self.assertEqual(splitreceiver.id, splitreceiver_id)
    
    def test_success_ids(self):
        splitreceivers = starkbank.splitreceiver.query(limit=2)
        splitreceivers_ids_expected = [t.id for t in splitreceivers]
        splitreceivers_ids_result = [t.id for t in starkbank.splitreceiver.query(ids=splitreceivers_ids_expected)]
        splitreceivers_ids_expected.sort()
        splitreceivers_ids_result.sort()
        self.assertTrue(splitreceivers_ids_result)
        self.assertEqual(splitreceivers_ids_expected, splitreceivers_ids_result)


if __name__ == '__main__':
    main()
