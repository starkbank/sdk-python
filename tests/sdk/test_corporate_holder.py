from uuid import uuid4
import starkbank
from unittest import TestCase, main
from datetime import date, timedelta
from tests.utils.user import exampleProject
from tests.utils.holder import generateExampleHoldersJson

starkbank.user = exampleProject


class TestCorporateHolderQuery(TestCase):

    def test_success(self):
        holders = starkbank.corporateholder.query(
            limit=10,
            expand=["rules"],
            after=date.today() - timedelta(days=100),
            before=date.today(),
        )
        for holder in holders:
            self.assertEqual(holder.id, str(holder.id))


class TestCorporateHolderPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            holders, cursor = starkbank.corporateholder.page(
                limit=2,
                after=date.today() - timedelta(days=100),
                before=date.today(),
                cursor=cursor
            )
            for holder in holders:
                self.assertFalse(holder.id in ids)
                ids.append(holder.id)
            if cursor is None:
                break


class TestCorporateHolderGet(TestCase):

    def test_success(self):
        holders = starkbank.corporateholder.query(limit=1)
        holder = starkbank.corporateholder.get(id=next(holders).id)
        self.assertEqual(holder.id, str(holder.id))


class TestCorporateHolderPostPatchAndDelete(TestCase):

    def test_success(self):
        holders = starkbank.corporateholder.create(generateExampleHoldersJson(n=1), expand=["rules"])
        holder_id = holders[0].id
        holder_name = "Updated Name" + str(uuid4())
        holder = starkbank.corporateholder.update(id=holder_id, name=holder_name)
        self.assertEqual(holder_name, holder.name)
        holder = starkbank.corporateholder.cancel(id=holder_id)
        self.assertEqual("canceled", holder.status)


if __name__ == '__main__':
    main()
