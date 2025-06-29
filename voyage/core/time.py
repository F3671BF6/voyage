import typing as _t

import dateutil.relativedelta as _rd
import pandas as _pd

import voyage.core.base as _b


class DateTime(_b.DateTime):
    """DateTime object to store all representations in a single object"""

    def __init__(self, value: _b.IntoDateTime) -> None:
        """Convert any Python datetime representation to the same format

        Parameters
        ----------
        value : IntoDateTime
            Anything that can be parsed as a datetime
        """
        if isinstance(value, _b.DateTime):
            value = value._timestamp
        else:
            value = _pd.Timestamp(value)

        self._timestamp = value

    def __eq__(self, value: _b.IntoDateTime) -> bool:
        value = DateTime(value)
        return self._timestamp == value._timestamp

    def __ne__(self, value: _b.IntoDateTime) -> bool:
        value = DateTime(value)
        return self._timestamp != value._timestamp

    def __le__(self, value: _b.IntoDateTime) -> bool:
        value = DateTime(value)
        return self._timestamp <= value._timestamp

    def __lt__(self, value: _b.IntoDateTime) -> bool:
        value = DateTime(value)
        return self._timestamp < value._timestamp

    def __ge__(self, value: _b.IntoDateTime) -> bool:
        value = DateTime(value)
        return self._timestamp >= value._timestamp

    def __gt__(self, value: _b.IntoDateTime) -> bool:
        value = DateTime(value)
        return self._timestamp > value._timestamp

    def __add__(self, other: _b.TimeDelta) -> "DateTime":
        result = DateTime(self._timestamp + other._relativedelta)
        return result

    def __sub__(self, other: _b.TimeDelta) -> "DateTime":
        result = DateTime(self._timestamp - other._relativedelta)
        return result


IntoDateTime: _t.TypeAlias = DateTime | _b.IntoDateTime


class TimeDelta(_b.TimeDelta):
    def __add__(self, other: IntoDateTime) -> DateTime:
        other = DateTime(other)
        result = DateTime(other._timestamp + self._relativedelta)
        return result


class Days(TimeDelta):
    period = "D"

    def __init__(self, amount: int) -> None:
        super().__init__(amount)
        self._relativedelta = _rd.relativedelta(days=amount)


class Weeks(TimeDelta):
    period = "W"

    def __init__(self, amount: int) -> None:
        super().__init__(amount)
        self._relativedelta = _rd.relativedelta(weeks=amount)


class Months(TimeDelta):
    period = "M"

    def __init__(self, amount: int) -> None:
        super().__init__(amount)
        self._relativedelta = _rd.relativedelta(months=amount)


class Years(TimeDelta):
    period = "Y"

    def __init__(self, amount: int) -> None:
        super().__init__(amount)
        self._relativedelta = _rd.relativedelta(years=amount)


class DateTimeRange:
    def __init__(
        self,
        from_date: IntoDateTime | None = None,
        to_date: IntoDateTime | None = None,
        step_size: TimeDelta = Days(1),
        step_number: int | None = None,
    ) -> None:
        pass

    def to_sequence(self) -> _t.Sequence[DateTime]:
        return []
