# coding: utf-8
from copy import deepcopy
from datetime import datetime, timezone
from uuid import uuid4
from random import randint, choice
from starkbank import PaymentLink
from starkbank.paymentlink import AllowedInstallment, Item


example_payment_link = PaymentLink(
    name="Assinatura Premium",
    amount=15000,
    usage_mode="single",
    allowed_methods=["credit", "debit"],
    allowed_installments=[
        AllowedInstallment(count=1, total_amount=15000),
        AllowedInstallment(count=2, total_amount=15500),
        AllowedInstallment(count=3, total_amount=16500),
    ],
    expiration=36000,
    description="Plano Premium Mensal",
    success_url="https://merchant.com/obrigado",
    tags=["sdk-test", "payment-link"],
    items=[
        Item(
            code="PREM-001",
            description="Plano Premium Mensal",
            quantity=1,
            unit_price=15000,
            total_price=15000,
            discount=0,
        ),
    ],
    metadata={"customerId": "5678901234567890", "orderId": "ORD-2026-001"},
    timestamp=datetime.now(timezone.utc),
)


def generateExamplePaymentLinksJson(n=1):
    links = []
    for _ in range(n):
        link = deepcopy(example_payment_link)
        link.amount = randint(10000, 50000)
        link.usage_mode = choice(["single", "multi"])
        link.metadata = {
            "customerId": str(uuid4()),
            "orderId": "ORD-" + str(uuid4()),
        }
        link.allowed_installments = [
            AllowedInstallment(count=1, total_amount=link.amount),
            AllowedInstallment(count=2, total_amount=link.amount + 500),
            AllowedInstallment(count=3, total_amount=link.amount + 1500),
        ]
        link.items = [
            Item(
                code="ITEM-" + str(uuid4())[:8],
                description="Plano Premium Mensal",
                quantity=1,
                unit_price=link.amount,
                total_price=link.amount,
                discount=0,
            ),
        ]
        links.append(link)
    return links
