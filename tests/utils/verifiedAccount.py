from starkbank import VerifiedAccount


def generateExampleBankInfoVerifiedAccountJson():
    return VerifiedAccount(
        tax_id="911.544.440-66",
        name="Daenerys Targaryen Stormborn",
        bank_code="341",
        branch_code="2201",
        number="76543-8",
        type="checking",
        tags=["verified-account-test"],
    )


def generateExamplePixKeyVerifiedAccountJson():
    return VerifiedAccount(
        tax_id="039.946.040-36",
        key_id="arya.stark@starkbank.com",
        tags=["verified-account-test"],
    )
