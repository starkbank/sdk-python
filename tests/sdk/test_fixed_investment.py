import starkbank
from time import sleep, time
from datetime import datetime, timedelta
from unittest import TestCase, main
from starkcore.error import InputErrors, UnknownError
from tests.utils.date import randomPastDate
from tests.utils.user import exampleProject
from tests.utils.fixedInvestment import generateExampleFixedInvestmentsJson


starkbank.user = exampleProject


class TestFixedInvestmentPost(TestCase):

    def test_success(self):
        investments = generateExampleFixedInvestmentsJson(n=1, amount=100000)
        investments = starkbank.fixedinvestment.create(investments)
        self.assertEqual(len(investments), 1)
        for investment in investments:
            print(investment)
            self.assertIsNotNone(investment.id)
            self.assertIsInstance(investment, starkbank.FixedInvestment)
            self.assertEqual(investment.nominal_amount, 100000)
            self.assertIn(investment.status, ["processing", "active"])
            self.assertIsInstance(investment.due, datetime)
            self.assertIsInstance(investment.created, datetime)

    def test_fail_amount_below_minimum(self):
        investments = generateExampleFixedInvestmentsJson(n=1, amount=99999)
        with self.assertRaises(InputErrors) as context:
            starkbank.fixedinvestment.create(investments)
        for error in context.exception.errors:
            print(error)


class TestFixedInvestmentQuery(TestCase):

    def test_success_after_before(self):
        after = randomPastDate(days=30)
        before = datetime.today()
        investments = starkbank.fixedinvestment.query(after=after.date(), before=before.date(), limit=10)
        for investment in investments:
            self.assertIsInstance(investment, starkbank.FixedInvestment)
            self.assertTrue(after.date() <= investment.created.date() <= (before + timedelta(hours=3)).date())

    def test_success_status_list(self):
        status = ["active", "voided"]
        investments = starkbank.fixedinvestment.query(status=status, limit=10)
        for investment in investments:
            self.assertIn(investment.status, status)


class TestFixedInvestmentPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            investments, cursor = starkbank.fixedinvestment.page(limit=2, cursor=cursor)
            for investment in investments:
                self.assertFalse(investment.id in ids)
                ids.append(investment.id)
            if cursor is None:
                break
        self.assertTrue(len(ids) > 0)


class TestFixedInvestmentPatch(TestCase):

    def test_success_partial(self):
        investment = _createActiveInvestment(amount=200000)
        investments = starkbank.fixedinvestment.patch([{"id": investment.id, "amount": 100000}])
        self.assertEqual(len(investments), 1)
        for patched in investments:
            print(patched)
            self.assertIsInstance(patched, starkbank.FixedInvestment)
            self.assertEqual(patched.id, investment.id)
            self.assertEqual(patched.amount, 100000)
            self.assertEqual(patched.status, "active")

    def test_full_withdraw_full(self):
        investment = _createActiveInvestment(amount=100000)
        investments = starkbank.fixedinvestment.patch([{"id": investment.id, "amount": 0}])
        self.assertEqual(investments[0].id, investment.id)
        _waitForStatus(id=investment.id, status="voided")

    def test_success_full_multiple(self):
        created = starkbank.fixedinvestment.create(generateExampleFixedInvestmentsJson(n=2, amount=100000))
        # colcar await ? 
        ids = {investment.id for investment in created}
        for id in ids:
            _waitForStatus(id=id, status="active")
        investments = starkbank.fixedinvestment.patch([{"id": id, "amount": 0} for id in ids])
        self.assertEqual({investment.id for investment in investments}, ids)
        for id in ids:
            _waitForStatus(id=id, status="voided")

    def test_fail_remaining_below_minimum(self):
        investment = _createActiveInvestment(amount=100000)
        with self.assertRaises(InputErrors) as context:
            starkbank.fixedinvestment.patch([{"id": investment.id, "amount": 50000}])
        for error in context.exception.errors:
            print(error)
        self.assertEqual(starkbank.fixedinvestment.get(investment.id).amount, investment.amount)

    def test_fail_withdrawn_below_minimum(self):
        investment = _createActiveInvestment(amount=200000)
        with self.assertRaises(InputErrors) as context:
            starkbank.fixedinvestment.patch([{"id": investment.id, "amount": investment.amount - 50000}])
        for error in context.exception.errors:
            print(error)
        self.assertEqual(starkbank.fixedinvestment.get(investment.id).amount, investment.amount)

    def test_fail_invalid_id(self):
        with self.assertRaises(InputErrors) as context:
            starkbank.fixedinvestment.patch([{"id": "123", "amount": 0}])
        for error in context.exception.errors:
            print(error)


class TestFixedInvestmentGet(TestCase):

    def test_success(self):
        investment_id = next(starkbank.fixedinvestment.query(limit=1)).id
        investment = starkbank.fixedinvestment.get(investment_id)
        print(investment)
        self.assertEqual(investment.id, investment_id)
        self.assertIsInstance(investment.updated, datetime)

    def test_fail_invalid_id(self):
        with self.assertRaises(InputErrors) as context:
            starkbank.fixedinvestment.get("123")
        for error in context.exception.errors:
            print(error)


def _createActiveInvestment(amount):
    investment = starkbank.fixedinvestment.create(generateExampleFixedInvestmentsJson(n=1, amount=amount))[0]
    return _waitForStatus(id=investment.id, status="active")


def _waitForStatus(id, status, timeout=120):
    # investments change status asynchronously, ~25s in sandbox for both "active" and "voided"
    deadline = time() + timeout
    while time() < deadline:
        investment = _getUnlessUnreachable(id)
        if investment and investment.status == status:
            return investment
        sleep(5)
    raise TimeoutError("investment {id} did not reach {status} in {timeout}s".format(
        id=id,
        status=status,
        timeout=timeout,
    ))


def _getUnlessUnreachable(id):
    # about 1 in 5 connections to the sandbox times out at random, even at one request every 5s;
    # a read is safe to repeat, so the wait skips that attempt instead of failing the test
    try:
        return starkbank.fixedinvestment.get(id)
    except UnknownError as exception:
        if "ConnectTimeout" not in str(exception):
            raise
        print("investment {id} unreachable, retrying".format(id=id))
        return None


if __name__ == '__main__':
    main()
