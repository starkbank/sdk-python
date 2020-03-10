from sys import version_info


if version_info.major == 3:
    from urllib.parse import urlencode
else:
    from urllib import urlencode
