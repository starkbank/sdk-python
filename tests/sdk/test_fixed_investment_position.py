import starkbank
from datetime import date, timedelta
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestFixedInvestmentPosition(TestCase):

    def test_success(self):
        position = starkbank.fixedinvestment.position(after=date.today() - timedelta(days=30), before=date.today())
        print(position)
        self.assertIsInstance(position, starkbank.fixedinvestment.Position)
        for amount in [
            position.initial_nominal_amount,
            position.deposited_amount,
            position.withdrawn_amount,
            position.yield_amount,
            position.final_nominal_amount,
            position.ir_preview,
            position.regressive_and_fee_preview,
        ]:
            self.assertIsInstance(amount, int)

    def test_success_string_dates(self):
        today = date.today()
        position = starkbank.fixedinvestment.position(after=str(today - timedelta(days=1)), before=str(today))
        self.assertIsInstance(position, starkbank.fixedinvestment.Position)


if __name__ == '__main__':
    main()
