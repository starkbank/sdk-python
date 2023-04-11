from copy import deepcopy
from random import choice, randint
from starkbank import CorporateRule, MerchantCountry, CardMethod, MerchantCategory


example_rule = CorporateRule(
    name="Example Rule",
    interval="day",
    amount=100000,
    currency_code="USD"
)


def generateExampleRuleJson(n=1):
    rules = []
    for _ in range(n):
        example_rule.interval = choice(["day", "week", "month", "instant"])
        example_rule.amount = randint(1000, 100000)
        example_rule.currency_code = choice(["BRL", "USD"])
        example_rule.countries = [MerchantCountry(code=choice(["BRA", "USA"]))]
        example_rule.methods = [CardMethod(code=choice(["manual", "server", "token"]))]
        example_rule.categories = [choice([
            MerchantCategory(code=choice(["fastFoodRestaurants", "veterinaryServices"])),
            MerchantCategory(type=choice(["pets", "food"]))
        ])]
        rules.append(deepcopy(example_rule))
    return rules
