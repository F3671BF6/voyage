from datetime import date, datetime

from pandas import Timestamp
from pytest import raises

from voyage.core.time import DateTime, Days, Months, Weeks, Years


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


def test_timedelta():
    x = DateTime("2020-01-01 12:30")
    assert x + Days(2) == DateTime("2020-01-03 12:30")
    assert x - Days(2) == DateTime("2019-12-30 12:30")
    assert Days(2) + x == DateTime("2020-01-03 12:30")
    with raises(TypeError):
        Days(2) - x  # type:ignore

    assert x + Weeks(2) == DateTime("2020-01-15 12:30")
    assert x - Weeks(2) == DateTime("2019-12-18 12:30")

    assert x + Months(2) == DateTime("2020-03-01 12:30")
    assert x - Months(2) == DateTime("2019-11-01 12:30")

    assert x + Years(2) == DateTime("2022-01-01 12:30")
    assert x - Years(2) == DateTime("2018-01-01 12:30")
