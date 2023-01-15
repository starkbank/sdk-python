# coding: utf-8
from copy import deepcopy
from random import randint
from starkbank import DynamicBrcode


example_brcode = DynamicBrcode(
    amount=400000,
    expiration=3600,
    tags=[
        "python-SDK/test"
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
