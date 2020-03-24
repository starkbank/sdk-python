from datetime import datetime, timedelta
from random import randint


def randomFutureDate(days=7):
    return datetime.today() + timedelta(days=randint(1, days))


def randomPastDate(days=7):
    return datetime.today() - timedelta(days=randint(1, days))


def randomDateBetween(after, before):
    if after > before:
        after, before = before, after
    delta = before - after
    return after + timedelta(days=randint(0, delta.days))
