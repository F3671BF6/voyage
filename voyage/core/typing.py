import abc as _abc
import datetime as _dt
import typing as _t

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
