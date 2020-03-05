from datetime import datetime


def parse_datetime(value):
    if not isinstance(value, datetime):
        # return datetime.fromisocalendar(value)
        return value

    return datetime
