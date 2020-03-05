import starkbank as sb
from tests.utils.examples.credentials.credentials import credentialsJson
from tests.utils.examples.keys.keys import memberPrivateKeyString, memberPublicKeyString, sessionPrivateKeyString, \
    sessionPublicKeyString

if __name__ == "__main__":
    member = sb.Member(
        credentialsJson=credentialsJson,
        privateKeyString=memberPrivateKeyString,
        publicKeyString=memberPublicKeyString,
    )

    # content, status = sb.getBoleto(member, params={"fields": "amount,id"})
    # content, status = sb.postWebhook(member, "https://teste", subscriptions=["transfer"])
    # webhookId = content["webhook"]["id"]
    # content, status = sb.getWebhookInfo(member, webhookId=webhookId)
    # content, status = sb.deleteWebhook(member, webhookId=webhookId)
    # content, status = sb.postSession(
    #     user=member,
    #     publicKeyString=sessionPublicKeyString,
    #     platform="web"
    # )
    # print(content)
    content, status = sb.getProject(member)
    print(content)
