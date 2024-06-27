import starkbank
from datetime import datetime, timedelta
import time
from unittest import TestCase, main
from tests.utils.date import randomPastDate
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestJokerGet(TestCase):

    def test_get(self):
        try:
            example_id = starkbank.request.get(
                path=f'/invoice/',
                query={"limit": 1, "status": "paid"},
            )

            request = starkbank.request.get(
                path=f'/invoice/{example_id.json()["invoices"][0]["id"]}',
                user=exampleProject
            )
            if request.status != 200:
                raise Exception(request.content)
            self.assertEqual(request.json()["invoice"]["id"], example_id.json()["invoices"][0]["id"])
        except Exception:
            raise Exception

    def test_get_pdf(self):
        example_id = starkbank.request.get(
            path=f'/invoice/',
            query={"limit": 10, "status": "paid"}
        ).json()["invoices"][0]["id"]
        pdf = starkbank.request.get(
            path=f'/invoice/{example_id}/pdf',
        ).content

        self.assertGreater(len(pdf), 1000)

    def test_get_qrcode(self):
        example_id = starkbank.request.get(
            path=f'/invoice/',
            query={"limit": 10, "status": "paid"}
        ).json()["invoices"][0]["id"]

        qrcode = starkbank.request.get(
            path=f'/invoice/{example_id}/qrcode',
            query={"size": 15},
        ).content
        self.assertGreater(len(qrcode), 1000)

    def test_get_reversal_receipt(self):
        example_id = starkbank.request.get(
            path=f'/deposit/log/',
            query={"limit": 1, "types": "reversed"}
        ).json()["logs"][0]["id"]
        reversal_pdf = starkbank.request.get(
            path=f'/deposit/log/{example_id}/pdf/',
        ).content
        self.assertGreater(len(reversal_pdf), 1000)

    def test_get_page(self):
        after = randomPastDate(days=10)
        before = datetime.today()
        request = starkbank.request.get(
            path=f'/invoice/',
            query={
                "limit": 10,
                "after": after.strftime("%Y-%m-%d"),
                "before": before.strftime("%Y-%m-%d"),
                "status": "paid"
            }
        ).json()
        for item in request["invoices"]:
            self.assertTrue(after.date() <= datetime.strptime(item["created"], "%Y-%m-%dT%H:%M:%S.%f%z").date() <= (before + timedelta(hours=3)).date())
        self.assertEqual(10, len(request["invoices"]))

    def test_get_pagination(self):
        after = randomPastDate(days=10)
        before = datetime.today()
        total_items = 0
        cursor = None
        i = 0
        while i <= 2:
            request = starkbank.request.get(
                path=f'/invoice/',
                query={
                    "limit": 10,
                    "after": after.strftime("%Y-%m-%d"),
                    "before": before.strftime("%Y-%m-%d"),
                    "status": "paid",
                    "cursor": cursor
                }
            ).json()
            cursor = request["cursor"]
            total_items += len(request["invoices"])
            for item in request["invoices"]:
                self.assertTrue(after.date() <= datetime.strptime(item["created"], "%Y-%m-%dT%H:%M:%S.%f%z").date() <= (before + timedelta(hours=3)).date())
            if cursor is None:
                break
            i += 1
            self.assertLessEqual(len(request["invoices"]), 10)
        self.assertLessEqual(total_items, 30)


class TestJokerPost(TestCase):

    def test_post(self):
        data={
            "invoices": [{
                "amount": 100,
                "name": "Iron Bank S.A.",
                "taxId": "20.018.183/0001-80"
            }]
        }
        request = starkbank.request.post(
            path=f'/invoice/',
            body=data,
        ).json()
        print(request)


class TestJokerPatch(TestCase):

    def test_patch(self):
        initial_state = starkbank.request.get(
            path=f'/invoice/',
            query={"limit": 1, "status": "paid"}
        ).json()
        example_id = initial_state["invoices"][0]["id"]
        amount = initial_state["invoices"][0]["amount"]

        starkbank.request.patch(
            path=f'/invoice/{example_id}/',
            body={"amount": amount - amount},
        ).json()

        final_state = starkbank.request.get(
            path=f'/invoice/{example_id}',
        ).json()
        self.assertEqual(final_state["invoice"]["amount"],0)


class TestJokerPut(TestCase):

    def test_put(self):
        data = {
            "profiles": [
                {
                    "interval": "day",
                    "delay": 0
                }
            ]
        }
        starkbank.request.put(
            path=f'/split-profile/',
            body=data,
        )

        result = starkbank.request.get(path=f'/split-profile/').json()

        self.assertEqual(result["profiles"][0]["delay"], 0)
        self.assertEqual(result["profiles"][0]["interval"], "day")


class TestJokerDelete(TestCase):

    def test_delete(self):
        future_date = datetime.now().date() + timedelta(days=10)

        data = {
            "transfers": [
                {
                    "amount": 10000,
                    "name": "Steve Rogers",
                    "taxId": "330.731.970-10",
                    "bankCode": "001",
                    "branchCode": "1234",
                    "accountNumber": "123456-0",
                    "accountType": "checking",
                    "scheduled": future_date.strftime("%Y-%m-%d"),
                    "externalId": str(int(time.time() * 1000)),
                }
            ]
        }

        create = starkbank.request.post(
            path=f'/transfer/',
            body=data,
        ).json()

        starkbank.request.delete(
            path=f'/transfer/{create["transfers"][0]["id"]}',
        ).json()

        final_status = starkbank.request.get(
            path=f'/transfer/{create["transfers"][0]["id"]}',
        ).json()["transfer"]["status"]

        self.assertEqual(final_status, 'canceled')


if __name__ == '__main__':
    main()
