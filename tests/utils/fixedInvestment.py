from starkbank import FixedInvestment


def generateExampleFixedInvestmentsJson(n=1, amount=100000):
    investments = []
    for _ in range(n):
        investments.append(FixedInvestment(
            amount=amount,
            type="deposit",
            tags=["python-sdk", "test"],
        ))
    return investments
