import starkbank
from datetime import timedelta, date
from unittest import TestCase, main
from tests.utils.user import exampleProject, exampleOrganization


starkbank.user = exampleProject


class TestSplitProfilePut(TestCase):

    def test_success(self):
        splitprofiles =[{
            "interval": "day",
            "delay": 0
        }]
        response = starkbank.splitprofile.put(splitprofiles)
        self.assertEqual(len(splitprofiles), 1)
        for splitprofile in response:
            self.assertIsNotNone(splitprofile.id)


class TestSplitProfileQuery(TestCase):

    def test_success(self):
        splitprofiles = list(starkbank.splitprofile.query(limit=2))
        for profile in splitprofiles:
            print(profile)
        assert len(splitprofiles) == 1

    def test_success_with_params(self):
        splitprofiles = starkbank.splitprofile.query(
            limit=2,
            after=date.today() - timedelta(days=100),
            before=date.today(),
            status="created",
            tags=["test"],
        )
        for receiver in splitprofiles:
            print(receiver)
        self.assertEqual(len(list(splitprofiles)), 0)


class TestSplitProfilePage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            logs, cursor = starkbank.splitprofile.page(limit=2, cursor=cursor)
            for log in logs:
                print(log)
                self.assertFalse(log.id in ids)
                ids.append(log.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) == 1)


class TestSplitProfileInfoGet(TestCase):

    def test_success(self):
        splitprofiles = starkbank.splitprofile.query()
        splitprofile_id = next(splitprofiles).id
        splitprofile = starkbank.splitprofile.get(splitprofile_id)
        self.assertIsNotNone(splitprofile.id)
        self.assertEqual(splitprofile.id, splitprofile_id)
    
    def test_success_ids(self):
        splitProfiles = starkbank.splitprofile.query(limit=2)
        splitProfiles_ids_expected = [t.id for t in splitProfiles]
        splitProfiles_ids_result = [t.id for t in starkbank.splitprofile.query(ids=splitProfiles_ids_expected)]
        splitProfiles_ids_expected.sort()
        splitProfiles_ids_result.sort()
        self.assertTrue(splitProfiles_ids_result)
        self.assertEqual(splitProfiles_ids_expected, splitProfiles_ids_result)


if __name__ == '__main__':
    main()
