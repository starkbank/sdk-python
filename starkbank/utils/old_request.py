from json import loads

import requests

signedIn = False
accessCredentials = dict()
accessToken = ""
version = "v2"
env = "development"


def getEnvironmentSubdomain():
    return {
        "development": "development.",
        "sandbox": "sandbox.",
        "production": "",
    }[env]


def route(apiRoute):
    environmentSubdomain = getEnvironmentSubdomain()
    baseUrl = f"https://{environmentSubdomain}api.starkbank.com"
    url = f"{baseUrl}/{version}{apiRoute}"
    return url.format()


def buildQueryString(params):
    if not params:
        return ""
    args = []
    for param, value in params.items():
        if value:
            args.append(
                "{param}={value}".format(
                    param=param,
                    value=str(value) if isinstance(value, (int, str)) else ",".join(value)
                )
            )
    if not args:
        return ""
    return "?" + "&".join(args)


def get(url, headers=None, params=None):
    if not headers:
        headers = dict()
    url += buildQueryString(params)
    print("GET", url, "Headers:", headers)
    response = requests.request('GET', url, headers=headers, allow_redirects=False)
    status = response.status_code
    try:
        content = loads(response.content)
    except:
        content = response.content
    print("Status:", status)
    return content, status


def post(url, headers=None, payload=None):
    if not headers:
        headers = dict()
    if not payload:
        payload = ""
    print("POST", url, "Payload:", payload)
    response = requests.request('POST', url, headers=headers, data=payload.encode(), allow_redirects=False)
    status = response.status_code
    content = loads(response.content)
    print("Status:", status)
    return content, status


def delete(url, headers=None):
    if not headers:
        headers = dict()
    print("DELETE", url, "Headers:", headers)
    response = requests.request('DELETE', url, headers=headers, allow_redirects=False)
    content = loads(response.content)
    status = response.status_code
    print("Status:", status)
    return content, status


if __name__ == '__main__':
    pass
