# coding: utf-8
from copy import deepcopy
from random import randint
from starkbank import DynamicBrcode
from starkbank.dynamicbrcode import Rule

example_brcode = DynamicBrcode(
    amount=400000,
    expiration=3600,
    tags=[
        "python-SDK/test"
    ],
    display_description="Payment for service #1234",
    rules=[
        Rule(
            key="allowedTaxIds",
            value=["012.345.678-90"]
        )
    ]
)


def generateExampleDynamicBrcodesJson(n=1, amount=None, expiration=None):
    brcodes = []
    for _ in range(n):
        if amount is None:
            brcodeAmount = randint(205, 300)
        else:
            brcodeAmount = int(amount)
        example_brcode.amount = brcodeAmount
        if expiration is None:
            brcodeExpiration = randint(0, 10000)
        else:
            brcodeExpiration = int(expiration)
        example_brcode.expiration = brcodeExpiration
        brcodes.append(deepcopy(example_brcode))
    return brcodes
