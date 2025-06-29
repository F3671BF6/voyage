from datetime import date, datetime

from pandas import Timestamp

from voyage.core.time import DateTime


def test_datetime_init():
    x = DateTime("2020-01-01 00:00")
    y = DateTime(date(2020, 1, 1))
    w = DateTime(datetime(2020, 1, 1, 0, 0))
    z = DateTime(Timestamp("2020-01-01"))
    x_p = DateTime(x)

    assert x == y
    assert x == w
    assert x == z
    assert x == x_p


def test_ordering():
    x = DateTime("2020-01-01 12:30")

    # same
    other = DateTime(x)
    assert x == other
    assert not (x != other)
    assert x <= other
    assert not (x < other)
    assert x >= other
    assert not (x > other)

    # before
    other = DateTime("2020-01-01 11:30")
    assert not (x == other)
    assert x != other
    assert not (x <= other)
    assert not (x < other)
    assert x >= other
    assert x > other

    # after
    other = DateTime("2020-01-01 13:30")
    assert not (x == other)
    assert x != other
    assert x <= other
    assert x < other
    assert not (x >= other)
    assert not (x > other)
