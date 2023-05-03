import starkbank
from unittest import TestCase, main
from datetime import date, timedelta
from tests.utils.holder import generateExampleHoldersJson
from tests.utils.user import exampleProject
from tests.utils.card import generateExampleCardJson

starkbank.user = exampleProject


class TestCorporateCardQuery(TestCase):

    def test_success(self):
        cards = starkbank.corporatecard.query(
            limit=10,
            after=date.today() - timedelta(days=100),
            before=date.today()
        )
        for card in cards:
            self.assertEqual(card.id, str(card.id))


class TestCorporateCardPage(TestCase):

    def test_success(self):
        cursor = None
        ids = []
        for _ in range(2):
            cards, cursor = starkbank.corporatecard.page(
                limit=2,
                after=date.today() - timedelta(days=100),
                before=date.today(),
                cursor=cursor
            )
            for card in cards:
                self.assertFalse(card.id in ids)
                ids.append(card.id)
            if cursor is None:
                break


class TestCorporateCardGet(TestCase):

    def test_success(self):
        cards = starkbank.corporatecard.query(limit=1)
        card = starkbank.corporatecard.get(id=next(cards).id)
        self.assertEqual(card.id, str(card.id))


class TestCorporateCardPostAndDelete(TestCase):

    def test_success(self):

        holder = starkbank.corporateholder.create(generateExampleHoldersJson(n=1), expand=["rules"])[0]
        card = starkbank.corporatecard.create(card=generateExampleCardJson(holder=holder), expand=["securityCode"])
        self.assertNotEqual(str(card.security_code), "***")

        card_id = card.id
        card = starkbank.corporatecard.update(card_id, display_name="Updated Name")
        self.assertEqual("Updated Name", card.display_name)

        card = starkbank.corporatecard.cancel(id=card_id)
        self.assertEqual("canceled", card.status)


class TestCorporateCardUpdate(TestCase):

    def test_success(self):
        holder = starkbank.corporateholder.create(generateExampleHoldersJson(n=1), expand=["rules"])[0]
        card = starkbank.corporatecard.create(card=generateExampleCardJson(holder=holder), expand=["securityCode"])
        self.assertIsNotNone(card.id)
        self.assertEqual(card.status, "active")
        patch_rule = [starkbank.CorporateRule(
            name="Patch Rule",
            interval="day",
            amount=989898,
            currency_code="USD",
            schedule="every monday, wednesday from 00:00 to 23:59 in America/Sao_Paulo",
            purposes=["purchase", "withdrawal"]
        )]
        update_card = starkbank.corporatecard.update(card.id, status="blocked", rules=patch_rule)
        self.assertEqual(update_card.status, "blocked")


if __name__ == '__main__':
    main()
