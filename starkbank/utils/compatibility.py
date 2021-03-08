from sys import version_info as pyVersion


if pyVersion.major == 3:
    from urllib.parse import urlencode
if pyVersion.major == 2:
    from urllib import urlencode
