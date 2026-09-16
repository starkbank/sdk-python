from uuid import uuid4
from datetime import datetime
from starkbank import VerifiedTransfer
from starkbank.transfer import Rule


def generateExampleVerifiedTransferJson(account_id):
    return VerifiedTransfer(
        amount=1000,
        account_id=account_id,
        account_type="checking",
        external_id=str(uuid4()),
        scheduled=datetime.now(),
        tags=["verified-transfer-test"],
        description="Test description",
        display_description="Test display description",
        rules=[
            Rule(key="resendingLimit", value=5),
        ],
    )
