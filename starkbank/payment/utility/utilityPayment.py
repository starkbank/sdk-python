from ...utils import rest
from ...utils.checks import check_datetime, check_date
from ...utils.resource import Resource


class UtilityPayment(Resource):

    def __init__(self, line, bar_code, tags, description, due, scheduled, id=None, amount=None, status=None, created=None):
        Resource.__init__(self, id=id)

        self.line = line
        self.bar_code = bar_code
        self.due = check_datetime(due)
        self.description = description
        self.tags = tags
        self.scheduled = check_datetime(scheduled)
        self.status = status
        self.amount = amount
        self.created = check_datetime(created)


def create(payments, user=None):
    return rest.post(resource=UtilityPayment, entities=payments, user=user)


def get(id, user=None):
    return rest.get_id(resource=UtilityPayment, id=id, user=user)


def query(limit=None, status=None, after=None, before=None, tags=None, ids=None, user=None):
    return rest.get_list(resource=UtilityPayment, limit=limit, user=user, status=status, tags=tags, after=check_date(after), before=check_date(before), ids=ids)


def delete(ids, user=None):
    assert isinstance(ids, (list, tuple, set)), "ids must be a list"
    return rest.delete_list(resource=UtilityPayment, ids=ids, user=user)
