from starkcore.utils.api import from_api_json
from starkcore.utils.resource import Resource
from starkbank.cardmethod.__cardmethod import _resource as _method_resource, CardMethod
from starkbank.merchantcountry.__merchantcountry import _resource as _country_resource, MerchantCountry
from starkbank.merchantcategory.__merchantcategory import _resource as _category_resource, MerchantCategory


class CorporateRule(Resource):
    """CorporateRule object
    The CorporateRule object displays the spending rules of CorporateCards and CorporateHolders created in your Workspace.
    # Parameters (required):
    - name [string]: rule name. ex: "Travel" or "Food"
    - amount [integer]: maximum amount that can be spent in the informed interval. ex: 200000 (= R$ 2000.00)
    # Parameters (optional):
    - interval [string, default "lifetime"]: interval after which the rule amount counter will be reset to 0. ex: "instant", "day", "week", "month", "year" or "lifetime"
    - schedule [string, default None]: schedule time for user to spend. ex: "every monday, wednesday from 00:00 to 23:59 in America/Sao_Paulo"
    - purposes [list of string, default []]: list of strings representing the allowed purposes for card purchases, you can use this to restrict ATM withdrawals. ex: ["purchase", "withdrawal"]
    - currency_code [string, default "BRL"]: code of the currency that the rule amount refers to. ex: "BRL" or "USD"
    - categories [list of MerchantCategories, default []]: merchant categories accepted by the rule. ex: [MerchantCategory(code="fastFoodRestaurants")]
    - countries [list of MerchantCountries, default []]: countries accepted by the rule. ex: [MerchantCountry(code="BRA")]
    - methods [list of CardMethods, default []]: card purchase methods accepted by the rule. ex: [CardMethod(code="magstripe")]
    # Attributes (expanded return-only):
    - id [string]: unique id returned when a CorporateRule is created, used to update a specific CorporateRule. ex: "5656565656565656"
    - counter_amount [integer]: current rule spent amount. ex: 1000
    - currency_symbol [string]: currency symbol. ex: "R$"
    - currency_name [string]: currency name. ex: "Brazilian Real"
    """

    def __init__(self, name, amount, id=None, interval=None, schedule=None, purposes=None, currency_code=None, categories=None, countries=None,
                 methods=None, counter_amount=None, currency_symbol=None, currency_name=None):
        Resource.__init__(self, id=id)

        self.name = name
        self.amount = amount
        self.interval = interval
        self.schedule = schedule
        self.purposes = purposes
        self.currency_code = currency_code
        self.categories = _parse_categories(categories)
        self.countries = _parse_countries(countries)
        self.methods = _parse_methods(methods)
        self.counter_amount = counter_amount
        self.currency_symbol = currency_symbol
        self.currency_name = currency_name


_resource = {"class": CorporateRule, "name": "CorporateRule"}


def _parse_categories(categories):
    if not categories:
        return []
    parsed_categories = []
    for category in categories:
        if isinstance(category, MerchantCategory):
            parsed_categories.append(category)
            continue
        parsed_categories.append(from_api_json(_category_resource, category))
    return parsed_categories


def _parse_countries(countries):
    if not countries:
        return []
    parsed_countries = []
    for country in countries:
        if isinstance(country, MerchantCountry):
            parsed_countries.append(country)
            continue
        parsed_countries.append(from_api_json(_country_resource, country))
    return parsed_countries


def _parse_methods(methods):
    if not methods:
        return []
    parsed_methods = []
    for method in methods:
        if isinstance(method, CardMethod):
            parsed_methods.append(method)
            continue
        parsed_methods.append(from_api_json(_method_resource, method))
    return parsed_methods


def parse_rules(rules):
    parsed_rules = []
    if rules is None:
        return rules
    for rule in rules:
        if isinstance(rule, CorporateRule):
            parsed_rules.append(rule)
            continue
        parsed_rules.append(from_api_json(_resource, rule))
    return parsed_rules

