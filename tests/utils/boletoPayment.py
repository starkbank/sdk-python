from copy import deepcopy
from hashlib import sha256
from datetime import date

from starkbank.old_boleto.boleto import postBoleto
from starkbank.old_auth.user import Member
from .boleto import generateExampleBoletos
from .examples.messages.messages import exampleBoletoPaymentsJson
from .examples.credentials.credentials import credentialsJson
from .examples.keys.keys import memberPrivateKeyString, memberPublicKeyString


def generateExampleBoletoPayments(n=1):
    boletosJson = generateExampleBoletos(n=n)

    member = Member(
        credentialsJson=credentialsJson,
        privateKeyString=memberPrivateKeyString,
        publicKeyString=memberPublicKeyString,
    )

    content, status = postBoleto(member, boletosJson=boletosJson)

    lines = [boleto["line"] for boleto in content["boletos"]]
    ids = [boleto["id"] for boleto in content["boletos"]]

    payment = exampleBoletoPaymentsJson["payments"][0]
    payments = []
    for id, line in zip(ids, lines):
        payment["line"] = line
        payment["scheduled"] = str(date.today())
        payment["description"] = sha256(str(id).encode('utf-8')).hexdigest()
        payments.append(deepcopy(payment))
    return {"payments": payments}
