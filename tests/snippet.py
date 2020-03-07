import starkbank as sb
from tests.utils.examples.credentials.credentials import credentialsJson
from tests.utils.examples.keys.keys import memberPrivateKeyString, memberPublicKeyString, sessionPrivateKeyString, \
    sessionPublicKeyString

if __name__ == "__main__":

    sb.settings.env = "development"
    sb.settings.logging = "debug"

    member = sb.Member(
        private_key=memberPrivateKeyString,
        workspace_id=credentialsJson["workspaceId"],
        email=credentialsJson["email"],
    )
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
    transfers, errors = sb.transfer.list(user=member)
    # for project in content["projects"]:
    #     content, status = sb.deleteProject(member, project["id"])
    #     print(content)
    print(transfers)
