from starkbank import CorporateCard


example_card = CorporateCard(
    holder_id="",
)


def generateExampleCardJson(holder):
    example_card.holder_id = holder.id
    return example_card
