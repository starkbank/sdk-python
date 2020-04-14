from . import api, resource, case, checks, enum, request, rest
from .cache import cache

import sys
if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding("UTF8")
