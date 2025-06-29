import abc as _abc
import datetime as _dt
import typing as _t

import dateutil.relativedelta as _rd
import pandas as _pd


class DateTime(_abc.ABC):
    """Abstract base class for DateTime"""

    _timestamp: _pd.Timestamp

    @_abc.abstractmethod
    def __eq__(self, value) -> bool: ...
    @_abc.abstractmethod
    def __ne__(self, value) -> bool: ...
    @_abc.abstractmethod
    def __le__(self, value) -> bool: ...
    @_abc.abstractmethod
    def __lt__(self, value) -> bool: ...
    @_abc.abstractmethod
    def __ge__(self, value) -> bool: ...
    @_abc.abstractmethod
    def __gt__(self, value) -> bool: ...


IntoDateTime: _t.TypeAlias = DateTime | _dt.date | _dt.datetime | _pd.Timestamp | str


class TimeDelta:
    period: str
    amount: int
    _relativedelta: _rd.relativedelta

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def __repr__(self) -> str:
        return f"{self.amount}{self.period}"

    def __eq__(self, other: "TimeDelta") -> bool:
        return (self.amount == 0 and other.amount == 0) or (
            self.period == other.period and self.amount == other.amount
        )
