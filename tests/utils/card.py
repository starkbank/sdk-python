from random import choice
from starkbank import CorporateCard


example_card = CorporateCard(
    holder_id="",
)


def generateExampleCardJson(holder):
    example_card.holder_id = holder.id
    return example_card


debitCards = [
    {
        "expiration": "2035-01",
        "card_number": "5277696455399733",
        "card_security_code": "123",
    },
    {
        "expiration": "2035-01",
        "card_number": "2223000148400010",
        "card_security_code": "123",
    },
    {
        "expiration": "2035-01",
        "card_number": "4761120000000148",
        "card_security_code": "123",
    },
    {
        "expiration": "2035-01",
        "card_number": "4824810010000006",
        "card_security_code": "123",
    },
    {
        "expiration": "2035-01",
        "card_number": "5204970000000007",
        "card_security_code": "123",
    },
]

creditCards = [
    {
        "expiration": "2035-01",
        "card_number": "5448280000000007",
        "card_security_code": "123",
    },
    {
        "expiration": "2035-01",
        "card_number": "4235647728025682",
        "card_security_code": "123",
    },
    {
        "expiration": "2035-01",
        "card_number": "6062825624254001",
        "card_security_code": "123",
    },
    {
        "expiration": "2035-01",
        "card_number": "36490101441625",
        "card_security_code": "123",
    },
]


def randomCreditCard():
    return choice(creditCards)


def randomDebitCard():
    return choice(debitCards)
