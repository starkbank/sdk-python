# coding: utf-8
from copy import deepcopy
from datetime import date, timedelta, datetime
from random import randint
from starkbank import Boleto
from .names.names import get_full_name
from .date import randomFutureDate, randomDateBetween
from .taxIdGenerator import TaxIdGenerator


example_boleto = Boleto(
    amount=10,
    due=date.today() + timedelta(days=3),
    name="Random Company",
    street_line_1="Rua ABC",
    street_line_2="Ap 123",
    district="Jardim Paulista",
    city="São Paulo",
    state_code="SP",
    zip_code="01234-567",
    tax_id="012.345.678-90",
    overdue_limit=10,
    fine=2.00,
    interest=1.00,
    descriptions=[
        {
            "text": "product A",
            "amount": 123
        },
        {
            "text": "product B",
            "amount": 456
        },
        {
            "text": "product C",
            "amount": 789
        }
    ],
    discounts=[
        {
            "percentage": 5,
            "date": date.today()
        },
        {
            "percentage": 3,
            "date": date.today() + timedelta(days=1)
        }
    ],
)


def generateExampleBoletosJson(n=1, amount=None, useRandomFutureDueDate=True, useRandomDiscount=False):
    boletos = []
    for _ in range(n):
        if amount is None:
            boletoAmount = randint(205, 300)
        else:
            boletoAmount = int(amount)
        if randint(0, 1):
            example_boleto.receiver_name = get_full_name()
            example_boleto.receiver_tax_id = TaxIdGenerator.taxId()
        example_boleto.name = get_full_name()
        example_boleto.amount = boletoAmount
        if useRandomFutureDueDate:
            example_boleto.due = randomFutureDate(days=7).date()
        if useRandomDiscount:
            example_boleto.discounts = [
                {
                    "percentage": 10 * randint(1, 9),
                    "date": str(randomDateBetween(datetime.today().date(), example_boleto.due))
                }
            ]
        example_boleto.tax_id = TaxIdGenerator.taxId()
        boletos.append(deepcopy(example_boleto))
    return boletos
