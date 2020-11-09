from datetime import datetime, timedelta
from random import randint


def randomFutureDate(days=7):
    return datetime.today() + timedelta(days=randint(1, days))


def randomFutureDatetime(days=7):
    return datetime.now() + timedelta(seconds=randint(1, days*24*3600))


def randomPastDate(days=7):
    return datetime.today() - timedelta(days=randint(1, days))


def randomPastDatetime(days=7):
    return datetime.now() - timedelta(seconds=randint(1, days*24*3600))


def randomDateBetween(after, before):
    if after > before:
        after, before = before, after
    delta = before - after
    return after + timedelta(days=randint(0, delta.days))


def randomDatetimeBetween(after, before):
    if after > before:
        after, before = before, after
    delta = before - after
    return after + timedelta(seconds=randint(0, delta.days*24*3600))
